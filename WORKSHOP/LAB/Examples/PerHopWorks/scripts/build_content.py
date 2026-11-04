"""Author deterministic, auditable level fixtures; no stored correct prediction answers."""
from pathlib import Path
import json,copy
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/'data'
for sub in ['traces','solutions']:(DATA/sub).mkdir(exist_ok=True)
def write(path,obj):(DATA/path).write_text(json.dumps(obj,indent=2)+'\n')
def m(id,type,x,y,config=None):return dict(id=id,type=type,x=x,y=y,rotation=0,config=config or {})
def edge(a,p,b,input='in'):return {'from':a,'port':p,'to':b,'input':input}
def incoming(id,x,y,trusted=True):return dict(id=id,x=x,y=y,trusted=trusted)
def outgoing(id,x,y,capacity=1500):return dict(id=id,x=x,y=y,bytes_per_tick=capacity)
def crate(id,tick,dock,octet,cls,app='',size=500,**kw):return dict(id=id,tick=tick,dock=dock,octet=octet,**{'class':cls},label={'application':app},size=size,**kw)
facts=json.loads((DATA/'facts.json').read_text());byid={f['id']:f for f in facts}
profile=json.loads((DATA/'profiles.json').read_text())['rfc4594']['classes']
levels=[]
def add(n,title,concept,ins,outs,reference,initial,trace,checks,ids,hints,wrong,**extras):
 lid=f'L{n:02}'; diagnostics={}
 for suffix,config,check,diag,why in wrong:
  write(f'solutions/{lid}-wrong-{suffix}.json',config)
  diagnostics[diag]={'why_wrong':why,'concept_reinforced':concept,'source':byid[ids[0]]['source'],'facts':ids}
 level={'id':lid,'act':1 if n<=3 else 2 if n<=8 else 3,'title':title,'concept':concept,'prerequisites':[] if n==1 else [f'L{n-1:02}'],'profile':'rfc4594','type':'build','briefing':{'title':title,'explanation':' '.join(byid[x]['claim'] for x in ids),'example':concept,'simplifications':['Crates stand for packets; shipping labels stand for packet fields and application identity.','Time advances in fixed ticks. Traffic traces do not react to loss.','Belts add one tick per grid tile; factory geometry is a teaching metaphor.'],'facts':ids},'work_order':{'tick_ms':70,'grid':{'width':24,'height':24},'docks_in':ins,'docks_out':outs,'locked':[d['id'] for d in ins+outs],'palette':{'belt':1000,'sorter':4,'paint_booth':12,'recycler':4,'buffer_belt':12,'priority_merger':2,'tank_single':3,'tank_cascade':2,'tank_twin':4,'spillway':4},'bounds':{},'trace':f'traces/{lid}.json','measurement_start_tick':0,'measurement_end_tick':max([p['tick'] for p in trace]+[0])+100,'max_drain_ticks':500},'checks':[{'id':'VALID'},{'id':'CONSERVATION'}]+checks,'diagnostics':diagnostics,'hints':[{'text':text,'facts':ids,'source':byid[ids[0]]['source']} for text in hints],'reference_solution':f'solutions/{lid}.json','initial_factory':initial,'known_wrong':[{'config':f'solutions/{lid}-wrong-{suffix}.json','must_fail':check,'diagnostic':diag} for suffix,config,check,diag,why in wrong],'source':'; '.join(dict.fromkeys(byid[x]['source'] for x in ids))}
 level.update(extras);levels.append(level);write(f'solutions/{lid}.json',reference);write(f'traces/{lid}.json',trace);return level
# L01
ins=[incoming('in',1,4)];outs=[outgoing('voice',13,1),outgoing('video',13,4),outgoing('standard',13,7)]
sort=m('sort','sorter',5,4,{'mode':'ba','rules':[{'value':46,'port':'voice'},{'value':34,'port':'video'}]})
ref={'machines':[m('in','dock_in',1,4),sort]+[m(d['id'],'dock_out',d['x'],d['y']) for d in outs],'links':[edge('in','out','sort'),edge('sort','voice','voice'),edge('sort','video','video'),edge('sort','default','standard')]}
initial=copy.deepcopy(ref);initial['machines'][1]['config']['rules'][0]['value']=47
trace=[crate('voice-clear',0,'in',184,'telephony','voip'),crate('voice-ecn',4,'in',185,'telephony','voip'),crate('video',8,'in',136,'conferencing','conference'),crate('web',12,'in',0,'standard','web')]
add(1,'Six Lights','Read six DSCP lights without confusing the two ECN lights.',ins,outs,ref,initial,trace,[{'id':'ROUTE','params':{'routes':{'46':'voice','34':'video','0':'standard'}}}],['F-0001','F-0002'],['Separate the two smaller ECN lights from the six DSCP lights.','The six weights are 32, 16, 8, 4, 2 and 1. Add only the lit DSCP weights.','The two voice crates have different ECN bits. Their six-bit DSCP values still match.'],[('ecn',initial,'ROUTE','wrong-route','The BA sorter compares the wrong six-bit value. ECN does not change which PHB the DSCP selects.')])
# L02 independent paint lanes
names=['EF','AF41','AF31','CS6','CS1'];values=[46,34,26,48,8];ins=[];outs=[];nodes=[];links=[];trace=[];targets={}
for i,(name,value) in enumerate(zip(names,values)):
 y=2+i*4;ind=f'in{i}';out=f'out{i}';paint=f'paint{i}';ins.append(incoming(ind,1,y));outs.append(outgoing(out,15,y));nodes += [m(ind,'dock_in',1,y),m(paint,'paint_booth',8,y,{'dscp':value}),m(out,'dock_out',15,y)];links += [edge(ind,'out',paint),edge(paint,'out',out)];trace.append(crate(name,0,ind,0,name));targets[name]=value
ref={'machines':nodes,'links':links};initial=copy.deepcopy(ref)
for node in initial['machines']:
 if node['type']=='paint_booth':node['config']['dscp']=0
wrong=copy.deepcopy(ref);wrong['machines'][1]['config']['dscp']=40
add(2,'Codepoint Forge','Make named DSCPs with six bit toggles.',ins,outs,ref,initial,trace,[{'id':'MARK','params':{'targets':targets}}],['F-0003','F-0004','F-0005'],['CS codepoints end with three zero bits.','AF class and drop precedence occupy different parts of the six-bit value.','Use the codepoint formula in the briefing, then express the result as six bit weights.'],[('ef',wrong,'MARK','wrong-mark','The paint booth produces a different DSCP from the named target. A nearby binary value is a different codepoint.')])
# L03 fixed legacy sorter
ins=[incoming('in',1,10)];outs=[outgoing('p0',16,3),outgoing('p1',16,7),outgoing('p4',16,11),outgoing('p5',16,15)]
ref={'machines':[m('in','dock_in',1,10),m('legacy','sorter',7,10,{'mode':'precedence','rules':[{'value':1,'port':'p1'},{'value':4,'port':'p4'},{'value':5,'port':'p5'}]})]+[m(d['id'],'dock_out',d['x'],d['y']) for d in outs],'links':[edge('in','out','legacy'),edge('legacy','default','p0')]+[edge('legacy',p,p) for p in ['p1','p4','p5']]}
trace=[crate(name,i*4,'in',value*4,name) for i,(name,value) in enumerate([('AF41',34),('AF43',38),('EF',46),('CS5',40),('AF11',10),('CS1',8),('DF',0)])]
wrong=copy.deepcopy(ref);wrong['submission']={'predictions':{p['id']:'p0' for p in trace}}
level=add(3,'The Old Sorter','Predict what only the upper three bits reveal.',ins,outs,ref,copy.deepcopy(ref),trace,[{'id':'PREDICT'}],['F-0006'],['Read only the first three of the six DSCP lights.','Compare AF41 with AF43, then EF with CS5.','The old sorter cannot recover information from bits it does not read.'],[('predictions',wrong,'PREDICT','wrong-prediction','At least one predicted dock differs from the three-bit precedence route computed by the engine.')],type='predict',predictions=[{'id':p['id'],'crate':p['id'],'kind':'route','prompt':f"Where does {p['id']} go?"} for p in trace])
level['fixed_factory']=copy.deepcopy(ref);level['work_order']['locked'].append('legacy')
# L04 ten application classes
keys=['telephony','signaling','conferencing','interactive','streaming','broadcast','low_latency','oam','high_throughput','standard']
ins=[incoming('in',1,10,False)];outs=[];nodes=[m('in','dock_in',1,10)];links=[edge('in','out','sort')];rules=[];trace=[];targets={}
for i,key in enumerate(keys):
 c=profile[key];y=1+i*2;outs.append(outgoing('out-'+key,21,y));nodes += [m('paint-'+key,'paint_booth',13,y,{'dscp':c['dscp']}),m('out-'+key,'dock_out',21,y)];links += [edge('sort',key if key!='standard' else 'default','paint-'+key),edge('paint-'+key,'out','out-'+key)];targets[key]=c['dscp'];trace.append(crate(key,i*4,'in',0,key,c['application']))
 if key!='standard':rules.append({'field':'application','value':c['application'],'port':key})
nodes.append(m('sort','sorter',6,10,{'mode':'mf','rules':rules}));ref={'machines':nodes,'links':links};initial=copy.deepcopy(ref)
for node in initial['machines']:
 if node['type']=='paint_booth':node['config']['dscp']=0
wrong=copy.deepcopy(ref);wrong['machines'][-1]['config']['rules'][0]['value']='mistyped-application'
add(4,'Who Goes Where','Classify the shipping label, then mark the service class.',ins,outs,ref,initial,trace,[{'id':'MARK','params':{'targets':targets}}],['F-0007','F-0008']+[profile[k]['facts'][0] for k in keys],['Read the shipping-label application before choosing a route.','MF rules are tested in order; the first match selects the output.','The marker on a route assigns the service-class DSCP. The marker and classifier are separate elements.'],[('mf',wrong,'MARK','wrong-mark','The VoIP label does not match its intended MF rule, so its marker produces the wrong service-class DSCP.')])
# L05 two trust domains
ins=[incoming('trusted',1,3,True),incoming('user',1,9,False)];outs=[outgoing('core',17,3),outgoing('access',17,9)]
ref={'machines':[m('trusted','dock_in',1,3),m('user','dock_in',1,9),m('remark','paint_booth',9,9,{'dscp':0}),m('core','dock_out',17,3),m('access','dock_out',17,9)],'links':[edge('trusted','out','core'),edge('user','out','remark'),edge('remark','out','access')]}
trace=[crate('routing',0,'trusted',192,'network_control','routing'),crate('spoofed-cs6',2,'user',192,'standard','web'),crate('spoofed-cs7',6,'user',224,'standard','web')]
initial=copy.deepcopy(ref);initial['machines'][2]['config']['dscp']=48
add(5,'Trust Boundary','Accept a trusted routing mark; re-mark untrusted claims.',ins,outs,ref,initial,trace,[{'id':'TRUST'},{'id':'MARK','params':{'targets':{'network_control':48,'standard':0}}}],['F-0017','F-0018','F-0008'],['The source dock defines trust; the crate cannot declare itself trusted.','Only the untrusted path needs its control marking removed.','A marker changes the six DSCP bits while preserving the two ECN bits.'],[('trust',initial,'TRUST','untrusted-mark','The untrusted lane still delivers a network-control marking. Changing CS7 to CS6 does not remove its privileged claim.')])

for i,l in enumerate(levels,1):
 l['work_order']['palette']={1:{'sorter':1,'belt':120},2:{'paint_booth':5,'belt':250},3:{'sorter':1,'belt':160},4:{'sorter':2,'paint_booth':10,'belt':1000},5:{'paint_booth':2,'recycler':2,'belt':200}}[i]
write('levels.json',levels)
print('Authored',len(levels),'levels with references and known-wrong fixtures.')
