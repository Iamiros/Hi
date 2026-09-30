#!/usr/bin/env python3
import sys, os, socket, threading, http.server, functools, time
from bs4 import BeautifulSoup, NavigableString

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, 'build')
PARTS = ['00_front.html', '01_toc.html',
         '02_part1_bench.html', '03_part2_baseline.html',
         '04_part3_specimens.html', '05_part3_specimens2.html',
         '06_review.html']

def read_parts():
    out = []
    for p in PARTS:
        fp = os.path.join(BUILD, p)
        if os.path.exists(fp):
            out.append(open(fp, encoding='utf-8').read())
    return '\n'.join(out)

SHELL = """<!DOCTYPE html><html lang="{lang}"><head><meta charset="utf-8">
<title>Cell and Tissue Injury and Repair (3) — Pathology Lab Session 3</title>
<link rel="stylesheet" href="base.css">{extra}
<script>window.PagedConfig = {{ after: function(flow){{ window.__pagedDone = true; window.__pagedCount = flow ? flow.total : 0; }} }};</script>
<script src="../vendor/paged.polyfill.js"></script>
</head><body>
{body}
</body></html>"""

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
        new = soup.new_tag('div')
        new['class'] = ['fa-block']
        for c in list(fa.contents):
            new.append(c.extract())
        if pname in ('td', 'th'):
            new['class'] = ['fa-cell']
            fa.replace_with(new)
        elif pname == 'li':
            new['class'] = ['fa-block', 'fa-li']
            fa.extract(); parent.append(new)
        elif pname == 'h1':
            new['class'] = ['fa-block', 'fa-h1']
            fa.extract(); parent.append(new)
        elif pname in ('h2', 'h3', 'h4', 'h5'):
            new['class'] = ['fa-block', 'fa-' + pname]
            fa.extract(); parent.insert_after(new)
        elif pname in ('figcaption', 'caption', 'dd', 'dt'):
            fa.extract(); parent.append(new)
        elif pname in ('p', 'div', 'span', 'blockquote'):
            fa.extract()
            if pname in ('p', 'blockquote'):
                parent.insert_after(new)
            else:
                parent.append(new)
        else:
            fa.extract(); parent.append(new)
    return str(soup)

def free_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0)); port = s.getsockname()[1]; s.close()
    return port

def serve(directory, port):
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=directory)
    srv = http.server.ThreadingHTTPServer(('127.0.0.1', port), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv

def render_pdf(html_path, out_pdf, port):
    from playwright.sync_api import sync_playwright
    rel = os.path.relpath(html_path, HERE)
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
        page = browser.new_page()
        errs = []
        page.on('pageerror', lambda e: errs.append(str(e)))
        page.goto(f'http://127.0.0.1:{port}/{rel}', wait_until='load')
        page.wait_for_function('window.__pagedDone === true', timeout=180000)
        n = page.evaluate("document.querySelectorAll('.pagedjs_page').length")
        page.pdf(path=out_pdf, print_background=True, prefer_css_page_size=True)
        browser.close()
    if errs:
        print('  page errors:', errs)
    print('  paged.js produced', n, 'pages')

def build(outfile, bilingual, label, port):
    body = read_parts().replace('EDITION_LABEL', label)
    body = transform(body, bilingual)
    extra = '<link rel="stylesheet" href="bilingual.css">' if bilingual else ''
    html = SHELL.format(lang='en', extra=extra, body=body)
    tmp = os.path.join(BUILD, '_render_%s.html' % ('bi' if bilingual else 'en'))
    open(tmp, 'w', encoding='utf-8').write(html)
    render_pdf(tmp, outfile, port)
    try:
        import pymupdf
        d = pymupdf.open(outfile)
        d.set_metadata({
            'title': 'Cell and Tissue Injury and Repair (3) — Pathology Lab Session 3 (%s)' % label,
            'author': 'Amirhossein Dehghan',
            'subject': 'Necrosis subtypes, gangrene, granulation tissue, and fracture repair: '
                       'specimen-by-specimen spot-exam guide. Zhejiang University lecture slides.',
            'keywords': 'pathology lab, necrosis, gangrene, granulation tissue, fracture repair, spleen, liver, appendix',
            'creator': 'Playwright Chromium + paged.js',
        })
        d.save(outfile + '.tmp')
        d.close()
        os.replace(outfile + '.tmp', outfile)
    except Exception as e:
        print('metadata skipped:', e)
    print('wrote', outfile, os.path.getsize(outfile) // 1024, 'KB')

if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'both'
    outdir = sys.argv[2] if len(sys.argv) > 2 else '.'
    port = free_port()
    srv = serve(HERE, port)
    time.sleep(0.3)
    try:
        if which in ('en', 'both'):
            build(os.path.join(outdir, 'pathology-lab3-english.pdf'), False, 'Full English Edition', port)
        if which in ('bi', 'both'):
            build(os.path.join(outdir, 'pathology-lab3-bilingual.pdf'), True, 'Bilingual Edition · English + فارسی', port)
    finally:
        srv.shutdown()
