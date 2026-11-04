import json,struct,hashlib
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
budgets={'floor_tile':300,'belt_straight':300,'belt_corner':300,'buffer_belt':1500,'sorter':4000,'paint_booth':4000,'tank_single':3000,'tank_cascade':5000,'tank_twin':5000,'recycler':3000,'priority_merger':5000,'dock_in':3000,'dock_out':3000,'crate_s':400,'crate_m':400,'crate_l':400,'hall':20000}
manifest={'schemaVersion':1,'models':[],'images':[]}
old=ROOT/'assets/manifest.json'
previous=json.loads(old.read_text()) if old.exists() else {}
manifest['images']=previous.get('images',[])
if 'continuing_authorization' in previous:manifest['continuing_authorization']=previous['continuing_authorization']
prior_models={m['id']:m for m in previous.get('models',[])}
for name,budget in budgets.items():
 id='phw_'+name;path=ROOT/f'assets/models/{id}.glb';blob=path.read_bytes();length=struct.unpack_from('<I',blob,12)[0];doc=json.loads(blob[20:20+length]);triangles=sum(doc['accessors'][p['indices']]['count']//3 for m in doc['meshes'] for p in m['primitives'])
 manifest['models'].append({'id':id,'path':str(path.relative_to(ROOT)),'generator':'Blender 5.2.1 LTS through mcp-for-blender 2.2.7','script':f'assets/src/blender/{id}.py','shared_recipe':'assets/src/blender/common.py','blend':f'assets/src/blender/{id}.blend','review_sheet':f'research/assets/{id}-angles-0.png','mcp_build_record':f'research/assets/{id}-build.json','mcp_review_record':f'research/assets/{id}-look.json','created_on':datetime.now(timezone.utc).isoformat(),'sha256':hashlib.sha256(blob).hexdigest(),'bytes':len(blob),'triangles':triangles,'triangle_budget':budget,'nodes':[n.get('name') for n in doc['nodes']],'license':'Original procedural project asset; no third-party model or texture','human_review':{'status':'pending','approver':None}})
for model in manifest['models']:
 prior=prior_models.get(model['id'],{})
 if prior.get('sha256')==model['sha256']:
  model['human_review']=prior.get('human_review',model['human_review'])
  model['created_on']=prior.get('created_on',model['created_on'])
old.write_text(json.dumps(manifest,indent=2)+'\n');print(json.dumps({'models':len(manifest['models']),'bytes':sum(m['bytes'] for m in manifest['models']),'triangles':sum(m['triangles'] for m in manifest['models']),'over_budget':[m['id'] for m in manifest['models'] if m['triangles']>m['triangle_budget']]},indent=2))
