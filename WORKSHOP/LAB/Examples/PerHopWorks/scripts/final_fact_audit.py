"""Append a live MCP retrieval audit without replacing the original evidence."""
import asyncio,hashlib,json,re
from datetime import datetime,timezone
from pathlib import Path
from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client
ROOT=Path(__file__).resolve().parents[1]
async def main():
    records=json.loads((ROOT/'research/verification-calls.json').read_text());out=ROOT/'research/rfc/final';out.mkdir(exist_ok=True)
    params=StdioServerParameters(command='node',args=[str(ROOT/'tools/rfc-mcp/compat.mjs')]);by_number={}
    async with stdio_client(params) as (read,write):
        async with ClientSession(read,write) as client:
            await client.initialize()
            for n in [2474,2475,2597,2697,2698,3168,3246,3260,3290,4594,2598,5865,8622]:
                args={'number':str(n),'format':'full'};result=await client.call_tool('get_rfc',args)
                raw='\n'.join(getattr(x,'text','') for x in result.content)+'\n'
                if getattr(result,'is_error',False):raise RuntimeError(raw)
                doc=json.loads(raw)
                if not doc.get('fullText') or not doc.get('sections'):raise RuntimeError(f'Empty RFC {n}')
                path=out/f'rfc{n}-mcp.json';path.write_text(raw)
                rec={'id':f'V-{len(records)+1:04}','timestamp':datetime.now(timezone.utc).isoformat(),'tool':'get_rfc','args':args,'server':'@mjpitz/mcp-rfc@0.2504.4 + perhop-html-anchors-v1','artifact':str(path.relative_to(ROOT/'research')),'sha256':hashlib.sha256(raw.encode()).hexdigest(),'sections':len(doc['sections']),'purpose':'Loop 5 final fact audit'};records.append(rec);by_number[n]=rec
                (ROOT/'research/verification-calls.json').write_text(json.dumps(records,indent=2)+'\n')
                with (ROOT/'research/VERIFICATION.md').open('a') as f:f.write(f"| {rec['id']} | {rec['timestamp']} | get_rfc {json.dumps(args)} (final audit) | [{rec['artifact']}]({rec['artifact']}) | {rec['sha256']} |\n")
                print(n,rec['id'],doc['metadata']['title'],flush=True)
    (ROOT/'research/final-audit-index.json').write_text(json.dumps(by_number,indent=2)+'\n')
asyncio.run(main())
