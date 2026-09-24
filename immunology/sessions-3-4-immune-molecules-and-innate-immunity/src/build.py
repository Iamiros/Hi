#!/usr/bin/env python3
import sys, os, glob, re
from bs4 import BeautifulSoup, NavigableString

BUILD = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'build')
PARTS = ['00_front.html','01_toc.html','02_part1.html','03_part2.html',
         '04_part3.html','05_part4.html','06_part5.html','07_part6.html',
         '08_part7.html','09_part8.html','10_review.html']

def read_parts():
    out=[]
    for p in PARTS:
        fp=os.path.join(BUILD,p)
        if os.path.exists(fp):
            out.append(open(fp,encoding='utf-8').read())
    return '\n'.join(out)

SHELL = """<!DOCTYPE html><html lang="{lang}"><head><meta charset="utf-8">
<title>Medical Immunology — Sessions 3 &amp; 4</title>
<link rel="stylesheet" href="base.css">{extra}
</head><body>
{body}
</body></html>"""

BLOCK_PARENTS = {'p','h1','h2','h3','h4','h5','div','li','dd','dt','blockquote','figcaption','caption','span','ol','ul'}

def transform(html, bilingual):
    soup = BeautifulSoup(html, 'html.parser')
    if not bilingual:
        for el in soup.select('.toc-fa'):
            el.decompose()
    for h in soup.find_all(['h1']):
        cls = h.get('class') or []
        if 'tp-title' in cls or 'part-title' in cls or 'fm-h' in cls:
            txt = ' '.join(t for t in h.find_all(string=True, recursive=True)
                           if not (t.parent and t.parent.name == 'fa'))
            h['data-bm'] = ' '.join(txt.split())
    for h in soup.find_all('h2'):
        sn = h.find('span', class_='sn')
        if sn is not None:
            sn.insert_after(NavigableString(' '))
    for fa in soup.find_all('fa'):
        if not bilingual:
            fa.decompose(); continue
        parent = fa.parent
        pname = parent.name if parent else 'div'
        # build replacement div
        new = soup.new_tag('div')
        new['class'] = ['fa-block']
        # move children
        for c in list(fa.contents):
            new.append(c.extract())
        if pname in ('td','th'):
            new['class'] = ['fa-cell']
            fa.replace_with(new)
        elif pname == 'li':
            new['class'] = ['fa-block','fa-li']
            fa.extract(); parent.append(new)
        elif pname == 'h1':
            new['class'] = ['fa-block','fa-h1']
            fa.extract(); parent.append(new)
        elif pname in ('h2','h3','h4','h5'):
            new['class'] = ['fa-block','fa-'+pname]
            fa.extract()
            parent.insert_after(new)
        elif pname in ('figcaption','caption','dd','dt'):
            fa.extract(); parent.append(new)
        elif pname in ('p','div','span','blockquote'):
            fa.extract()
            # insert after the parent block if parent is p/blockquote, else append inside
            if pname in ('p','blockquote'):
                parent.insert_after(new)
            else:
                parent.append(new)
        else:
            fa.extract(); parent.append(new)
    return str(soup)

def build(outfile, bilingual, label):
    body = read_parts().replace('EDITION_LABEL', label)
    body = transform(body, bilingual)
    extra = '<link rel="stylesheet" href="bilingual.css">' if bilingual else ''
    html = SHELL.format(lang='en', extra=extra, body=body)
    tmp = os.path.join(BUILD, '_render_%s.html' % ('bi' if bilingual else 'en'))
    open(tmp,'w',encoding='utf-8').write(html)
    from weasyprint import HTML
    HTML(tmp, base_url=os.path.join(BUILD,'x')).write_pdf(outfile)
    try:
        import pymupdf
        d = pymupdf.open(outfile)
        d.set_metadata({
            'title': 'Medical Immunology — Sessions 3 & 4: Immune Molecules and Innate Immunity (%s)' % label,
            'author': 'Amirhossein Dehghan',
            'subject': 'CD molecules and leukocyte differentiation antigens, the three-signal model of T cell activation, MHC/HLA class I and II, cytokines and their receptors, JAK-STAT signalling, innate immunity, PAMPs and DAMPs, Toll-like receptors, NF-kB, the inflammasome, caspase-1, gasdermin D and pyroptosis, cytokine storm and anti-cytokine therapy',
            'keywords': 'immunology, CD molecules, CD3, CD4, CD8, CD28, CTLA-4, costimulation, three-signal model, MHC, HLA, class I, class II, cytokines, IL-2, JAK-STAT, SOCS, common gamma chain, SCID, ALPS, innate immunity, PAMP, DAMP, PRR, Toll-like receptor, MyD88, NF-kB, RIG-I, inflammasome, NLRP3, ASC, caspase-1, gasdermin D, pyroptosis, IL-1beta, cytokine storm, anti-TNF',
            'creator': 'WeasyPrint',
        })
        d.saveIncr() if False else d.save(outfile + '.tmp')
        d.close()
        os.replace(outfile + '.tmp', outfile)
    except Exception as e:
        print('metadata skipped:', e)
    print('wrote', outfile, os.path.getsize(outfile)//1024, 'KB')

if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv)>1 else 'both'
    outdir = sys.argv[2] if len(sys.argv)>2 else '.'
    if which in ('en','both'):
        build(os.path.join(outdir,'immunology-sessions3-4-english.pdf'), False, 'Full English Edition')
    if which in ('bi','both'):
        build(os.path.join(outdir,'immunology-sessions3-4-bilingual.pdf'), True, 'Bilingual Edition · English + فارسی')
