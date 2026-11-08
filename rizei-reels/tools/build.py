"""Embed assets into src/reels.template.html -> dist/index.html (single self-contained file)."""
import base64, json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = lambda *p: os.path.join(ROOT, 'assets', *p)
s = open(os.path.join(ROOT, 'src', 'reels.template.html'), encoding='utf-8').read()
uri = lambda p, m: f'data:{m};base64,' + base64.b64encode(open(p, 'rb').read()).decode()
for k in ['R', 'I', 'Z', 'Zfull', 'E', 'I2', 'K1', 'K2', 'D']:
    s = s.replace('{{%s}}' % k, uri(A(k + '.png'), 'image/png'))
fonts = {'F_INTER300': 'inter-latin-300-normal', 'F_INTER400': 'inter-latin-400-normal',
         'F_CG500': 'cormorant-garamond-latin-500-normal', 'F_CG600': 'cormorant-garamond-latin-600-normal'}
for k, f in fonts.items():
    s = s.replace('{{%s}}' % k, uri(A('fonts', f + '.woff2'), 'font/woff2'))
s = s.replace('{{LAYOUT}}', json.dumps(json.load(open(A('layout.json')))))
assert '{{' not in s, 'placeholder left'
out = os.path.join(ROOT, 'dist', 'index.html'); open(out, 'w', encoding='utf-8').write(s)
print(out, len(s))
