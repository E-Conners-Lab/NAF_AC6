import {chromium} from 'playwright';
import {readFileSync,writeFileSync} from 'node:fs';
import assert from 'node:assert/strict';
import {compileFactory} from '../../engine/factory.js';
import {runWorkOrder,runSimulation} from '../../engine/sim.js';
import {predictionAnswers} from '../../engine/grader.js';
const json=p=>JSON.parse(readFileSync(p));
const levels=json('data/levels.json'),defs=json('data/machines.json');
const browser=await chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
const mode=process.argv[2]??'schematic';
const page=await browser.newPage({viewport:{width:1920,height:1080}}),errors=[],records=[];
page.on('pageerror',e=>errors.push(e.message));page.on('console',m=>{if(m.type()==='error')errors.push(m.text());});
async function tabTo(target){await target.waitFor({state:'visible'});for(let i=0;i<500;i++){if(await target.evaluate(e=>e===document.activeElement))return;await page.keyboard.press('Tab');}throw Error('Cannot reach with Tab: '+await target.textContent());}
async function press(target){await tabTo(target);await page.keyboard.press('Enter');}
async function type(target,value){await tabTo(target);await page.keyboard.press('Meta+A');await page.keyboard.type(String(value));assert.equal(await target.inputValue(),String(value),'Typed value must remain in focused field');}
async function selectMachine(x,y){await tabTo(page.locator('#floor'));const [cx,cy]=(await page.locator('#cursor-status').innerText()).match(/\d+/g).map(Number);for(let i=0;i<Math.abs(x-cx);i++)await page.keyboard.press(x>cx?'ArrowRight':'ArrowLeft');for(let i=0;i<Math.abs(y-cy);i++)await page.keyboard.press(y>cy?'ArrowDown':'ArrowUp');await page.keyboard.press('Enter');}
async function setBits(dscp){for(const bit of [32,16,8,4,2,1]){const b=page.getByRole('button',{name:'DSCP weight '+bit,exact:true});if((await b.getAttribute('aria-pressed')==='true')!==Boolean(dscp&bit))await press(b);}await press(page.getByRole('button',{name:'Apply configuration'}));}
async function speed8(){await tabTo(page.locator('#speed'));for(let i=0;i<6;i++)await page.keyboard.press('ArrowDown');await page.keyboard.press('Tab');assert.equal(await page.locator('#speed').inputValue(),'8');}
async function run(expectPass){await press(page.locator('#run-button'));await page.locator('.grade-pill').waitFor({timeout:15000});assert.equal(await page.locator('.grade-pill').evaluate(e=>e.classList.contains('pass')),expectPass);}
try{
 await page.goto('http://localhost:8000');await press(page.getByRole('button',{name:'Continue campaign'}));await press(page.getByRole('button',{name:'Open the work order'}));
 await press(page.locator(mode==='3d'?'#view-3d':'#view-schematic'));assert.equal(await page.evaluate(()=>perHopDiagnostics().view),mode);assert.equal(await page.locator('[data-level="L02"]').isDisabled(),true);await speed8();await run(false);
 records.push({test:'initial incorrect L01 fails without unlocking L02',passed:await page.locator('[data-level="L02"]').isDisabled()});
 for(const l of levels){
  if(l.id!=='L01'){await press(page.locator(`[data-level="${l.id}"]`));await press(page.getByRole('button',{name:'Open the work order'}));}
  assert.equal(await page.evaluate(()=>perHopDiagnostics().view),mode,l.id+' must stay in selected view');const ref=json('data/'+l.reference_solution);
  if(l.id==='L01'){await selectMachine(5,4);await type(page.getByLabel('Match value').first(),46);await press(page.getByRole('button',{name:'Apply configuration'}));}
  if(['L02','L04','L05'].includes(l.id)){for(const m of ref.machines.filter(m=>m.type==='paint_booth')){await selectMachine(m.x,m.y);await setBits(m.config.dscp);}}
  if(l.predictions?.length){const graph=compileFactory(l,ref,defs).graph,result=runWorkOrder(l,graph,json('data/'+l.work_order.trace),{},defs);const answers=predictionAnswers(l,result);for(const q of l.predictions)await type(page.locator('#prediction-'+q.id),answers[q.id]);}
  if(Number(l.id.slice(1))>=6){for(const target of ref.machines){const current=l.initial_factory.machines.find(m=>m.id===target.id);if(JSON.stringify(current.config)===JSON.stringify(target.config))continue;await selectMachine(target.x,target.y);for(const [key,value]of Object.entries(target.config)){if(JSON.stringify(current.config[key])===JSON.stringify(value))continue;if(key==='dscp'){await setBits(value);continue;}if(key==='thresholds'){for(const [name,range]of Object.entries(value))for(let i=0;i<2;i++)await type(page.locator(`[data-threshold="${name}"][data-end="${i}"]`),range[i]);}else if(key==='weights'){for(const [name,weight]of Object.entries(value))await type(page.locator(`[data-weight="${name}"]`),weight);}else{const input=page.locator(`#machine-form [name="${key}"]`);if(await input.evaluate(e=>e.tagName==='SELECT')){await tabTo(input);await page.keyboard.press('Home');const at=await input.evaluate((e,v)=>[...e.options].findIndex(o=>o.value===v),value);for(let i=0;i<at;i++)await page.keyboard.press('ArrowDown');await page.keyboard.press('Tab');}else await type(input,value);}}await press(page.getByRole('button',{name:'Apply configuration'}));}}
  await run(true);const render=await page.evaluate(()=>perHopDiagnostics().render);if(mode==='3d')assert.ok(render,l.id+' must remain in 3D');if(render)assert.ok(render.maxDrawCalls<=150,JSON.stringify(render));const first=await page.evaluate(()=>perHopDiagnostics().grade);await press(page.locator(mode==='3d'?'#view-schematic':'#view-3d'));assert.deepEqual(await page.evaluate(()=>perHopDiagnostics().grade),first);await press(page.locator(mode==='3d'?'#view-3d':'#view-schematic'));await page.screenshot({path:`research/browser/${l.id}-${mode}-keyboard.png`,fullPage:true});records.push({level:l.id,keyboard_only:true,checks:await page.locator('.grade-pill').innerText(),passed:true,render});
 }
 // Inspect a crate and seek one event with keyboard controls.
 await press(page.locator('[data-inspect-arrival]').first());await press(page.locator('[data-seek]').last());assert.ok(await page.locator('#inspector').innerText());records.push({test:'Crate Trace keyboard event seeking',passed:true});
 await page.reload();await page.getByRole('button',{name:'Continue campaign'}).waitFor();const save=await page.evaluate(()=>JSON.parse(localStorage.getItem('perhopworks:v1')));assert.equal(save.completed.length,levels.length);records.push({test:'reload preserves all earned unlocks and drafts',passed:true});
 assert.deepEqual(errors,[]);console.log(JSON.stringify({records,errors},null,2));
 writeFileSync(`research/browser/keyboard-${mode}.json`,JSON.stringify({records,errors,at:new Date().toISOString()},null,2));
}catch(e){console.error(await page.evaluate(()=>perHopDiagnostics()));console.error(await page.locator('#dashboard').innerText());await page.screenshot({path:'research/browser/keyboard-failure.png',fullPage:true});console.error(e);process.exitCode=1;}finally{await browser.close();}
