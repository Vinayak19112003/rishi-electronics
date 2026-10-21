from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote
import json
import xml.etree.ElementTree as ET

root=Path(__file__).resolve().parent/'dist'
errors=[]
class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.ids=set();self.refs=[];self.images=[];self.h1=0;self.title=0;self.dialog=False;self.labels=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:
            if a['id'] in self.ids:errors.append('Duplicate ID '+a['id'])
            self.ids.add(a['id'])
        if tag=='h1':self.h1+=1
        if tag=='title':self.title+=1
        if tag=='dialog':self.dialog=True
        for attr in ['src','href']:
            if a.get(attr):self.refs.append(a[attr])
        if tag=='img':
            self.images.append(a)
            if 'alt' not in a:errors.append('Image missing alt')
        if tag=='script' and a.get('src') and not a['src'].startswith('/'):errors.append('Unexpected third-party script')

pages=list(root.rglob('*.html'))
for file in pages:
    p=Page();p.feed(file.read_text());name=str(file.relative_to(root))
    if p.h1!=1:errors.append(f'{name}: expected one h1, got {p.h1}')
    if p.title!=1:errors.append(f'{name}: expected title')
    if not p.dialog:errors.append(f'{name}: request dialog missing')
    for ref in p.refs:
        parsed=urlparse(ref)
        if parsed.scheme or parsed.netloc:continue
        if not parsed.path and parsed.fragment:
            if parsed.fragment not in p.ids:errors.append(f'{name}: broken fragment {ref}')
            continue
        dest=(root/unquote(parsed.path).lstrip('/')) if parsed.path.startswith('/') else file.parent/unquote(parsed.path)
        if dest.is_dir():dest=dest/'index.html'
        if not dest.is_file():errors.append(f'{name}: missing {ref}')
    for node in p.images:
        if not node.get('width') or not node.get('height'):errors.append(f'{name}: missing image dimensions')

assert len(pages)==12,len(pages)
manifest=json.loads((root.parent/'.openai/hosting.json').read_text())
assert manifest['static']['directory']=='dist'
assert manifest['project_id']=='appgprj_6ad82ffecb248191872854719263ea99'
ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
assert len(ET.parse(root/'sitemap.xml').findall('s:url',ns))==12
home=(root/'index.html').read_text()
assert home.count('class="service-card"')==9
assert '5.0 Rating' not in home
assert not errors, '\n'.join(errors)
print(f'Passed: {len(pages)} pages, 9 service routes, sitemap, image references, local links and core HTML checks.')
