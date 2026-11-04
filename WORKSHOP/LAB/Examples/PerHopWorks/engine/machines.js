import {splitOctet,precedence,markOctet} from './dsfield.js';
import {createMeter,meterPacket} from './meters.js';
export function sorterPort(machine,crate){const dscp=splitOctet(crate.octet).dscp;for(const [i,rule] of (machine.config.rules??[]).entries()){let value;if(machine.config.mode==='ba')value=dscp;else if(machine.config.mode==='precedence')value=precedence(dscp);else value=rule.field==='sourceDock'?crate.sourceDock:rule.field==='class'?crate.class:crate.label?.[rule.field??'application'];if(value===rule.value)return {port:rule.port,rule:i+1};}return {port:'default',rule:null};}
export function initialMachineState(machine){const state={processed:0,queue:[],aqm:{},drops:0};if(machine.type.startsWith('tank_'))state.meter=createMeter({tank_single:'single',tank_cascade:'srtcm',tank_twin:'trtcm'}[machine.type],machine.config);return state;}
export function processPacket(machine,state,crate,ms){
  const s={...state,processed:state.processed+1};let packet={...crate},port='out',action='processed',detail={};
  if(machine.type==='sorter'){const match=sorterPort(machine,packet);port=match.port;action='sorted';detail={rule:match.rule,mode:machine.config.mode};}
  if(machine.type==='paint_booth'){const before=packet.octet;packet.octet=markOctet(before,machine.config.dscp);packet.lastMarker=machine.id;action='marked';detail={before,after:packet.octet};}
  if(machine.type.startsWith('tank_')){const r=meterPacket(s.meter,packet.size,ms,packet.color??'green');s.meter=r.state;packet.color=r.color;action='metered';port=machine.type==='tank_single'?(r.conform?'conform':'exceed'):r.color;detail={color:r.color,tokens:{committed:r.state.committed,excess:r.state.excess,peak:r.state.peak}};packet.lastMeter=machine.id;if(machine.type==='tank_single'){packet.policed=r.conform;packet.excess=!r.conform;}}
  return {state:s,crate:packet,port,action,detail};
}
