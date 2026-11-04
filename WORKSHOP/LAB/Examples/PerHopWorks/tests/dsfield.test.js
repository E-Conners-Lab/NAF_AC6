import test from 'node:test';
import assert from 'node:assert/strict';
import {splitOctet, joinOctet, nameToDscp, dscpName, precedence, markOctet} from '../engine/dsfield.js';
test('all octets round trip; marking preserves ECN',()=>{for(let n=0;n<256;n++){const {dscp,ecn}=splitOctet(n);assert.equal(joinOctet(dscp,ecn),n);assert.equal(splitOctet(markOctet(n,34)).ecn,ecn);}});
test('supplied codepoint/octets/precedence fixtures',()=>{assert.deepEqual(splitOctet(0xb8),{dscp:46,ecn:0});assert.deepEqual(splitOctet(0xb9),{dscp:46,ecn:1});assert.equal(precedence(34),4);assert.equal(precedence(46),5);assert.equal(nameToDscp('EF'),46);assert.equal(nameToDscp('DF'),0);for(let x=0;x<=7;x++)assert.equal(nameToDscp(`CS${x}`),8*x);for(let x=1;x<=4;x++)for(let y=1;y<=3;y++){assert.equal(nameToDscp(`AF${x}${y}`),8*x+2*y);assert.equal(dscpName(8*x+2*y),`AF${x}${y}`);}});
test('invalid octets and codepoints never truncate',()=>{for(const n of [-1,256,NaN,1.5,'46'])assert.throws(()=>splitOctet(n));assert.throws(()=>nameToDscp('AF45'));assert.throws(()=>joinOctet(64,0));});
