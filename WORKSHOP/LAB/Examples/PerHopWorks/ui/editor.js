import {machineOutputs} from '../engine/factory.js';
export function createEditor(level,initial,definitions,onChange){
  let layout=structuredClone(initial),history=[],selected=null,tool=null;const cursor={x:1,y:1};const defs=Object.fromEntries(definitions.map(d=>[d.id,d]));
  const locked=id=>level.type==='predict'||level.work_order.locked.includes(id);
  function edit(action){history.push(structuredClone(layout));action();onChange();}
  const api={cursor,get layout(){return layout;},get selected(){return selected;},get tool(){return tool;},locked,connectionsLocked:()=>level.type==='predict',
    select(id){selected=id;const m=layout.machines.find(m=>m.id===id);if(m){cursor.x=m.x;cursor.y=m.y;}onChange({selectionOnly:true});},
    setTool(type){tool=type;onChange({toolOnly:true});},
    place(){const occupied=layout.machines.find(m=>m.x===cursor.x&&m.y===cursor.y);if(occupied){api.select(occupied.id);return;}if(level.type==='predict'||!tool)return;const def=defs[tool];if(!def)return;edit(()=>{let n=1;while(layout.machines.some(m=>m.id===tool+n))n++;selected=tool+n;layout.machines.push({id:selected,type:tool,x:cursor.x,y:cursor.y,rotation:0,config:Object.fromEntries(def.fields.map(f=>[f.name,structuredClone(f.default)]))});});},
    remove(){if(!selected||locked(selected))return;edit(()=>{layout.machines=layout.machines.filter(m=>m.id!==selected);layout.links=layout.links.filter(e=>e.from!==selected&&e.to!==selected);selected=null;});},
    rotate(){if(!selected||locked(selected))return;edit(()=>{const m=layout.machines.find(m=>m.id===selected);m.rotation=(m.rotation+90)%360;});},
    update(id,config){if(locked(id))return;edit(()=>{layout.machines.find(m=>m.id===id).config=structuredClone(config);});},
    connect(from,port,to,input='in'){if(level.type==='predict')return;edit(()=>{layout.links=layout.links.filter(e=>!(e.from===from&&e.port===port));if(to)layout.links.push({from,port,to,input});});},
    undo(){if(!history.length)return;layout=history.pop();onChange();},
    key(event){if(event.target.closest('input,select,textarea'))return;let handled=true;const grid=level.work_order.grid;if(event.key==='ArrowRight')cursor.x=Math.min(grid.width-1,cursor.x+1);else if(event.key==='ArrowLeft')cursor.x=Math.max(0,cursor.x-1);else if(event.key==='ArrowDown')cursor.y=Math.min(grid.height-1,cursor.y+1);else if(event.key==='ArrowUp')cursor.y=Math.max(0,cursor.y-1);else if(event.key==='Enter'){api.place();}else if(event.key.toLowerCase()==='r'){api.rotate();}else if(['Delete','Backspace'].includes(event.key)){api.remove();}else if(event.key.toLowerCase()==='z'&&(event.ctrlKey||event.metaKey)){api.undo();}else handled=false;if(handled){event.preventDefault();onChange({cursorOnly:true});}}
  };return api;
}
