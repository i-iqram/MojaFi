import re,hashlib,os,shutil,sys
from PIL import Image
src=open('index_v10.html',encoding='utf-8').read()
out='dist'; shutil.rmtree(out,ignore_errors=True); os.makedirs(out+'/assets')
import base64
ext={'image/jpeg':'jpg','image/png':'png','image/webp':'webp','font/woff2':'woff2'}
seen={}
def sub(m):
    mime,b=m.group(1),m.group(2)
    if mime not in ext: return m.group(0)
    h=hashlib.md5(b.encode()).hexdigest()[:10]; fn=f'assets/{h}.{ext[mime]}'
    if h not in seen:
        open(f'{out}/{fn}','wb').write(base64.b64decode(b)); seen[h]=fn
    return fn
html=re.sub(r'data:([a-z/0-9+.-]+);base64,([A-Za-z0-9+/=]+)',sub,src)
# preload main fonts (first two woff2 of Baloo/Hind latin/bengali used above the fold)
fonts=[]
for m in re.finditer(r'@font-face\s*\{.*?\}',html,re.S):
    b=m.group(0); fam=re.search(r"font-family:\s*['\"]?([^;'\"]+)",b).group(1).strip(); w=re.search(r'font-weight:\s*([^;]+)',b).group(1).strip(); u=re.search(r'(assets/\w+\.woff2)',b)
    if u: fonts.append((fam,w,u.group(1)))
print(fonts)
pre=''  # fonts stay inline (file:// safe)
_unused=''.join(f'<link rel="preload" as="font" type="font/woff2" crossorigin href="{u}">\n' for f,w,u in fonts if f=='Baloo Da 2' or (f=='Hind Siliguri' and w=='400'))
hl=re.search(r'class="main-logo" src="(assets/[^"]+)"',html).group(1)
pre+=f'<link rel="preload" as="image" href="{hl}" fetchpriority="high">\n'
html=html.replace('<link rel="canonical"',pre+'<link rel="canonical"',1)
html=html.replace('<link rel="icon" type="image/png" href="assets/','<link rel="icon" type="image/png" href="assets/',1)
open(f'{out}/index.html','w',encoding='utf-8').write(html)
print(len(html),len(seen),sum(os.path.getsize(f'{out}/{v}') for v in seen.values()))

import json
from PIL import Image
for f in('robots.txt','sitemap.xml','logo.png'): shutil.copy('seo_out/'+f,out+'/'+f)
shutil.copy('og2.jpg',out+'/og-image.jpg')
im=Image.open('seo_out/logo.png').convert('RGBA'); im.save(out+'/favicon.ico',sizes=[(16,16),(32,32),(48,48)])
open(out+'/.htaccess','w').write("""# MojaFi — Apache/cPanel hosting settings (safe to leave as is)
<IfModule mod_deflate.c>
AddOutputFilterByType DEFLATE text/html text/css application/javascript application/json text/xml application/xml image/svg+xml
</IfModule>
<IfModule mod_expires.c>
ExpiresActive On
ExpiresByType image/jpeg "access plus 1 year"
ExpiresByType image/png "access plus 1 year"
ExpiresByType image/webp "access plus 1 year"
ExpiresByType font/woff2 "access plus 1 year"
ExpiresByType text/html "access plus 10 minutes"
</IfModule>
<IfModule mod_headers.c>
<FilesMatch "\\.(jpg|png|webp|woff2|ico)$">
Header set Cache-Control "public, max-age=31536000, immutable"
</FilesMatch>
Header always set X-Content-Type-Options "nosniff"
Header always set Referrer-Policy "strict-origin-when-cross-origin"
</IfModule>
ErrorDocument 404 /404.html
""")
open(out+'/404.html','w',encoding='utf-8').write("""<!doctype html><html lang="bn"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex"><title>404 — MojaFi</title>
<style>body{margin:0;min-height:100vh;display:grid;place-items:center;background:#FFF6E0;color:#16114F;font-family:system-ui,sans-serif;text-align:center;padding:24px}h1{font-size:4rem;margin:0}a{display:inline-block;margin-top:16px;background:#D81B60;color:#fff;padding:12px 24px;border-radius:999px;text-decoration:none;font-weight:800}</style></head>
<body><main><h1>404 😅</h1><p>এই page-টা খুঁজে পাওয়া যায়নি, বস! খাবারটা কিন্তু হোমপেজেই আছে।</p><a href="/">MojaFi হোমে যান</a></main></body></html>""")
