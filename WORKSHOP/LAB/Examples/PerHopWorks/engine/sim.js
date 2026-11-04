import {compileFactory} from './factory.js';
import {integer,splitOctet,dscpName} from './dsfield.js';
import {initialMachineState,processPacket} from './machines.js';
import {refillMeter} from './meters.js';
import {aqmArrival} from './aqm.js';
import {scheduleTick} from './scheduler.js';
const clone=value=>structuredClone(value);
export function runSimulation(level,graph,trace,submission={}){
  const events=[],snapshots=[],crates={},metrics={},errors=[];
  const failure=message=>({valid:false,complete:false,events,snapshots,crates,metrics,errors:[{message}],submission:clone(submission),graphValid:Boolean(graph?.valid)});
  if(!graph?.valid)return failure('Compile a valid factory before running.');
  if(!Array.isArray(trace))return failure('Arrival trace is missing.');
  const work=level.work_order,tickMs=work.tick_ms,begin=work.measurement_start_tick??0,end=work.measurement_end_tick??100,drain=work.max_drain_ticks??1000;
  try{integer(tickMs,1,1000,'tick duration');integer(begin,0,100000,'measurement start');integer(end,begin+1,100000,'measurement end');integer(drain,0,100000,'drain limit');const ids=new Set();
    for(const p of trace){if(!p.id||ids.has(p.id))throw new Error('Trace crate IDs must be unique.');ids.add(p.id);integer(p.tick,0,end-1,'arrival tick');integer(p.size,1,1000000000,'crate bytes');splitOctet(p.octet);if(!work.docks_in.some(d=>d.id===p.dock))throw new Error(`Unknown input dock: ${p.dock}`);if(!p.class)throw new Error('Every crate needs an immutable service class.');if(!work.docks_out.some(d=>d.bytes_per_tick>=p.size))throw new Error('A crate exceeds every output capacity.');}
  }catch(e){return failure(e.message);}
  const states=Object.fromEntries(Object.entries(graph.nodes).map(([id,m])=>[id,initialMachineState(m)])),inboxes=Object.fromEntries(graph.order.map(id=>[id,[]])),transit=[];
  const outEdge=(id,port)=>graph.edges.find(e=>e.from===id&&e.port===port);
  let tick=0;
  const event=(crate,machine,action,detail={})=>{const e={sequence:events.length,tick,crate:crate?.id??null,machine,action,...clone(detail)};events.push(e);return e;};
  const metric=cls=>metrics[cls]??=( {offered:0,offered_bytes:0,delivered:0,delivered_bytes:0,window_bytes:0,dropped:{policer:0,tail_drop:0,aqm:0,recycler:0},dropped_bytes:0,delay_values:[]});
  const terminal=(packet,machine,cause=null)=>{if(graph.nodes[machine]?.type==='dock_out')states[machine].processed++;if(packet.terminal){errors.push({message:`Duplicate terminal result for ${packet.id}`});return;}const m=metric(packet.class);packet.terminal={tick,machine,cause};delete packet.travel;packet.location=machine;
    if(cause){m.dropped[cause]++;m.dropped_bytes+=packet.size;event(packet,machine,'dropped',{cause});}
    else{m.delivered++;m.delivered_bytes+=packet.size;if(tick>=begin&&tick<end)m.window_bytes+=packet.size;m.delay_values.push(packet.queueDelay);event(packet,machine,'delivered',{octet:packet.octet,queueDelay:packet.queueDelay});}};
  const send=(packet,machine,port,extraDelay=0)=>{const edge=outEdge(machine.id,port);if(!edge){errors.push({message:`Missing output ${machine.id}:${port}`});return;}
    packet.location=machine.id;packet.travel={edge:edge.id,from:tick,until:tick+edge.length+extraDelay};transit.push({id:packet.id,edge:edge.id,to:edge.to,at:packet.travel.until});event(packet,machine.id,'departed',{port,edge:edge.id,to:edge.to});};
  for(tick=0;tick<end+drain;tick++){
    for(const [id,s]of Object.entries(states))if(s.meter)s.meter=refillMeter(s.meter,tick*tickMs);
    for(const arrival of trace.filter(p=>p.tick===tick)){
      const dock=work.docks_in.find(d=>d.id===arrival.dock),p={...clone(arrival),sourceDock:arrival.dock,originalOctet:arrival.octet,color:arrival.color??'green',trusted:dock.trusted,location:dock.id,queueDelay:0,policed:false,excess:false};crates[p.id]=p;const m=metric(p.class);m.offered++;m.offered_bytes+=p.size;inboxes[dock.id].push(p.id);event(p,dock.id,'arrived',{octet:p.octet,size:p.size});
    }
    // Arrival FIFO order is stable within the trace, then stable belt dispatch order.
    for(let i=0;i<transit.length;){const t=transit[i];if(t.at<=tick){const p=crates[t.id];p.location=t.to;delete p.travel;inboxes[t.to].push(t.id);transit.splice(i,1);}else i++;}
    const outputUsed={};
    for(const id of graph.order){const machine=graph.nodes[id];const arrivals=inboxes[id].splice(0);
      for(const crateId of arrivals){let p=crates[crateId];if(p.terminal)continue;
        if(machine.type==='recycler'){states[id].processed++;states[id].drops++;terminal(p,id,p.excess?'policer':'recycler');continue;}
        if(machine.type==='dock_out'){outputUsed[id]=(outputUsed[id]??0)+p.size;if(outputUsed[id]>machine.dock.bytes_per_tick){errors.push({message:`Output ${id} overloaded without explicit queuing.`});continue;}terminal(p,id);continue;}
        if(['buffer_belt','spillway'].includes(machine.type)){
          const s=states[id],edge=outEdge(id,'out');s.processed++;p.aqmCohort??=(machine.type==='spillway'?splitOctet(p.octet).dscp:null);
          if(machine.type==='spillway'){try{const r=aqmArrival(s.aqm,dscpName(splitOctet(p.octet).dscp),s.queue.length,machine.config.thresholds,machine.config.max_p);s.aqm=r.state;if(r.drop){s.drops++;terminal(p,id,'aqm');continue;}}catch(e){errors.push({message:e.message});continue;}}
          if(s.queue.length>=machine.config.capacity){s.drops++;terminal(p,id,'tail_drop');continue;}
          s.queue.push({id:p.id,entered:tick,ready:tick+edge.length});event(p,id,'queued',{depth:s.queue.length});continue;
        }
        if(machine.type==='priority_merger'){errors.push({message:'Merger received a crate outside an owned buffer queue.'});continue;}
        const r=processPacket(machine,states[id],p,tick*tickMs);states[id]=r.state;crates[p.id]=r.crate;p=crates[p.id];event(p,id,r.action,r.detail);send(p,machine,r.port,machine.type==='belt'?machine.config.length:0);
      }
    }
    // Explicit buffers retain ownership until the scheduler pulls their FIFO head.
    for(const id of graph.order){const machine=graph.nodes[id];if(machine.type!=='priority_merger')continue;
      const edge=outEdge(id,'out'),dock=graph.nodes[edge.to];if(dock.type!=='dock_out'){errors.push({message:'A Priority Merger must connect to an output dock.'});continue;}
      const inputs=graph.edges.filter(e=>e.to===id).map(e=>({id:e.from,input:e.input,priority:e.input===machine.config.priority,weight:machine.config.weights[e.input]??1,crates:states[e.from].queue.filter(q=>q.ready<=tick).map(q=>crates[q.id])}));
      try{const r=scheduleTick(states[id].scheduler??{},inputs,dock.dock.bytes_per_tick,machine.config.quantum);states[id].scheduler=r.state;
        for(const item of r.served){states[id].processed++;const field=inputs.find(x=>x.id===item.queue).priority?'servedPriority':'servedWeighted';states[id][field]=(states[id][field]??0)+1;const q=states[item.queue].queue.shift(),p=crates[q.id];p.queueDelay+=tick-q.ready;p.location=id;event(p,item.queue,'dequeued',{wait:tick-q.ready});event(p,id,'scheduled',{input:inputs.find(x=>x.id===item.queue).input,priority:inputs.find(x=>x.id===item.queue).priority});send(p,machine,'out');}
      }catch(e){errors.push({message:e.message});}
    }
    for(const id of graph.order){const machine=graph.nodes[id];if(!['buffer_belt','spillway'].includes(machine.type))continue;
      const edge=outEdge(id,'out'),target=graph.nodes[edge.to];if(target.type==='priority_merger')continue;
      if(target.type!=='dock_out'){if(states[id].queue.length)errors.push({message:'A Buffer Belt output must feed a merger or output dock.'});continue;}
      let capacity=target.dock.bytes_per_tick;while(states[id].queue.length){const q=states[id].queue[0],p=crates[q.id];if(q.ready>tick||p.size>capacity)break;states[id].queue.shift();capacity-=p.size;p.queueDelay+=tick-q.ready;event(p,id,'dequeued',{wait:tick-q.ready});terminal(p,target.id);}
    }
    snapshots.push({tick,crates:Object.values(crates).filter(p=>!p.terminal).map(p=>({id:p.id,octet:p.octet,color:p.color,size:p.size,class:p.class,location:p.location,travel:clone(p.travel??null)})),machines:Object.fromEntries(Object.entries(states).map(([id,s])=>[id,{processed:s.processed,servedPriority:s.servedPriority??0,servedWeighted:s.servedWeighted??0,queue:s.queue.length,drops:s.drops,tokens:s.meter?{committed:s.meter.committed,excess:s.meter.excess,peak:s.meter.peak,cbs:s.meter.cbs,ebs:s.meter.ebs,pbs:s.meter.pbs}:null}])),metrics:clone(metrics)});
    if(errors.length)break;
    if(tick>=Math.max(0,...trace.map(p=>p.tick))&&Object.values(crates).every(p=>p.terminal)&&Object.keys(crates).length===trace.length)break;
  }
  for(const m of Object.values(metrics)){const values=m.delay_values; m.loss_percent=m.offered?100*(m.offered-m.delivered)/m.offered:0;m.delay={min:values.length?Math.min(...values):null,avg:values.length?values.reduce((a,b)=>a+b,0)/values.length:null,max:values.length?Math.max(...values):null};delete m.delay_values;}
  const complete=errors.length===0&&Object.keys(crates).length===trace.length&&Object.values(crates).every(p=>p.terminal);
  return {valid:errors.length===0,graphValid:true,complete,events,snapshots,crates,metrics,errors,ticks:snapshots.length,submission:clone(submission),offered:trace.length,measurement:{start:begin,end}};
}

// Both parts are simulated independently. A player's build cannot change the prediction exercise.
export function runWorkOrder(level,graph,trace,submission,definitions){const result=runSimulation(level,graph,trace,submission);if(level.prediction_factory){const compiled=compileFactory(level,level.prediction_factory,definitions);result.prediction_result=runSimulation(level,compiled.graph,trace,submission);if(!compiled.valid||!result.prediction_result.valid){result.valid=false;result.errors.push({message:'The fixed prediction exercise is invalid.'});}}return result;}
