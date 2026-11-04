"""Fetch live RFCs through the repaired upstream MCP and preserve every call."""
import asyncio, hashlib, json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
ROOT=Path(__file__).resolve().parents[1]
NUMBERS=[2474,2475,2597,2697,2698,3168,3246,3260,3290,4594,2598,5865,8622]
async def main():
    out=ROOT/'research/rfc';out.mkdir(parents=True,exist_ok=True)
    records=[]
    params=StdioServerParameters(command='node',args=[str(ROOT/'tools/rfc-mcp/compat.mjs')])
    async with stdio_client(params) as (read,write):
        async with ClientSession(read,write) as client:
            await client.initialize()
            for number in NUMBERS:
                result=await client.call_tool('get_rfc',{'number':str(number),'format':'full'})
                raw='\n'.join(getattr(x,'text','') for x in result.content)
                if getattr(result,'is_error',False): raise RuntimeError(raw)
                doc=json.loads(raw)
                if not doc['fullText'] or not doc['sections']: raise RuntimeError(f'RFC {number} has no content/sections')
                filename=f'rfc{number}-mcp.json';(out/filename).write_text(raw+'\n')
                with urlopen(f'https://www.rfc-editor.org/rfc/rfc{number}.txt',timeout=30) as response: plain=response.read()
                (out/f'rfc{number}.txt').write_bytes(plain)
                vid=f'V-{len(records)+1:04}'
                records.append({'id':vid,'timestamp':datetime.now(timezone.utc).isoformat(),'tool':'get_rfc','args':{'number':str(number),'format':'full'},'server':'@mjpitz/mcp-rfc@0.2504.4 + perhop-html-anchors-v1','artifact':f'rfc/{filename}','sha256':hashlib.sha256((raw+'\n').encode()).hexdigest(),'sections':len(doc['sections'])})
                (ROOT/'research/verification-calls.json').write_text(json.dumps(records,indent=2)+'\n')
                print(number,vid,doc['metadata']['title'],len(doc['sections']),flush=True)
    ledger='# RFC MCP verification ledger\n\nEvery row is a real live MCP call. Full returned text is preserved for claim review.\nRetrieval alone does not certify a claim; facts reference a record only after inspecting its text.\nBootstrap get_rfc/get_rfc_section calls, including failures, are separately retained in\n`tool-results/rfc-upstream-failure.json` and `tool-results/rfc-smoke.json`.\n\n| ID | Time UTC | Tool and arguments | Artifact | SHA-256 |\n|---|---|---|---|---|\n'
    for r in records: ledger+=f"| {r['id']} | {r['timestamp']} | {r['tool']} {json.dumps(r['args'])} | [{r['artifact']}]({r['artifact']}) | {r['sha256']} |\n"
    (ROOT/'research/VERIFICATION.md').write_text(ledger)
asyncio.run(main())
