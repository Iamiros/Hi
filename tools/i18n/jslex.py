"""Tiny JS lexer: finds string literals and template-literal text segments.
Yields (kind, start, end, depth) where kind is 'str' (quoted, incl. quotes) or 'tpl' (raw text
segment inside a template literal). depth = brace depth of code at that point (0 = top level)."""
import re
PUNCT_BEFORE_REGEX = set('(,=:[!&|?{};+-*%<>~^')
def lex(src, start=0, end=None):
    end = len(src) if end is None else end
    i, out, stack, depth, last = start, [], [], 0, ''
    # stack holds frames: ('tpl',) inside template text, ('expr', braces) inside ${ }
    while i < end:
        c = src[i]
        if stack and stack[-1][0] == 'tpl':
            j = i
            while j < end:
                if src[j] == '\\': j += 2; continue
                if src[j] == '`' or src.startswith('${', j): break
                j += 1
            if j > i: out.append(('tpl', i, j, depth))
            if src[j] == '`': stack.pop(); i = j + 1; last = '`'
            else: stack.append(['expr', 0]); i = j + 2; last = '{'
            continue
        if c in ' \t\r\n': i += 1; continue
        if src.startswith('//', i): i = src.index('\n', i); continue
        if src.startswith('/*', i): i = src.index('*/', i) + 2; continue
        if c in '"\'':
            j = i + 1
            while src[j] != c:
                j += 2 if src[j] == '\\' else 1
            out.append(('str', i, j + 1, depth)); i = j + 1; last = 'a'; continue
        if c == '`': stack.append(('tpl',)); i += 1; continue
        if c == '/' and (last in PUNCT_BEFORE_REGEX or last == '' or re.search(r'\b(return|typeof|case)\s*$', src[max(0,i-10):i])):
            j, cls = i + 1, False
            while True:
                ch = src[j]
                if ch == '\\': j += 2; continue
                if ch == '[': cls = True
                elif ch == ']': cls = False
                elif ch == '/' and not cls: break
                j += 1
            i = j + 1
            while i < end and src[i].isalpha(): i += 1
            last = 'a'; continue
        if c == '{':
            if stack and stack[-1][0] == 'expr': stack[-1][1] += 1
            depth += 1
        elif c == '}':
            if stack and stack[-1][0] == 'expr':
                if stack[-1][1] == 0: stack.pop(); i += 1; last = 'a'; continue
                stack[-1][1] -= 1
            depth -= 1
        last = c if not (c.isalnum() or c in '_$)].') else 'a'
        i += 1
    return out
FA = re.compile(r'[؀-ۿ]')
FALETTER = re.compile(r'[\u0621-\u064A\u067E\u0686\u0698\u06A9\u06AF\u06CC]')
