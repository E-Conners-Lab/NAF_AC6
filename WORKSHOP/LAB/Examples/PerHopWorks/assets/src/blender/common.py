"""Original Per-Hop Works procedural geometry. Invoked by each asset's saved recipe through MCP."""
import bpy, math, json
from pathlib import Path
from mathutils import Vector
ROOT=Path(__file__).resolve().parents[2]
IVORY=(.78,.81,.76,1); DARK=(.055,.09,.115,1); TEAL=(.08,.34,.32,1); ORANGE=(.75,.32,.10,1); METAL=(.27,.34,.36,1)
static=[]; animated=[]
def start(name):
 global static,animated,collection,asset
 static=[];animated=[];asset=name
 for c in list(bpy.data.collections):
  if c.name.startswith('PHW_'):
   for o in list(c.objects):bpy.data.objects.remove(o,do_unlink=True)
   bpy.data.collections.remove(c)
 collection=bpy.data.collections.new('PHW_'+name);bpy.context.scene.collection.children.link(collection)
 bpy.context.scene.unit_settings.system='METRIC';bpy.context.scene.unit_settings.scale_length=1
 for obj in bpy.context.scene.objects:obj.select_set(False)
 bpy.context.scene.world.color=(.16,.18,.2)
def material():
 m=bpy.data.materials.get('PHW_surface')
 if m:return m
 m=bpy.data.materials.new('PHW_surface');m.use_nodes=True
 n=m.node_tree.nodes;shader=n.get('Principled BSDF');shader.inputs['Roughness'].default_value=.6
 vertex=n.new('ShaderNodeVertexColor');vertex.layer_name='Col';m.node_tree.links.new(vertex.outputs['Color'],shader.inputs['Base Color'])
 return m
def finish_mesh(obj,color,name=None):
 for c in list(obj.users_collection):c.objects.unlink(obj)
 collection.objects.link(obj)
 obj.name=name or 'body_part';bpy.context.view_layer.objects.active=obj
 bpy.ops.object.transform_apply(location=False,rotation=True,scale=True)
 colors=obj.data.color_attributes.new(name='Col',type='FLOAT_COLOR',domain='CORNER')
 for c in colors.data:c.color=color
 obj.data.materials.clear();obj.data.materials.append(material());obj.color=color
 if name:animated.append(obj)
 else:static.append(obj)
 return obj
def box(pos,dim,color=IVORY,name=None,bevel=.025):
 bpy.ops.mesh.primitive_cube_add(size=1,location=pos);o=bpy.context.object;o.dimensions=dim
 bpy.ops.object.transform_apply(location=False,rotation=True,scale=True)
 if bevel:
  mod=o.modifiers.new('Small bevel','BEVEL');mod.width=min(bevel,min(dim)/4);mod.segments=1;bpy.ops.object.modifier_apply(modifier=mod.name)
 return finish_mesh(o,color,name)
def cylinder(pos,radius,depth,color=METAL,name=None,vertices=12):
 bpy.ops.mesh.primitive_cylinder_add(vertices=vertices,radius=radius,depth=depth,location=pos)
 return finish_mesh(bpy.context.object,color,name)
def beam(a,b,width,color=METAL):
 mid=(Vector(a)+Vector(b))/2;delta=Vector(b)-Vector(a)
 bpy.ops.mesh.primitive_cube_add(size=1,location=mid);o=bpy.context.object;o.dimensions=(width,width,delta.length);o.rotation_euler=delta.to_track_quat('Z','Y').to_euler();return finish_mesh(o,color)
def base():
 box((0,0,.085),(.94,.88,.17),DARK)
 box((0,0,.18),(.86,.74,.08),METAL)
def feet():
 for x in [-.34,.34]:
  for y in [-.3,.3]:box((x,y,.28),(.09,.09,.42),DARK)
def water(name,x,z,height,radius=.15):
 o=cylinder((x,0,z+height/2),radius,height,(.055,.5,.75,1),name)
 # The node origin is the water bottom; scaling its exported Y fills upward.
 for v in o.data.vertices:v.co.z+=height/2
 o.location.z=z
 return o
def tank(x,height,water_name):
 cylinder((x,0,.32),.205,.1,TEAL)
 cylinder((x,0,height+.36),.21,.1,IVORY)
 for y in [-.16,.16]:
  for dx in [-.14,.14]:beam((x+dx,y,.3),(x+dx,y,height+.36),.035,IVORY)
 water(water_name,x,.38,height-.06)
 box((x,-.215,.5),(.13,.08,.16),DARK)
def build(name):
 start(name)
 if name=='phw_floor_tile':box((0,0,-.045),(.99,.99,.09),(.16,.22,.25,1),bevel=.012)
 elif name in ['phw_belt_straight','phw_belt_corner']:
  box((0,0,.065),(1,.64,.13),DARK,bevel=.01)
  if name.endswith('straight'):
   for y in [-.3,.3]:box((0,y,.15),(1,.04,.12),METAL,bevel=0)
   for x in [-.4,-.2,0,.2,.4]:box((x,0,.14),(.035,.5,.025),(.4,.49,.5,1),bevel=0)
  else:
   box((0,0,.14),(.9,.9,.025),METAL,bevel=0)
   for n in range(5):
    t=-math.pi/2+n*math.pi/8;o=box((-.35+.35*math.cos(t),.35+.35*math.sin(t),.16),(.4,.035,.025),(.4,.49,.5,1),bevel=0);o.rotation_euler.z=t;bpy.ops.object.transform_apply(location=False,rotation=True,scale=True)
 elif name=='phw_buffer_belt':
  base()
  for y in [-.34,.34]:box((0,y,.4),(.9,.07,.38),IVORY)
  for x in [-.32,0,.32]:box((x,0,.25),(.045,.54,.05),TEAL)
  box((-.32,-.41,.55),(.07,.04,.24),(.05,.55,.72,1),'fill_marker')
  box((-.1,-.41,.55),(.045,.06,.27),ORANGE,'threshold_min')
  box((.24,-.41,.55),(.045,.06,.27),ORANGE,'threshold_max')
 elif name=='phw_sorter':
  base();box((-.24,0,.48),(.25,.68,.5),IVORY)
  for y in [-.27,0,.27]:box((.19,y,.26),(.6,.14,.08),TEAL)
  flap=box((.02,0,.39),(.5,.045,.13),ORANGE,'flap');cylinder((-.2,0,.42),.07,.22,METAL)
 elif name=='phw_paint_booth':
  base()
  for y in [-.32,.32]:box((0,y,.65),(.6,.1,.95),IVORY)
  box((0,0,1.1),(.7,.78,.14),TEAL);cylinder((0,0,.97),.07,.15,ORANGE,'nozzle')
  bpy.ops.mesh.primitive_cone_add(vertices=8,radius1=.17,radius2=.025,depth=.35,location=(0,0,.72));finish_mesh(bpy.context.object,(.25,.6,.62,1),'spray')
  box((-.31,-.34,.6),(.16,.12,.22),DARK)
 elif name in ['phw_tank_single','phw_tank_cascade','phw_tank_twin']:
  base()
  if name.endswith('single'):tank(0,1.05,'water')
  elif name.endswith('cascade'):
   tank(-.23,1.05,'water_committed');tank(.23,.65,'water_excess');box((0,0,1.05),(.22,.10,.12),TEAL,'overflow_spout')
  else:
   tank(-.23,.95,'water_peak');tank(.23,.95,'water_committed');beam((-.23,0,1.4),(.23,0,1.4),.08,TEAL)
 elif name=='phw_recycler':
  base();box((0,0,.4),(.7,.7,.44),TEAL);box((0,0,.66),(.86,.8,.12),ORANGE)
  box((0,0,.73),(.65,.6,.08),DARK,'hatch')
  for x in [-.2,.2]:box((x,-.36,.34),(.08,.05,.3),IVORY)
 elif name=='phw_priority_merger':
  base();box((.28,0,.47),(.22,.75,.5),IVORY)
  for y in [-.24,.24]:box((-.12,y,.27),(.65,.22,.09),TEAL)
  box((-.1,-.24,.48),(.09,.26,.34),ORANGE,'gate_priority');box((-.1,.24,.48),(.09,.26,.34),(.1,.45,.55,1),'gate_weighted')
  box((.35,0,.78),(.3,.74,.11),DARK)
 elif name in ['phw_dock_in','phw_dock_out']:
  base();color=TEAL if name.endswith('_in') else ORANGE
  for y in [-.35,.35]:box((0,y,.7),(.48,.14,1.1),IVORY)
  box((0,0,1.23),(.54,.84,.15),color)
  box((.15,0,.71),(.07,.56,.83),DARK,'door')
  for y in [-.34,.34]:box((-.32,y,.27),(.28,.06,.14),color)
 elif name.startswith('phw_crate_'):
  size={'s':.36,'m':.5,'l':.64}[name[-1]];height=size*.7
  box((0,0,height/2),(size,size*.82,height),(.66,.49,.27,1),bevel=.025)
  box((0,0,height),(size*.92,size*.75,.035),IVORY,bevel=.012)
  for x in [-size*.38,size*.38]:box((x,0,height/2),(.035,size*.84,height*.82),DARK,bevel=.005)
  for i in range(8):
   o=bpy.data.objects.new('bit_'+str(7-i),None);collection.objects.link(o)
   o.location=((-0.37+i*.105+(0.05 if i>5 else 0))*size,-.07*size,height+.025);o.empty_display_size=.025
 elif name=='phw_hall':
  box((0,0,-.22),(28,28,.35),DARK,bevel=.08)
  for x in [-13,13]:
   box((x,0,.48),(.25,27,1.2),(.23,.32,.34,1))
   for y in [-11,-5,1,7,13]:
    box((x,y,2.2),(.32,.32,4.5),IVORY);box((x,y,4.45),(.65,.7,.2),TEAL)
  box((0,13,1.35),(26,.25,2.7),(.27,.36,.38,1))
  for x in [-10,-5,0,5,10]:
   box((x,12.8,2.2),(3.7,.12,.5),(.47,.58,.6,1));box((x,12.3,.65),(1.4,1,.9),TEAL)
  for x in [-13,13]:beam((x,-11,4.5),(x,13,4.5),.15,METAL)
  beam((-13,13,4.5),(13,13,4.5),.15,METAL)
 else:raise ValueError(name)
 # Consolidate the stationary body into one draw call with per-vertex colors.
 bpy.ops.object.select_all(action='DESELECT')
 for o in static:o.select_set(True)
 bpy.context.view_layer.objects.active=static[0];bpy.ops.object.join();body=bpy.context.object;body.name='body'
 bpy.context.scene.cursor.location=(0,0,0);bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
 for o in collection.objects:
  if o.type=='MESH':
   bpy.context.view_layer.objects.active=o;o.select_set(True);bpy.ops.object.transform_apply(location=False,rotation=True,scale=True);o.data.calc_loop_triangles();o.select_set(False)
 root=bpy.data.objects.new(name,None);collection.objects.link(root)
 for o in list(collection.objects):
  if o!=root:o.parent=root
 bpy.ops.object.select_all(action='DESELECT')
 for o in collection.objects:o.select_set(True)
 bpy.context.view_layer.objects.active=body
 # Keep other user objects outside the export; no imported art is ever included.
 bpy.ops.export_scene.gltf(filepath=str(ROOT/'models'/f'{name}.glb'),export_format='GLB',use_selection=True,export_yup=True,export_cameras=False,export_lights=False)
 bpy.ops.wm.save_as_mainfile(filepath=str(ROOT/'src/blender'/f'{name}.blend'))
 stats={'asset':name,'triangles':sum(len(o.data.loop_triangles) for o in collection.objects if o.type=='MESH'),'nodes':[o.name for o in collection.objects],'meters':True}
 print('PHW_ASSET '+json.dumps(stats))
 return stats
