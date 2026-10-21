import test from 'node:test';
import assert from 'node:assert/strict';
import {normalizeIndianPhone, indiaToday, validateRequest, buildRequestMessage} from '../dist/domain.mjs';

test('accepts common Indian mobile formats while rejecting incomplete and international numbers', () => {
  for (const value of ['9655333511','+91 96553 33511','91-96553-33511']) assert.equal(normalizeIndianPhone(value),'+919655333511');
  for (const value of ['','12345','+44 7700 900123','0655333511','919655333511123']) assert.equal(normalizeIndianPhone(value),null);
});
test('calendar date follows India across the UTC midnight boundary', () => {
  assert.equal(indiaToday(new Date('2026-10-20T18:29:59Z')),'2026-10-20');
  assert.equal(indiaToday(new Date('2026-10-20T18:30:00Z')),'2026-10-21');
  assert.equal(indiaToday(new Date('2026-10-21T00:01:00Z')),'2026-10-21');
});
test('validates a real service, contact and date before preparing a request', () => {
  const now=new Date('2026-10-20T20:00:00Z');
  const base={service:'ro-repair',name:'Customer',phone:'+91 98765 43210',date:'2026-10-21'};
  assert.equal(validateRequest(base,['tv','ro-repair'],now),null);
  assert.equal(validateRequest({...base,date:''},['ro-repair'],now),null);
  assert.equal(validateRequest({...base,service:'unknown'},['ro-repair'],now).field,'service');
  assert.equal(validateRequest({...base,date:'2026-10-20'},['ro-repair'],now).field,'date');
  assert.equal(validateRequest({...base,date:'2027-02-30'},['ro-repair'],now).field,'date');
  assert.equal(validateRequest({...base,name:'  '},['ro-repair'],now).field,'name');
  assert.equal(validateRequest({...base,phone:'123'},['ro-repair'],now).field,'phone');
});
test('WhatsApp draft preserves customer information without claiming a confirmed appointment', () => {
  const message=buildRequestMessage({name:' Test Customer ',phone:'9876543210',problem:' No cooling & making noise ',date:'2026-10-22',time:'9 AM – 12 PM'},'Refrigerator Repair');
  assert.match(message,/Appliance: Refrigerator Repair/);
  assert.match(message,/Name: Test Customer/);
  assert.match(message,/Mobile: \+919876543210/);
  assert.match(message,/Problem: No cooling & making noise/);
  assert.match(message,/Preferred date: 2026-10-22/);
  assert.match(message,/Please contact me to confirm availability/);
  assert.equal(decodeURIComponent(encodeURIComponent(message)),message);
});
