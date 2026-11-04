import {integer} from './dsfield.js';
export function scheduleTick(previous,inputs,capacity,quantum=1500){
  integer(capacity,1,1_000_000_000,'output capacity');integer(quantum,1,1_000_000,'quantum');
  if(inputs.filter(q=>q.priority).length>1)throw new RangeError('Only one priority input is allowed');
  const queues=inputs.map(q=>({...q,crates:[...q.crates]})),state={deficits:{...(previous.deficits??{})},cursor:previous.cursor??0,active:previous.active??null},served=[];let remaining=capacity;
  for(const q of queues){if(!q.priority)integer(q.weight??1,1,1000,'weight');for(const p of q.crates)integer(p.size,1,capacity,'packet size');}
  const take=q=>{const crate=q.crates.shift();remaining-=crate.size;served.push({queue:q.id,crate});};
  const priority=queues.find(q=>q.priority);if(priority){while(priority.crates.length&&priority.crates[0].size<=remaining)take(priority);if(priority.crates.length)return {state,queues,served,unused:remaining};}
  const weighted=queues.filter(q=>!q.priority);if(!weighted.length)return {state,queues,served,unused:remaining};
  state.cursor%=weighted.length;
  // Deficits grow during complete rounds, so bound scans by total capacity/quantum and queue count.
  const bound=(Math.ceil(capacity/quantum)+2)*weighted.length+inputs.reduce((n,q)=>n+q.crates.length,0)*weighted.length;
  let scans=0;
  while(remaining>0&&weighted.some(q=>q.crates.length)&&scans++<bound){
    const q=weighted[state.cursor];state.deficits[q.id]??=0;
    if(!q.crates.length){state.deficits[q.id]=0;state.active=null;state.cursor=(state.cursor+1)%weighted.length;continue;}
    if(state.active!==q.id){state.deficits[q.id]+=quantum*(q.weight??1);state.active=q.id;}
    if(q.crates[0].size>state.deficits[q.id]){state.active=null;state.cursor=(state.cursor+1)%weighted.length;continue;}
    if(q.crates[0].size>remaining)break;
    const size=q.crates[0].size;take(q);state.deficits[q.id]-=size;
    if(!q.crates.length){state.deficits[q.id]=0;state.active=null;state.cursor=(state.cursor+1)%weighted.length;}
    else if(q.crates[0].size>state.deficits[q.id]){state.active=null;state.cursor=(state.cursor+1)%weighted.length;}
  }
  return {state,queues,served,unused:remaining};
}
