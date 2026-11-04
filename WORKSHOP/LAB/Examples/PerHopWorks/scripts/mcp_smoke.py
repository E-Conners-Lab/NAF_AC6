"""Live MCP bootstrap checks; writes exact tool responses, never fabricated fact evidence.
Run: uv run --with mcp python scripts/mcp_smoke.py rfc|blender
"""
import asyncio
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'research/tool-results'
OUTPUT.mkdir(parents=True, exist_ok=True)

async def main(kind):
    args = [str(ROOT / 'tools/rfc-mcp/compat.mjs')] if kind == 'rfc' else ['--from', 'mcp-for-blender==2.2.7', 'mcp-for-blender']
    params = StdioServerParameters(command='node' if kind == 'rfc' else 'uvx', args=args,
        env={**os.environ, 'DISABLE_TELEMETRY': 'true'})
    records = []
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            listed = await session.list_tools()
            (OUTPUT / f'{kind}-tools.json').write_text(listed.model_dump_json(indent=2))
            async def call(name, arguments):
                response = await session.call_tool(name, arguments)
                payload = response.model_dump(mode='json')
                rec = {'time': datetime.now(timezone.utc).isoformat(), 'tool': name,
                       'arguments': arguments, 'result': payload}
                records.append(rec)
                (OUTPUT / f'{kind}-smoke.json').write_text(json.dumps(records, indent=2) + '\n')
                return '\n'.join(getattr(x, 'text', '') for x in response.content), bool(getattr(response, 'is_error', getattr(response, 'isError', False)))
            if kind == 'rfc':
                raw, error = await call('get_rfc', {'number': '2474', 'format': 'metadata'})
                print('RFC 2474 metadata:', raw[:1800])
                title_ok = not error and 'differentiated services' in raw.lower()
                section, section_error = await call('get_rfc_section', {'number': '4594', 'section': '4.3'})
                numeric_ok = not section_error and 'AF41' in section
                print('RFC 4594 numeric section:', section[:1000])
                if not numeric_ok:
                    section, section_error = await call('get_rfc_section', {'number': '4594', 'section': 'Multimedia Conferencing Service Class'})
                    print('RFC 4594 title section:', section[:1600])
                section_ok = not section_error and 'AF41' in section
                status = {'title_passed': title_ok, 'section_passed': section_ok,
                          'section_lookup': 'number' if numeric_ok else 'title', 'passed': title_ok and section_ok}
            else:
                raw, error = await call('get_addon_status', {'user_prompt': 'Install the Blender MCP and verify its addon and GLB export for Per-Hop Works.'})
                print('Blender addon status:', raw[:2500])
                status = {'addon_error': error, 'passed': False}
                if not error:
                    target = ROOT / 'assets/models/_smoke.glb'
                    code = f'''import bpy, json
bpy.ops.mesh.primitive_cube_add(size=1, location=(0,0,0.5))
smoke = bpy.context.object
smoke.name = "phw_mcp_smoke_cube"
bpy.ops.object.select_all(action='DESELECT')
smoke.select_set(True)
bpy.context.view_layer.objects.active = smoke
bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
bpy.ops.export_scene.gltf(filepath={str(target)!r}, export_format='GLB', use_selection=True, export_yup=True)
bpy.data.objects.remove(smoke, do_unlink=True)
print("PHW_SMOKE_EXPORTED")'''
                    raw, error = await call('execute_blender_code', {'code': code, 'user_prompt': 'Create a smoke-test cube, export assets/models/_smoke.glb, then remove the cube.'})
                    print('Blender export:', raw[:1600])
                    if not error and target.exists():
                        blob = target.read_bytes()
                        status.update({'glb_magic': blob[:4].decode('ascii', errors='replace'), 'bytes': len(blob),
                            'sha256': hashlib.sha256(blob).hexdigest(), 'passed': blob[:4] == b'glTF'})
                        target.unlink()
                        status['smoke_deleted'] = not target.exists()
            (OUTPUT / f'{kind}-status.json').write_text(json.dumps(status, indent=2) + '\n')
            print(json.dumps(status))
            return 0 if status['passed'] else 1

if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ('rfc', 'blender'):
        raise SystemExit('Usage: mcp_smoke.py rfc|blender')
    raise SystemExit(asyncio.run(main(sys.argv[1])))
