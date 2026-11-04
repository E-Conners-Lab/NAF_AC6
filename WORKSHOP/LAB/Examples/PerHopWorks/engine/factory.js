import {createMeter} from './meters.js';
export function machineOutputs(machine,definition){return machine.type==='sorter'?['default',...new Set((Array.isArray(machine.config.rules)?machine.config.rules:[]).map(r=>r.port))]:definition.outputs;}
export function routePath(from,to,blocked,width,height){
  const key=(x,y)=>`${x},${y}`,start=key(from.x,from.y),goal=key(to.x,to.y),queue=[[from.x,from.y]],seen=new Set([start]),previous=new Map();
  for(let i=0;i<queue.length;i++){const [x,y]=queue[i];if(key(x,y)===goal){const path=[];let at=goal;while(at){path.push(at.split(',').map(Number));at=previous.get(at);}return path.reverse();}
    for(const [dx,dy] of [[1,0],[0,1],[0,-1],[-1,0]]){const nx=x+dx,ny=y+dy,k=key(nx,ny);if(nx<0||ny<0||nx>=width||ny>=height||seen.has(k)||(blocked.has(k)&&k!==goal))continue;seen.add(k);previous.set(k,key(x,y));queue.push([nx,ny]);}}
  return null;
}
export function portDirection(machine,input=false){const directions=[[1,0],[0,1],[-1,0],[0,-1]],index=((machine.rotation??0)/90+(input?2:0))%4;return directions[index];}
export function routePorts(from,to,blocked,width,height){const [dx,dy]=portDirection(from),[ix,iy]=portDirection(to,true),start={x:from.x+dx,y:from.y+dy},end={x:to.x+ix,y:to.y+iy};if(start.x===to.x&&start.y===to.y&&end.x===from.x&&end.y===from.y)return [[from.x,from.y],[to.x,to.y]];for(const p of [start,end])if(p.x<0||p.y<0||p.x>=width||p.y>=height||blocked.has(`${p.x},${p.y}`))return null;const path=routePath(start,end,blocked,width,height);return path?[[from.x,from.y],...path,[to.x,to.y]]:null;}
function compile(level,layout,definitions){
  const errors=[],error=(code,machine,message,port=null)=>errors.push({code,machine,port,message});
  if(!layout||!Array.isArray(layout.machines)||!Array.isArray(layout.links))return {valid:false,graph:null,errors:[{code:'layout',message:'Factory layout is missing.'}]};
  const defs=Object.fromEntries(definitions.map(d=>[d.id,d])),nodes={},counts={},grid=level.work_order.grid??{width:32,height:20},positions=new Set();
  for(const raw of layout.machines){const def=defs[raw.type];if(!def){error('type',raw.id,'Unknown machine type.');continue;}
    if(!raw.id||nodes[raw.id]){error('id',raw.id,'Machine IDs must be unique.');continue;}
    const config=Object.fromEntries(def.fields.map(f=>[f.name,structuredClone(f.default)]));Object.assign(config,structuredClone(raw.config??{}));const m={...structuredClone(raw),rotation:raw.rotation??0,config};nodes[m.id]=m;counts[m.type]=(counts[m.type]??0)+1;
    if(!Number.isInteger(m.x)||!Number.isInteger(m.y)||m.x<0||m.y<0||m.x>=grid.width||m.y>=grid.height)error('bounds',m.id,'Machine is outside the floor.');
    if(![0,90,180,270].includes(m.rotation))error('rotation',m.id,'Rotation must be a quarter turn.');
    const position=`${m.x},${m.y}`;if(positions.has(position))error('overlap',m.id,'Two machines occupy this tile.');positions.add(position);
    for(const field of def.fields){const value=config[field.name];if(['integer','number'].includes(field.type)&&(!Number.isFinite(value)||(field.type==='integer'&&!Number.isSafeInteger(value))||value<field.min||value>field.max))error('config',m.id,`${field.label} is out of range.`);if(field.type==='enum'&&!field.options.includes(value))error('config',m.id,`${field.label} is invalid.`);}
    if(m.type==='sorter'){if(!Array.isArray(config.rules))error('config',m.id,'Rules must be an ordered list.');else for(const r of config.rules){if(!r.port||r.port==='default')error('config',m.id,'Each rule needs a named output.');if(config.mode==='ba'&&(!Number.isInteger(r.value)||r.value<0||r.value>63))error('config',m.id,'BA rules need a DSCP integer 0–63.');if(config.mode==='precedence'&&(!Number.isInteger(r.value)||r.value<0||r.value>7))error('config',m.id,'Precedence rules need an integer 0–7.');}}
    try{if(m.type.startsWith('tank_'))createMeter({tank_single:'single',tank_cascade:'srtcm',tank_twin:'trtcm'}[m.type],config);}catch(e){error('config',m.id,e.message);}
    if(m.type==='spillway'&&(!config.thresholds||typeof config.thresholds!=='object'))error('config',m.id,'AQM thresholds are missing.');
  }
  for(const dock of [...level.work_order.docks_in,...level.work_order.docks_out]){const m=nodes[dock.id];const type=level.work_order.docks_in.includes(dock)?'dock_in':'dock_out';if(!m||m.type!==type||m.x!==dock.x||m.y!==dock.y||m.rotation!==(dock.rotation??0))error('locked',dock.id,'This dock is locked to its work-order position.');if(m)m.dock=structuredClone(dock);}
  for(const m of Object.values(nodes))if(m.type.startsWith('dock_')&&!m.dock)error('dock',m.id,'Extra docks are not allowed.');
  for(const id of level.work_order.locked??[]){const expected=level.fixed_factory?.machines.find(m=>m.id===id);if(expected&&JSON.stringify(nodes[id]?.config)!==JSON.stringify(expected.config))error('locked',id,'This prediction factory configuration is locked.');}
  if(level.type==='predict'&&level.fixed_factory){const canonical=x=>JSON.stringify({machines:x.machines,links:x.links});if(canonical(layout)!==canonical(level.fixed_factory))error('locked',null,'The prediction factory layout and connections are fixed.');}
  const edges=[],used=new Set(),usedInputs=new Set();let beltCount=counts.belt??0;
  for(const [i,raw] of layout.links.entries()){
    const from=nodes[raw.from],to=nodes[raw.to];if(!from||!to){error('connection',raw.from,'A connection references a missing machine.');continue;}
    if(!machineOutputs(from,defs[from.type]).includes(raw.port))error('port',from.id,'Unknown output port.',raw.port);
    const portKey=`${from.id}:${raw.port}`;if(used.has(portKey))error('duplicate-output',from.id,'An output cannot split without a sorter.',raw.port);used.add(portKey);
    const input=raw.input??'in',inputNames=defs[to.type].dynamic_inputs?[to.config.priority,...Object.keys(to.config.weights)]:defs[to.type].inputs;if(!inputNames.includes(input))error('input',to.id,'Unknown input port.',input);const inputKey=`${to.id}:${input}`;if(usedInputs.has(inputKey))error('duplicate-input',to.id,'Each input accepts one belt. Combine traffic through a merger.',input);usedInputs.add(inputKey);
    if(to.type==='priority_merger'&&!['buffer_belt','spillway'].includes(from.type))error('queue',to.id,'Each merger input needs an explicit Buffer Belt or Spillway queue.');
    const path=raw.path??routePorts(from,to,positions,grid.width,grid.height);
    if(!path||path.length<2||path[0][0]!==from.x||path[0][1]!==from.y||path.at(-1)[0]!==to.x||path.at(-1)[1]!==to.y){error('path',from.id,'No continuous belt path reaches the target.');continue;}
    const [dx,dy]=portDirection(from),[ix,iy]=portDirection(to,true);if(path[1][0]-from.x!==dx||path[1][1]-from.y!==dy||path.at(-2)[0]-to.x!==ix||path.at(-2)[1]-to.y!==iy)error('port-direction',from.id,'The belt must meet the rotated output and input sides.');
    for(let j=1;j<path.length;j++){const [x,y]=path[j],[px,py]=path[j-1];if(!Number.isInteger(x)||!Number.isInteger(y)||Math.abs(x-px)+Math.abs(y-py)!==1||x<0||y<0||x>=grid.width||y>=grid.height||(j<path.length-1&&positions.has(`${x},${y}`)))error('path',from.id,'Belt paths must use adjacent free grid tiles.');}
    const edge={...structuredClone(raw),id:raw.id??`edge-${i}`,input:raw.input??'in',path,length:path.length-1};edges.push(edge);beltCount+=edge.length;
  }
  for(const m of Object.values(nodes))for(const port of machineOutputs(m,defs[m.type]))if(!used.has(`${m.id}:${port}`))error('unconnected',m.id,'Connect this output before running.',port);
  counts.belt=beltCount;for(const [type,count]of Object.entries(counts)){if(type.startsWith('dock_'))continue;const allowance=level.work_order.palette[type]??0;if(count>allowance)error('palette',null,`${type}: ${count} used, ${allowance} available.`);}
  const degree=Object.fromEntries(Object.keys(nodes).map(id=>[id,0]));for(const e of edges)degree[e.to]++;
  const ready=Object.keys(degree).filter(id=>degree[id]===0).sort(),order=[];while(ready.length){const id=ready.shift();order.push(id);for(const e of edges.filter(e=>e.from===id)){if(--degree[e.to]===0){ready.push(e.to);ready.sort();}}}
  if(order.length!==Object.keys(nodes).length)error('cycle',null,'The factory contains a cycle.');
  const graph={nodes,edges,order,grid,counts,valid:errors.length===0};return {valid:graph.valid,graph,errors};
}

export function compileFactory(level,layout,definitions){try{return compile(level,layout,definitions);}catch(error){return {valid:false,graph:null,errors:[{code:"invalid-data",machine:null,port:null,message:error.message}]};}}
