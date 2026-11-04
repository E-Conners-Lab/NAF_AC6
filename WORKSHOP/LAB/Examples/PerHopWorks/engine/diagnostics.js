import {splitOctet,joinOctet,dscpName} from './dsfield.js';
import {sorterPort} from './machines.js';
export function analyzePaths(graph,level){
  if(!graph?.valid)return [];
  const fields={};for(const m of Object.values(graph.nodes))if(m.type==='sorter'&&m.config.mode==='mf')for(const r of m.config.rules??[]){const field=r.field??'application';if(!['sourceDock','class'].includes(field)){fields[field]??=new Set(['__other__']);fields[field].add(r.value);}}
  let labels=[{}];for(const [field,values]of Object.entries(fields))labels=labels.flatMap(label=>[...values].map(value=>({...label,[field]:value})));
  const classValues=new Set(['__other__']);for(const m of Object.values(graph.nodes))for(const r of m.config?.rules??[])if(r.field==='class')classValues.add(r.value);
  const records=[],dedupe=new Set();
  for(const dock of level.work_order.docks_in)for(let dscp=0;dscp<64;dscp++)for(const label of labels)for(const cls of classValues){
    const queue=[{node:dock.id,octet:joinOctet(dscp,0),policed:false,excess:false,path:[],label,class:cls,input:null}];
    for(let i=0;i<queue.length;i++){const s=queue[i],m=graph.nodes[s.node];if(!m)continue;const current=splitOctet(s.octet).dscp,key=[dock.id,m.id,dscp,current,s.policed,s.excess,s.input].join('|');
      if(!dedupe.has(key)){records.push({machine:m.id,dscp:current,originalDscp:dscp,sourceDock:dock.id,trusted:dock.trusted,policed:s.policed,excess:s.excess,input:s.input,path:[...s.path,m.id]});dedupe.add(key);}
      let branches=[{port:'out',octet:s.octet,policed:s.policed,excess:s.excess}];
      if(m.type==='sorter')branches=[{...branches[0],port:sorterPort(m,{...s,sourceDock:dock.id}).port}];
      if(m.type==='paint_booth')branches[0].octet=joinOctet(m.config.dscp,0);
      if(m.type==='tank_single')branches=[{...branches[0],port:'conform',policed:true,excess:false},{...branches[0],port:'exceed',policed:false,excess:true}];
      if(['tank_cascade','tank_twin'].includes(m.type))branches=['green','yellow','red'].map(port=>({...branches[0],port}));
      for(const branch of branches){const edge=graph.edges.find(e=>e.from===m.id&&e.port===branch.port);if(edge)queue.push({...s,...branch,node:edge.to,input:edge.input,path:[...s.path,m.id]});}
    }
  }
  return records;
}
export function detectStatic(graph,level,paths=analyzePaths(graph,level)){
  const found=[];for(const p of paths){const m=graph.nodes[p.machine];let id=null;
    if(m.type==='spillway'&&[46,40,32,24].includes(p.dscp))id='aqm-on-ef';
    if(m.type==='priority_merger'&&p.input===m.config.priority&&p.dscp===46&&!p.policed)id='unpoliced-priority';
    if(m.type==='dock_out'&&!p.trusted&&[48,56].includes(p.originalDscp)&&[48,56].includes(p.dscp))id='untrusted-mark';
    if(id&&!found.some(x=>x.id===id&&x.machine===m.id))found.push({id,machine:m.id,path:p.path});
  }return found;
}
export function detectMeasured(result){const found=[];for(const [cls,m]of Object.entries(result.metrics??{}))if(m.offered>0&&m.delivered===0)found.push({id:'class-starved',class:cls});for(const group of ['AF1','AF2','AF3','AF4']){const packets=Object.values(result.crates??{}),cohorts=[1,2,3].map(n=>packets.filter(p=>dscpName(p.aqmCohort??splitOctet(p.originalOctet).dscp)===group+n)),loss=cohorts.map(ps=>({offered:ps.length,dropped:ps.filter(p=>p.terminal?.cause).length}));if(loss.every(x=>x.offered>0)&&loss.slice(1).some((x,i)=>loss[i].dropped*x.offered>x.dropped*loss[i].offered))found.push({id:'loss-order-inverted',class:group,loss});}return found;}
