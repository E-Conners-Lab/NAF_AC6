export function classAppearance(name,classes){return classes[name]??Object.values(classes).find(c=>c.name===name||(/^AF[1-4][1-3]$/.test(name)&&c.name.slice(0,3)===name.slice(0,3)))??{label:name,color:'#e4bb73',pattern:'plain'};}
export function patternInk(color){const [r,g,b]=[1,3,5].map(i=>parseInt(color.slice(i,i+2),16)/255);return .2126*r+.7152*g+.0722*b<.43?'#fff6de':'#102c3b';}
