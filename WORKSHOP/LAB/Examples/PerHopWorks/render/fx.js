const reduced=()=>matchMedia('(prefers-reduced-motion: reduce)').matches;
export function updateMachineEffects(root,machine,snapshot,previous,tick){const state=snapshot?.machines[machine.id];if(!state)return;const active=state.processed>(previous?.machines[machine.id]?.processed??0),motion=reduced()?0:Math.sin(tick*.6);
 const node=name=>root.getObjectByName(name);const water=(name,value,capacity)=>{const o=node(name);if(o)o.scale.y=Math.max(.015,Math.min(1,(value??0)/Math.max(1,capacity??1)));};
 if(state.tokens){const t=state.tokens;water('water',t.committed,t.cbs);water('water_committed',t.committed,t.cbs);water('water_excess',t.excess,t.ebs);water('water_peak',t.peak,t.pbs);const spout=node('overflow_spout');if(spout)spout.visible=t.committed>=t.cbs&&t.excess<t.ebs;}
 for(const name of ['flap','gate_priority','gate_weighted','hatch']){const o=node(name);if(o){const rest=o.userData.restRotation??=o.rotation.clone();o.rotation.copy(rest);const field=name==='gate_priority'?'servedPriority':name==='gate_weighted'?'servedWeighted':null;const moved=field?state[field]>(previous?.machines[machine.id]?.[field]??0):active;o.rotateY(moved?.3+motion*.15:0);}}
 const door=node('door');if(door){door.userData.restY??=door.position.y;door.position.y=door.userData.restY+(active?.3:0);}
 const spray=node('spray');if(spray)spray.visible=active&&!reduced();const nozzle=node('nozzle');if(nozzle){nozzle.userData.restY??=nozzle.position.y;nozzle.position.y=nozzle.userData.restY+(active?motion*.015:0);}
 const fill=node('fill_marker');if(fill)fill.scale.y=Math.max(.05,state.queue/Math.max(1,machine.config.capacity));
 const values=Object.values(machine.config.thresholds??{});for(const [name,index] of [['threshold_min',0],['threshold_max',1]]){const o=node(name);if(o&&values.length)o.position.x=-.4+.8*Math.max(...values.map(v=>v[index]))/machine.config.capacity;}
}
export {reduced as reducedMotion};
