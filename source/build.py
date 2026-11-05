t=open('template4.html',encoding='utf-8').read()
r=lambda n:open(f'assets/{n}.b64').read()
m={'__FONTS__':open('fonts.css',encoding='utf-8').read(),'__MENU__':open('menu_data.js',encoding='utf-8').read(),
'__GRAIN__':r('grain'),'__LOGO_NAV__':r('logo_nav'),'__LOGO_HERO__':r('logo_hero'),'__LOGO_AR__':r('logo_ar'),
'__MASCOT_CHILI__':r('mascot_chili'),'__MASCOT_ROOSTER__':r('mascot_rooster'),'__MASCOT_DINO__':r('mascot_dino'),'__MASCOT_FRIES__':r('mascot_fries'),
'__LOGO_ICCA__':r('icca'),'__LOGO_UFS__':r('ufs'),'__LOGO_WCA__':r('wca'),'__LOGO_CLOUD__':r('cloud'),'__LOGO_EFOOD__':r('efood'),'__LOGO_SAFEFOOD__':r('safefood')}
import json
m['__FAVICON__']=r('favicon')
m['__PHOTOS__']=json.dumps(json.load(open('photos.json')))
for k,v in m.items():
    assert k in t,k; t=t.replace(k,v)
open('index_v10.html','w',encoding='utf-8').write(t); print(len(t)//1024,'KB')
