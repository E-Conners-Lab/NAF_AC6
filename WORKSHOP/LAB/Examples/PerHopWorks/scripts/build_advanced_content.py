"""Author the seven advanced work orders and their deliberately failing configurations."""
from pathlib import Path
import runpy,copy,json
base=runpy.run_path(str(Path(__file__).with_name('build_content.py')))
globals().update({k:base[k] for k in ['m','edge','incoming','outgoing','crate','add','levels','write','DATA','profile']})
def change(factory,id,**config):
 x=copy.deepcopy(factory);next(m for m in x['machines'] if m['id']==id)['config'].update(config);return x
def docks(ins,outs):return [m(d['id'],'dock_in',d['x'],d['y']) for d in ins]+[m(d['id'],'dock_out',d['x'],d['y']) for d in outs]
def question(trace,machine):return [{'id':p['id'],'crate':p['id'],'machine':machine if isinstance(machine,str) else machine[p['dock']],'kind':'color','prompt':f"{p['id']}: green, yellow or red?"} for p in trace]
def finalize(l,ref,ms=50,end=None,grid=(32,28),plain='',steps=None):
 w=l['work_order'];w.update(tick_ms=ms,grid={'width':grid[0],'height':grid[1]},max_drain_ticks=1200)
 if end:w['measurement_end_tick']=end
 if l['id'] in ['L06','L07','L08']:
  for d in w['docks_out']:d['bytes_per_tick']=10000
  l['briefing']['simplifications'].append('Output docks can accept the whole burst; these lessons isolate metering from output congestion.')
 counts={}
 for n in ref['machines']:
  if not n['type'].startswith('dock_'):counts[n['type']]=counts.get(n['type'],0)+1
 w['palette']={**counts,'belt':2000}
 l['briefing']['plain_language']=plain;l['guide']=steps or []
 return l
# L06: one fixed prediction part and one editable policer contract.
ins=[incoming('in',1,4)];outs=[outgoing('voice-out',16,2)]
ref={'machines':docks(ins,outs)+[m('tank','tank_single',5,4,{'rate':1000,'burst':1000}),m('recycle','recycler',11,7)],'links':[edge('in','out','tank'),edge('tank','conform','voice-out'),edge('tank','exceed','recycle')]}
trace=[crate('contract-1',0,'in',184,'telephony',size=500),crate('contract-2',0,'in',184,'telephony',size=500)]+[crate(f'flood-{i}',0,'in',184,'telephony',size=1000) for i in range(4)]+[crate('contract-later',20,'in',184,'telephony',size=1000)]
for p in trace:p['label']['flood']=p['id'].startswith('flood')
initial=change(ref,'tank',rate=10000,burst=5000)
l=add(6,'The Water Tower','Spend tokens to keep voice within its contract.',ins,outs,ref,initial,trace,[{'id':'METER-PREDICT'},{'id':'POLICE-EF','params':{'rate_limits':{'tank':1000},'min_excess_drops':4}}],['F-0009','F-0010','F-0016'],['A token pays for one byte. The bucket starts full.','The fixed prediction tank holds 1000 bytes and refills at 1000 bytes per second.','For the build, match the 1000 B/s contract and a 1000-byte burst. Keep the excess lane connected to the Recycler.'],[('unpoliced',initial,'POLICE-EF','unpoliced-priority','The configured rate exceeds the voice contract, so the burst flood is admitted instead of being policed.')],predictions=question(trace,'tank'),prediction_factory=copy.deepcopy(ref))
finalize(l,ref,plain='The tank is a spending limit. Each byte needs one token. Green means the crate fits; red means it exceeds the allowance. First predict the fixed tank, then repair the editable tank below.',steps=['Predict the fixed tank: 1000 B/s, burst 1000 bytes.','Select tank and set its rate and burst to the contract values.','Run both parts. Only a pass on both completes the work order.'])
# L07: literal srTCM seed and three markers.
ins=[incoming('in',1,10)];outs=[outgoing(c+'-out',21,y) for c,y in [('green',3),('yellow',10),('red',17)]]
ref={'machines':docks(ins,outs)+[m('cascade','tank_cascade',6,10,{'cir':1000,'cbs':1500,'ebs':3000,'mode':'blind'})],'links':[edge('in','out','cascade')]}
for c,y,value in [('green',3,18),('yellow',10,20),('red',17,22)]:ref['machines'].append(m('paint-'+c,'paint_booth',13,y,{'dscp':value}));ref['links'] += [edge('cascade',c,'paint-'+c),edge('paint-'+c,'out',c+'-out')]
trace=[crate('burst-'+str(i+1),0,'in',0,'low_latency',size=1000) for i in range(5)]+[crate('refilled',20,'in',0,'low_latency',size=1000)]
initial=copy.deepcopy(ref)
for n in initial['machines']:
 if n['type']=='paint_booth':n['config']['dscp']=0
wrong=change(ref,'paint-yellow',dscp=18)
l=add(7,'Cascade','One refill stream, two buckets, three colors.',ins,outs,ref,initial,trace,[{'id':'METER-PREDICT'},{'id':'MARK','params':{'color_targets':{'low_latency':{'green':18,'yellow':20,'red':22}}}}],['F-0019','F-0020','F-0021','F-0026'],['Green spends committed tokens. Yellow spends excess tokens. Red spends neither.','Committed tokens refill first; only their overflow fills the excess bucket.','Mark green AF21, yellow AF22 and red AF23. The suffix is drop precedence, not another service class.'],[('yellow',wrong,'MARK','wrong-mark','The yellow lane uses the green codepoint. The meter color must choose the corresponding AF2x marking.')],predictions=question(trace,'cascade'),prediction_factory=copy.deepcopy(ref))
finalize(l,ref,plain='A cascade has a main bucket and an overflow bucket. A crate is green if the main bucket can pay, yellow if only the overflow bucket can pay, and red if neither can pay.',steps=['Predict the fixed 1000 B/s cascade: CBS 1500, EBS 3000.','Paint the three output lanes AF21 (18), AF22 (20), AF23 (22).','Red is a color here; this work order delivers all three colors.'])
# L08: independent trusted-aware and untrusted-blind twin tanks.
ins=[incoming('trusted',1,5,True),incoming('user',1,18,False)];outs=[];nodes=[];links=[];trace=[]
for dock,y,mode in [('trusted',5,'aware'),('user',18,'blind')]:
 nodes += [m(dock,'dock_in',1,y),m('twin-'+dock,'tank_twin',6,y,{'pir':4000,'pbs':3000,'cir':1000,'cbs':1500,'mode':mode})];links.append(edge(dock,'out','twin-'+dock))
 for c,delta,value in [('green',-3,34),('yellow',0,36),('red',3,38)]:
  pid=f'paint-{dock}-{c}';out=f'{dock}-{c}-out';nodes += [m(pid,'paint_booth',13,y+delta,{'dscp':value}),m(out,'dock_out',22,y+delta)];outs.append(outgoing(out,22,y+delta));links += [edge('twin-'+dock,c,pid),edge(pid,'out',out)]
 for i in range(5):
  color=['yellow','green','red','green','green'][i] if dock=='trusted' else 'red';value={'green':34,'yellow':36,'red':38}[color];trace.append(crate(f'{dock}-{i+1}',0 if i<4 else 10,dock,value*4,'conferencing',size=1000,color=color))
ref={'machines':nodes,'links':links};initial=change(ref,'twin-trusted',mode='blind');initial=change(initial,'twin-user',mode='aware');wrong=change(ref,'twin-trusted',mode='blind')
l=add(8,'Twin Towers','Respect trusted colors; measure untrusted traffic afresh.',ins,outs,ref,initial,trace,[{'id':'METER-PREDICT'},{'id':'METER-MODE','params':{'modes':{'twin-trusted':'aware','twin-user':'blind'}}},{'id':'MARK','params':{'color_targets':{'conferencing':{'green':34,'yellow':36,'red':38}}}}],['F-0022','F-0023','F-0024','F-0025','F-0027'],['Peak and committed tokens refill independently.','An aware meter never upgrades an incoming yellow or red crate.','Use aware on the trusted lane and blind on the untrusted lane. Both use PIR 4000, PBS 3000, CIR 1000, CBS 1500.'],[('mode',wrong,'METER-MODE','wrong-meter-mode','The trusted path ignores the incoming color and may upgrade traffic that was already marked yellow or red.')],predictions=question(trace,{'trusted':'twin-trusted','user':'twin-user'}),prediction_factory=copy.deepcopy(ref))
finalize(l,ref,plain='The two tanks measure different limits: peak and committed rate. A trusted color is a previous measurement you must respect. An untrusted color is a claim you measure again.',steps=['Predict the fixed tanks: trusted aware, user blind.','Change the editable trusted tank to aware and the user tank to blind.','The three paint lanes are already prepared as AF41, AF42 and AF43.'])
# L09 priority under a real flood.
ins=[incoming('voice',1,3),incoming('web',1,17)];outs=[outgoing('out',28,10,1000)]
ref={'machines':docks(ins,outs)+[m('policer','tank_single',6,3,{'rate':1000,'burst':1000}),m('recycle','recycler',12,6),m('voice-q','buffer_belt',15,3,{'capacity':256}),m('web-q','buffer_belt',15,17,{'capacity':256}),m('merge','priority_merger',23,10,{'quantum':1000,'priority':'voice','weights':{'web':1}})],'links':[edge('voice','out','policer'),edge('policer','conform','voice-q'),edge('policer','exceed','recycle'),edge('voice-q','out','merge','voice'),edge('web','out','web-q'),edge('web-q','out','merge','web'),edge('merge','out','out')]}
trace=[]
for t in range(60):
 if t in [0,20,40]:trace.append(crate('contract-'+str(t),t,'voice',184,'telephony',size=200))
 p=crate('flood-'+str(t),t,'voice',184,'telephony',size=1000);p['label']['flood']=True;trace += [p,crate('web-'+str(t),t,'web',0,'standard',size=1000)]
initial=change(ref,'policer',rate=100000,burst=5000)
l=add(9,'Express Lane','Protect priority service without starving the shared lane.',ins,outs,ref,initial,trace,[{'id':'POLICE-EF','params':{'rate_limits':{'policer':1000},'min_excess_drops':20}},{'id':'DELAY-BOUND','params':{'max_ticks':3}},{'id':'MIN-SHARE','params':{'bytes':{'standard':20000}}}],['F-0016','F-0013','F-0028'],['The priority queue is served whenever it has an eligible crate.','A flood can keep that queue full. Police before the queue, not after it.','The voice contract is 1000 B/s with a 1000-byte burst. The web lane needs 20,000 bytes during the measurement window.'],[('flood',initial,'POLICE-EF','unpoliced-priority','The oversized policer admits a priority flood, taking capacity needed by the shared lane.')])
finalize(l,ref,end=110,plain='An express lane only helps if its entry is controlled. Otherwise a flood can occupy it continuously. Repair the voice policer and watch the web queue begin to move.',steps=['Set policer to 1000 B/s and a 1000-byte burst.','Run the trace and compare delivered web bytes with its 20,000-byte goal.','Inspect one voice crate to see its queue delay.'])
# L10 weighted byte shares, explicit DF marker makes the default queue dedicated.
keys=[('video','conferencing',34,3),('backup','high_throughput',10,2),('web','standard',0,1)];ins=[];outs=[outgoing('out',28,10,1000)];nodes=[];links=[];trace=[]
for i,(lane,cls,dscp,weight) in enumerate(keys):
 y=3+i*7;ins.append(incoming(lane,1,y));nodes += [m(lane,'dock_in',1,y),m('paint-'+lane,'paint_booth',6,y,{'dscp':dscp}),m(lane+'-q','buffer_belt',15,y,{'capacity':256})];links += [edge(lane,'out','paint-'+lane),edge('paint-'+lane,'out',lane+'-q'),edge(lane+'-q','out','merge',lane)]
 for t in range(80):trace.append(crate(lane+'-'+str(t),t,lane,0,cls,size=1000))
nodes += [m('merge','priority_merger',23,10,{'quantum':500,'priority':'priority','weights':{k[0]:k[3] for k in keys}}),m('out','dock_out',28,10)];links.append(edge('merge','out','out'));ref={'machines':nodes,'links':links};initial=change(ref,'merge',weights={'video':20,'backup':1,'web':1})
l=add(10,'Shares','Share output bytes among queues, including Default.',ins,outs,ref,initial,trace,[{'id':'MIN-SHARE','params':{'bytes':{'conferencing':30000,'high_throughput':20000,'standard':8000}}},{'id':'STANDARD-PRESENT'}],['F-0013','F-0015','F-0028'],['Weights buy byte service, not packet-count quotas.','The Default queue must remain reachable and have a positive weighted share.','Try the planned 3:2:1 allocation for video, backup and web. Check bytes before the congestion window closes.'],[('starvation',initial,'MIN-SHARE','class-starved','The video weight takes too much of the finite congestion window. Backup or Default misses its required byte budget.')])
finalize(l,ref,end=130,plain='Think of the weights as turns in a shared loading schedule. A weight of three receives more byte credit than a weight of one. No queue should disappear from the schedule.',steps=['Select merge and set video 3, backup 2, web 1.','Keep the Default marker at DSCP 0.','Run and inspect the measured bytes in the congestion window.'])
# L11 ordered AQM within one shared AF4 queue.
ins=[incoming('in',1,10)];outs=[outgoing('out',28,10,500)]
ref={'machines':docks(ins,outs)+[m('sort','sorter',6,10,{'mode':'ba','rules':[{'value':d,'port':'af'} for d in [34,36,38]]}),m('spillway','spillway',15,4,{'capacity':64,'thresholds':{'AF43':[10,20],'AF42':[20,30],'AF41':[30,40]},'max_p':.1}),m('protected-q','buffer_belt',15,18,{'capacity':64}),m('merge','priority_merger',23,10,{'quantum':500,'priority':'priority','weights':{'af':1,'protected':1}})],'links':[edge('in','out','sort'),edge('sort','af','spillway'),edge('sort','default','protected-q'),edge('spillway','out','merge','af'),edge('protected-q','out','merge','protected'),edge('merge','out','out')]}
trace=[crate(f'AF4{s}-{t}',t,'in',d*4,'conferencing',size=500) for t in range(80) for s,d in [(1,34),(2,36),(3,38)]]+[crate(name,10+i*10,'in',d*4,cls,size=500) for i,(name,d,cls) in enumerate([('EF',46,'telephony'),('CS5',40,'signaling'),('CS4',32,'interactive'),('CS3',24,'broadcast')])]
initial=change(ref,'spillway',thresholds={'AF43':[10,25],'AF42':[20,30],'AF41':[30,40]});wrong=copy.deepcopy(ref);next(n for n in wrong['machines'] if n['id']=='sort')['config']['rules'].append({'value':46,'port':'af'});next(n for n in wrong['machines'] if n['id']=='spillway')['config']['thresholds']['EF']=[0,64]
l=add(11,'Spillway','Drop higher AF drop precedence sooner as the queue grows.',ins,outs,ref,initial,trace,[{'id':'NO-AQM-ON'},{'id':'RED-THRESHOLDS','params':{'class':'AF4'}},{'id':'LOSS-ORDER','params':{'class':'AF4'}}],['F-0029','F-0030','F-0031','F-0032'],['AF43 starts dropping first, then AF42, then AF41.','The maximum threshold of AF43 must not exceed the minimum of AF42.','Keep EF, CS5, CS4 and CS3 on the ordinary Buffer Belt. The intended AF ranges are 10–20, 20–30 and 30–40.'],[('overlap',initial,'RED-THRESHOLDS','thresholds-overlap','AF43 continues into AF42’s dropping range because its maximum is above AF42’s minimum.'),('ef-aqm',wrong,'NO-AQM-ON','aqm-on-ef','The voice path reaches a Spillway. RFC 4594 recommends against AQM for the Telephony service class.')])
finalize(l,ref,end=150,plain='A Spillway starts discarding selected crates before its queue fills. Within AF4, the third drop-precedence color must be treated more harshly than the first.',steps=['Change AF43 maximum from 25 to 20.','Keep the protected traffic on the ordinary buffer.','Run and compare offered/dropped counts for all three AF4 markings.'])
l['briefing']['simplifications'] += ['Queue depth is instantaneous, not averaged.','Drops use exact deterministic spacing, not random sampling.','Measured loss on this finite trace does not prove a stochastic loss-probability guarantee.']
# L12: historical Example 3, nine classes; current LE update explained explicitly.
profile['low_priority']={'label':'Low Priority (2006 profile)','dscp':8,'name':'CS1','application':'background','color':'#8b9299','pattern':'chevron','source':'RFC 4594 §2.4.3 (historical); RFC 8622 §10 updates this mapping','facts':['F-0033','F-0035']}
profiles=json.loads((DATA/'profiles.json').read_text());profiles['rfc4594']['classes']=profile;write('profiles.json',profiles)
rows={'network_control':2,'oam':5,'standard':8,'telephony':11,'signaling':14,'conferencing':17,'streaming':20,'high_throughput':23,'low_priority':26}
ins=[incoming('routing',1,2,True),incoming('access',1,11,False),incoming('conference',1,17,True)];outs=[outgoing('out',31,14,1500)];nodes=docks(ins,outs);links=[];rules=[];weights={};targets={k:profile[k]['dscp'] for k in rows if k!='conferencing'}
for key,y in rows.items():
 q='q-'+key
 if key=='conferencing':
  nodes += [m('conf-sort','sorter',6,y,{'mode':'ba','rules':[{'value':d,'port':'af'} for d in [34,36,38]]}),m('conf-recycle','recycler',10,19),m(q,'spillway',23,y,{'capacity':64,'thresholds':{'AF43':[10,20],'AF42':[20,30],'AF41':[30,40]},'max_p':.1})];links += [edge('conference','out','conf-sort'),edge('conf-sort','af',q),edge('conf-sort','default','conf-recycle')]
 else:
  paint='paint-'+key;nodes += [m(paint,'paint_booth',11,y,{'dscp':profile[key]['dscp']}),m(q,'buffer_belt',23,y,{'capacity':256})]
  if key=='network_control':links.append(edge('routing','out',paint))
  else:
   port='default' if key=='standard' else key;links.append(edge('access-sort',port,paint))
   if key!='standard':rules.append({'field':'application','value':profile[key]['application'],'port':key})
  if key=='telephony':
   nodes += [m('policer','tank_single',16,y,{'rate':2000,'burst':1000}),m('voice-recycle','recycler',20,13)];links += [edge(paint,'out','policer'),edge('policer','conform',q),edge('policer','exceed','voice-recycle')]
  else:links.append(edge(paint,'out',q))
 links.append(edge(q,'out','merge',key));weights[key]=3 if key in ['conferencing','network_control'] else 2 if key in ['streaming','standard','high_throughput'] else 1
weights.pop('telephony');nodes += [m('access-sort','sorter',6,11,{'mode':'mf','rules':rules}),m('merge','priority_merger',28,14,{'quantum':500,'priority':'telephony','weights':weights})];links += [edge('access','out','access-sort'),edge('merge','out','out')];ref={'machines':nodes,'links':links};trace=[]
for t in range(160):
 trace.append(crate('routing-'+str(t),t,'routing',192,'network_control','routing',100))
 if t==0:trace.append(crate('voice-contract',t,'access',192,'telephony','voip',100))
 p=crate('voice-flood-'+str(t),t,'access',192,'telephony','voip',1000);p['label']['flood']=True;trace.append(p)
 for key,period,size in [('oam',5,250),('standard',1,500),('signaling',4,100),('streaming',2,500),('high_throughput',1,1000),('low_priority',1,1000)]:
  if t%period==0:trace.append(crate(key+'-'+str(t),t,'access',192,key,profile[key]['application'],size))
 for s,d,c in [(1,34,'green'),(2,36,'yellow'),(3,38,'red')]:trace.append(crate(f'conf{s}-{t}',t,'conference',d*4,'conferencing','conference',500,color=c))
initial=change(ref,'policer',rate=100000,burst=5000);initial=change(initial,'q-conferencing',thresholds={'AF43':[10,25],'AF42':[20,30],'AF41':[30,40]});wrongtrust=change(ref,'paint-standard',dscp=48);wrongdf=change(ref,'paint-standard',dscp=8);wrongrate=change(ref,'policer',rate=100000,burst=5000)
checks=[{'id':'MARK','params':{'targets':targets,'color_targets':{'conferencing':{'green':34,'yellow':36,'red':38}},'allowed_drop_classes':['telephony','conferencing']}},{'id':'TRUST'},{'id':'POLICE-EF','params':{'rate_limits':{'policer':2000},'min_excess_drops':80}},{'id':'DELAY-BOUND','params':{'max_ticks':4}},{'id':'MIN-SHARE','params':{'bytes':{'network_control':8000,'oam':3000,'standard':10000,'signaling':1000,'streaming':8000,'high_throughput':14000,'low_priority':2000,'conferencing':14000}}},{'id':'STANDARD-PRESENT'},{'id':'NO-AQM-ON'},{'id':'RED-THRESHOLDS','params':{'class':'AF4'}},{'id':'LOSS-ORDER','params':{'class':'AF4'}}]
l=add(12,'Rush Hour','Bring nine service classes through one busy enterprise hop.',ins,outs,ref,initial,trace,checks,['F-0033','F-0034','F-0035','F-0016','F-0018','F-0029','F-0030','F-0031','F-0032'],['Follow the access path: classify the application, mark, then queue.','Repair the voice contract before the priority queue. Keep an independent DF queue.','Use 2000 B/s and a 1000-byte voice burst. Correct the AF43 maximum to 20, then inspect every remaining check.'],[('trust',wrongtrust,'TRUST','untrusted-mark','The untrusted Default path still carries a control marking after its marker.'),('default',wrongdf,'STANDARD-PRESENT','missing-standard','Default traffic is being marked as another class, so the factory has no dedicated reachable DF queue.'),('priority',wrongrate,'POLICE-EF','unpoliced-priority','The voice flood exceeds the work-order contract but is admitted to the strict-priority input.')])
finalize(l,ref,ms=20,end=240,grid=(34,30),plain='This is the full factory. Two settings are deliberately wrong: the voice limit is too large, and the AF43 dropping range overlaps AF42. Repair them, then use the checks to verify the whole hop.',steps=['Set policer to 2000 B/s and burst 1000 bytes.','Set q-conferencing AF43 maximum to 20.','Run all checks. This same verified factory powers the presentation demo.'])
l['work_order']['allowed_drop_classes']=['telephony','conferencing'];l['briefing']['simplifications'] += ['This is the historical nine-class RFC 4594 Example 3. RFC 8622 replaces its CS1 Low Priority mapping with LE (DSCP 1); LE behavior is outside this version.','RFC 5865 admission control is not simulated.','Queue depth is instantaneous; drop spacing is deterministic; no sender feedback is simulated.','Conferencing arrives already classified and colored at a trusted boundary.','Weights, capacities and rate contracts are this work order’s teaching values, not universal RFC configuration values.']
# Preserve readable summaries, while retaining verified detail for each level.
plain={1:'Every voice crate carries the same lane label: DSCP 46. One sorter rule is looking for 47 instead. Make that small correction and watch both voice crates take the voice lane.',2:'A marker changes the six DSCP lights. Use their weights to make each requested codepoint. The two smaller ECN lights are preserved automatically.',3:'This old sorter reads only the first three DSCP lights. Different six-bit labels can look the same to it. Predict which p0, p1, p4 or p5 dock each crate reaches.',4:'The shipping label tells you what the application is. The sorter already separates the applications; set each paint booth to the recommended service label.',5:'A trusted router may use a routing label. A user device cannot grant itself that privilege. Clear the six DSCP lights on the untrusted remark booth.'}
for i,l in enumerate(levels,1):
 if i in plain:l['briefing']['plain_language']=plain[i]
 if i>=6:l['briefing']['simplifications']+=['Token buckets begin full. Refill is exact to whole bytes; sub-byte credit is retained.'] if i in [6,7,8,9,12] else []
write('levels.json',levels)
print('Authored complete campaign:',len(levels),'levels')
