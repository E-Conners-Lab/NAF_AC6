export function validateThresholds(thresholds,capacity,group='AF4'){
  const errors=[];for(const suffix of [3,2,1]){const name=group+suffix,v=thresholds?.[name];if(!Array.isArray(v)||v.length!==2||!v.every(Number.isSafeInteger)||v[0]<0||v[0]>=v[1]||v[1]>capacity)errors.push({rule:`0 <= min ${name} < max ${name} <= capacity`,actual:v??null});}
  for(const [left,right] of [[3,2],[2,1]]){const a=thresholds?.[group+left],b=thresholds?.[group+right];if(a&&b&&a[1]>b[0])errors.push({rule:`max ${group+left} <= min ${group+right}`,actual:[a[1],b[0]]});}
  return errors;
}
const gcd=(a,b)=>{while(b){[a,b]=[b,a%b];}return a;};
function rational(value){
  if(typeof value==='object'&&value!==null)return [BigInt(value.numerator),BigInt(value.denominator)];
  if(!Number.isFinite(value)||value<0||value>1)throw new RangeError('max_p must be between 0 and 1');
  const [mantissa,exponent='0']=String(value).toLowerCase().split('e');const [whole,fraction='']=mantissa.split('.');
  let n=BigInt(whole+fraction),d=10n**BigInt(fraction.length);const e=Number(exponent);if(e<0)d*=10n**BigInt(-e);else n*=10n**BigInt(e);return [n,d];
}
export function aqmArrival(state,dscp,depth,thresholds,maxP){
  const range=thresholds[dscp];if(!range)throw new RangeError(`Missing AQM thresholds for ${dscp}`);
  const [min,max]=range;if(!Number.isSafeInteger(depth)||depth<0||min<0||max<=min)throw new RangeError('Invalid AQM depth/thresholds');
  const next=structuredClone(state);if(depth>=max)return {state:next,drop:true,probability:1};
  if(depth<=min)return {state:next,drop:false,probability:0};
  const [pn,pd]=rational(maxP);if(pd<=0n||pn<0n||pn>pd)throw new RangeError('Invalid max_p fraction');
  let n=BigInt(next[dscp]?.n??0),d=BigInt(next[dscp]?.d??1);
  const addN=pn*BigInt(depth-min),addD=pd*BigInt(max-min);n=n*addD+addN*d;d*=addD;
  const drop=n>=d;if(drop)n-=d;const factor=gcd(n,d);next[dscp]={n:String(n/factor),d:String(d/factor)};
  return {state:next,drop,probability:Number(addN)/Number(addD)};
}
