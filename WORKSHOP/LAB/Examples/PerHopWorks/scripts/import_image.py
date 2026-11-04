"""Convert an inspected generated image to the project's requested WebP delivery format."""
import argparse,hashlib,json
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('id');p.add_argument('source');args=p.parse_args()
im=Image.open(args.source);im.load();im.thumbnail((2048,2048));out=ROOT/f'assets/images/{args.id}.webp';out.parent.mkdir(exist_ok=True)
quality=90
while True:
    im.save(out,'WEBP',quality=quality,method=6)
    if out.stat().st_size<=400000: break
    quality-=5
    if quality<30: raise RuntimeError('Image exceeds budget at minimum quality')
m=ROOT/'assets/manifest.json';d=json.loads(m.read_text());d.setdefault('images',[])
if any(x['id']==args.id for x in d['images']): raise RuntimeError('Refusing duplicate manifest id')
d['images'].append({'id':args.id,'path':str(out.relative_to(ROOT)),'prompt':f'assets/prompts/{args.id}.json','generator':'ChatGPT built-in image_gen','model':'not exposed by tool','source_generated_path':args.source,'created_on':'2026-11-04','reference':None if args.id=='title' else 'assets/images/title.webp','width':im.width,'height':im.height,'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'license':'Original AI-generated project art; no third-party source image','review':{'reviewer':'Codex visual inspection under owner continuing authorization','status':'accepted','text_digits_glyphs':'none observed','note':'Decorative art; teaching diagrams and exact bit states are generated from data.'}})
m.write_text(json.dumps(d,indent=2)+'\n');print(out,im.size,out.stat().st_size)
