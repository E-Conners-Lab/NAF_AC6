"""Run saved recipes and actual multi-angle look calls through one Blender MCP process."""
import asyncio,base64,json,os,sys,hashlib
from pathlib import Path
from datetime import datetime,timezone
from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client
ROOT=Path(__file__).resolve().parents[1]
PROMPT='what gates install them let me know if when you need me to reload blender cli should be available no hurdles here'
async def main():
 names=sys.argv[1:] or [p.stem for p in sorted((ROOT/'assets/src/blender').glob('phw_*.py'))]
 params=StdioServerParameters(command='uvx',args=['--from','mcp-for-blender==2.2.7','mcp-for-blender'],env={**os.environ,'DISABLE_TELEMETRY':'true'})
 async with stdio_client(params) as (read,write):
  async with ClientSession(read,write) as s:
   await s.initialize()
   for name in names:
    script=ROOT/f'assets/src/blender/{name}.py'
    code=f"import runpy\nrunpy.run_path({str(script)!r},run_name='__main__')"
    result=await s.call_tool('execute_blender_code',{'code':code,'user_prompt':PROMPT})
    payload=result.model_dump(mode='json');(ROOT/f'research/assets/{name}-build.json').write_text(json.dumps({'at':datetime.now(timezone.utc).isoformat(),'tool':'execute_blender_code','arguments':{'code':code,'user_prompt':PROMPT},'result':payload},indent=2))
    text='\n'.join(getattr(c,'text','') for c in result.content)
    print(name,text[-1600:],flush=True)
    if bool(getattr(result,'is_error',getattr(result,'isError',False))) or 'PHW_ASSET ' not in text:raise RuntimeError('Blender recipe failed: '+name)
    prep="import bpy\n_phw_visibility=[(o,o.hide_get()) for o in bpy.context.scene.objects]\nfor o in bpy.context.scene.objects:\n o.hide_set(not any(c.name.startswith('PHW_') for c in o.users_collection));o.select_set(False)\nfor a in bpy.context.screen.areas:\n if a.type=='VIEW_3D':\n  a.spaces.active.shading.color_type='VERTEX';a.spaces.active.overlay.show_overlays=False\nbpy.context.view_layer.update()"
    await s.call_tool('execute_blender_code',{'code':prep,'user_prompt':PROMPT})
    lookargs={'mode':'angles','target':[name],'views':['front','right','top','three_quarter'],'shading':'solid','max_size':1400,'user_prompt':PROMPT}
    review=await s.call_tool('look',lookargs)
    record={'at':datetime.now(timezone.utc).isoformat(),'tool':'look','arguments':lookargs,'text':[],'images':[]}
    for i,c in enumerate(review.content):
     if c.type=='image':
      out=ROOT/f'research/assets/{name}-angles-{i}.png';out.write_bytes(base64.b64decode(c.data));record['images'].append(str(out.relative_to(ROOT)))
     elif c.type=='text':record['text'].append(c.text)
    (ROOT/f'research/assets/{name}-look.json').write_text(json.dumps(record,indent=2))
    await s.call_tool('execute_blender_code',{'code':"for o,hidden in _phw_visibility: o.hide_set(hidden)",'user_prompt':PROMPT})
    if not record['images']:raise RuntimeError('No look image returned: '+str(record))
    print('LOOK',name,record['images'],flush=True)
if __name__=='__main__':asyncio.run(main())
