export function integer(value, min, max, label='value') {
  if(!Number.isSafeInteger(value)||value<min||value>max) throw new RangeError(`${label} must be an integer from ${min} to ${max}`);
  return value;
}
export function splitOctet(octet){integer(octet,0,255,'DS field');return {dscp:octet>>>2,ecn:octet&3};}
export function joinOctet(dscp,ecn){integer(dscp,0,63,'DSCP');integer(ecn,0,3,'ECN');return dscp*4+ecn;}
export function markOctet(octet,dscp){return joinOctet(dscp,splitOctet(octet).ecn);}
export function precedence(dscp){return integer(dscp,0,63,'DSCP')>>>3;}
export function nameToDscp(name){
  if(name==='EF')return 46;if(name==='DF')return 0;
  let m=/^CS([0-7])$/.exec(name);if(m)return Number(m[1])*8;
  m=/^AF([1-4])([1-3])$/.exec(name);if(m)return Number(m[1])*8+Number(m[2])*2;
  throw new RangeError(`Unknown supported codepoint name: ${name}`);
}
export function dscpName(dscp){integer(dscp,0,63,'DSCP');if(dscp===0)return 'DF';if(dscp===46)return 'EF';if(dscp%8===0)return `CS${dscp/8}`;const x=dscp>>3,y=(dscp%8)/2;if(x>=1&&x<=4&&Number.isInteger(y)&&y>=1&&y<=3)return `AF${x}${y}`;return `DSCP ${dscp}`;}
export function bits(octet){return integer(octet,0,255,'DS field').toString(2).padStart(8,'0');}
