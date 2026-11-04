import {readFileSync} from 'node:fs';
export const definitions=JSON.parse(readFileSync(new URL('../data/machines.json',import.meta.url)));
export const level={id:'TEST',profile:'rfc4594',work_order:{tick_ms:1,grid:{width:16,height:8},docks_in:[{id:'in',x:0,y:2,trusted:false}],docks_out:[{id:'out',x:8,y:2,bytes_per_tick:1500}],locked:['in','out'],palette:{belt:100,paint_booth:2,sorter:1,recycler:1,buffer_belt:2,tank_single:1,priority_merger:1,spillway:1},bounds:{},measurement_start_tick:0,measurement_end_tick:30,max_drain_ticks:100},checks:[{id:'VALID'},{id:'CONSERVATION'}]};
export const machine=(id,type,x,y,config={})=>({id,type,x,y,rotation:0,config});
export const layout={machines:[machine('in','dock_in',0,2),machine('paint','paint_booth',4,2,{dscp:46}),machine('out','dock_out',8,2)],links:[{from:'in',port:'out',to:'paint',input:'in'},{from:'paint',port:'out',to:'out',input:'in'}]};
export const trace=[{id:'c1',tick:0,dock:'in',size:1000,octet:1,class:'telephony',label:{application:'voip'}},{id:'c2',tick:1,dock:'in',size:500,octet:0,class:'telephony',label:{application:'voip'}}];
