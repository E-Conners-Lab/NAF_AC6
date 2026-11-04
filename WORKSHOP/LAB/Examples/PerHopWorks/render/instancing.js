import {classAppearance,patternInk} from './classStyle.js';
import * as THREE from 'three';
import {mergeGeometries} from 'three/addons/utils/BufferGeometryUtils.js';
import {cratePosition} from './schematic.js';
function bodyGeometry(model){model.updateMatrixWorld(true);const body=model.getObjectByName('body');return body.geometry.clone().applyMatrix4(body.matrixWorld);}
function patternGeometry(pattern){const pieces=[];function bar(x,z,w,d,angle=0){const g=new THREE.BoxGeometry(w,.005,d);g.rotateY(angle);g.translate(x,0,z);pieces.push(g);}const dot=(x,z,r=.025)=>{const g=new THREE.CylinderGeometry(r,r,.006,8);g.translate(x,0,z);pieces.push(g);};
 if(pattern==='dots'){dot(-.1,.07);dot(0,.14);dot(.1,.07);}
 else if(pattern==='cross'){bar(0,.1,.25,.02);bar(0,.1,.02,.15);}
 else if(pattern==='diagonal'){bar(-.07,.1,.02,.21,.6);bar(.07,.1,.02,.21,.6);}
 else if(pattern==='chevron'){bar(-.05,.08,.14,.02,-.55);bar(.05,.08,.14,.02,.55);bar(-.05,.15,.14,.02,-.55);bar(.05,.15,.14,.02,.55);}
 else if(pattern==='checker'){bar(-.08,.06,.07,.06);bar(.02,.13,.07,.06);}
 else if(pattern==='rings'){const g=new THREE.TorusGeometry(.075,.012,4,12);g.rotateX(Math.PI/2);g.translate(0,0,.1);pieces.push(g);}
 else if(pattern==='diamond'){for(const s of [-1,1]){bar(s*.06,.05,.13,.016,s*.65);bar(s*.06,.15,.13,.016,-s*.65);}}
 else if(pattern==='horizontal'||pattern==='waves'){bar(0,.05,.25,.018);bar(0,.13,.25,.018);if(pattern==='waves')bar(.05,.09,.018,.12);}
 else if(['bars','vertical'].includes(pattern)){for(const x of pattern==='bars'?[-.1,0,.1]:[-.07,.07])bar(x,.1,.018,.15);}
 else bar(0,.13,.23,.015);
 const geometry=mergeGeometries(pieces);pieces.forEach(g=>g.dispose());return geometry;
}
export function createCrateInstances(models,scene,max=1200){const dummy=new THREE.Object3D(),color=new THREE.Color(),meshes={},sockets={},heights={},patterns={};
 for(const size of ['s','m','l']){const model=models['phw_crate_'+size],body=model.getObjectByName('body'),mesh=new THREE.InstancedMesh(bodyGeometry(model),body.material.clone(),max);mesh.instanceMatrix.setUsage(THREE.DynamicDrawUsage);mesh.count=0;mesh.castShadow=true;mesh.frustumCulled=false;mesh.userData.crateIds=[];scene.add(mesh);meshes[size]=mesh;sockets[size]=Array.from({length:8},(_,i)=>model.getObjectByName('bit_'+(7-i)).getWorldPosition(new THREE.Vector3()));heights[size]=sockets[size][0].y;}
 const lights=new THREE.InstancedMesh(new THREE.BoxGeometry(1,1,1),new THREE.MeshBasicMaterial(),max*8);lights.count=0;lights.frustumCulled=false;lights.instanceMatrix.setUsage(THREE.DynamicDrawUsage);scene.add(lights);
 function update(snapshot,graph,tick,classes){const counts={s:0,m:0,l:0},patternCounts={};let lamp=0;for(const c of (snapshot?.crates??[]).slice(0,max)){const size=c.size<=600?'s':c.size<=1200?'m':'l',mesh=meshes[size],index=counts[size]++,p=cratePosition(c,graph,tick);dummy.position.set(p.x,.19,p.y);dummy.rotation.set(0,0,0);dummy.scale.setScalar(1);dummy.updateMatrix();mesh.setMatrixAt(index,dummy.matrix);const appearance=classAppearance(c.class,classes);mesh.setColorAt(index,color.set(appearance.color));mesh.userData.crateIds[index]=c.id;
  for(let bit=0;bit<8;bit++){const socket=sockets[size][bit],on=(c.octet>>(7-bit))&1;dummy.position.set(p.x+socket.x,.19+socket.y,p.y+socket.z);const width=bit>5?.018:.027;dummy.scale.set(width,.016,bit>5?.025:.042);dummy.updateMatrix();lights.setMatrixAt(lamp,dummy.matrix);lights.setColorAt(lamp++,color.set(on?'#fffac1':'#162b34'));}
  const pattern=appearance.pattern;if(!patterns[pattern]){const m=new THREE.InstancedMesh(patternGeometry(pattern),new THREE.MeshBasicMaterial({color:'#ffffff'}),max);m.frustumCulled=false;m.count=0;scene.add(m);patterns[pattern]=m;}const pi=patternCounts[pattern]??0;patternCounts[pattern]=pi+1;dummy.position.set(p.x,.19+heights[size]-.008,p.y);dummy.scale.setScalar(size==='s'?.7:size==='l'?1.2:1);dummy.updateMatrix();patterns[pattern].setMatrixAt(pi,dummy.matrix);patterns[pattern].setColorAt(pi,color.set(patternInk(appearance.color)));
 }
 for(const [size,m]of Object.entries(meshes)){m.count=counts[size];m.instanceMatrix.needsUpdate=true;if(m.instanceColor)m.instanceColor.needsUpdate=true;}lights.count=lamp;lights.instanceMatrix.needsUpdate=true;if(lights.instanceColor)lights.instanceColor.needsUpdate=true;for(const [p,m]of Object.entries(patterns)){m.count=patternCounts[p]??0;m.instanceMatrix.needsUpdate=true;if(m.instanceColor)m.instanceColor.needsUpdate=true;}}
 return {update,pickables:Object.values(meshes),dispose(){for(const m of [...Object.values(meshes),lights,...Object.values(patterns)]){scene.remove(m);m.geometry.dispose();m.material.dispose();}}};}
