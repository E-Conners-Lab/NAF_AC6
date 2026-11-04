import {integer} from './dsfield.js';
const MAX=1_000_000_000;
export function createMeter(kind,config={}){
  if(!['single','srtcm','trtcm'].includes(kind))throw new RangeError('Unknown meter');
  const mode=config.mode??'blind';if(!['blind','aware'].includes(mode))throw new RangeError('Invalid meter mode');
  const cir=integer(kind==='single'?config.rate:config.cir,0,MAX,'rate');
  const cbs=integer(kind==='single'?config.burst:config.cbs,kind==='srtcm'?0:1,MAX,'committed burst');
  const ebs=kind==='srtcm'?integer(config.ebs,0,MAX,'excess burst'):0;
  if(kind==='srtcm'&&cbs+ebs===0)throw new RangeError('At least one srTCM bucket must be positive');
  const pir=kind==='trtcm'?integer(config.pir,cir,MAX,'peak rate'):0;
  const pbs=kind==='trtcm'?integer(config.pbs,1,MAX,'peak burst'):0;
  return {kind,mode,cir,cbs,ebs,pir,pbs,committed:cbs,excess:ebs,peak:pbs,committedRemainder:0,peakRemainder:0,lastMs:0};
}
export function refillMeter(state,ms){
  integer(ms,state.lastMs,Number.MAX_SAFE_INTEGER,'time');const s={...state},dt=ms-state.lastMs;
  const credit=s.cir*dt+s.committedRemainder;integer(credit,0,Number.MAX_SAFE_INTEGER,'token credit');
  const tokens=Math.floor(credit/1000);s.committedRemainder=credit%1000;
  const add=Math.min(s.cbs-s.committed,tokens);s.committed+=add;
  if(s.kind==='srtcm')s.excess=Math.min(s.ebs,s.excess+tokens-add);
  if(s.kind==='trtcm'){const peakCredit=s.pir*dt+s.peakRemainder;integer(peakCredit,0,Number.MAX_SAFE_INTEGER,'peak credit');s.peak=Math.min(s.pbs,s.peak+Math.floor(peakCredit/1000));s.peakRemainder=peakCredit%1000;}
  s.lastMs=ms;return s;
}
export function meterPacket(state,size,ms,inputColor='green'){
  integer(size,1,MAX,'packet bytes');if(!['green','yellow','red'].includes(inputColor))throw new RangeError('Invalid meter color');
  const s=refillMeter(state,ms),pre=s.mode==='aware'?inputColor:'green';let color='red';
  if(s.kind==='trtcm'){
    if(pre!=='red'&&s.peak>=size){s.peak-=size;if(pre==='yellow'||s.committed<size)color='yellow';else{color='green';s.committed-=size;}}
  }else if(pre==='green'&&s.committed>=size){color='green';s.committed-=size;}
  else if(s.kind==='srtcm'&&pre!=='red'&&s.excess>=size){color='yellow';s.excess-=size;}
  return {state:s,color,conform:color==='green'};
}
