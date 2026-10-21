import {indiaToday, validateRequest, buildRequestMessage} from './domain.mjs';

const services = JSON.parse(document.querySelector('#service-data').textContent);
const dialog = document.querySelector('#repair-dialog');
const form = document.querySelector('#repair-form');
const panels = [...document.querySelectorAll('[data-step]')];
const error = document.querySelector('#form-error');
const status = document.querySelector('#request-status');
const picker = document.querySelector('#hero-service');
let step = 1;
let message = '';
let trigger = null;

function showStep(next) {
  step = next;
  panels.forEach(panel => panel.hidden = Number(panel.dataset.step) !== next);
  document.querySelector('#step-label').textContent = `STEP ${next} OF 3`;
  document.querySelector('#request-title').textContent = ['','What needs fixing?','How can we reach you?','Review your request'][next];
  document.querySelector('#step-progress').value = next;
  error.hidden = true;
  status.textContent = '';
  const focus = next === 1 ? form.elements.service : next === 2 ? form.elements.name : document.querySelector('#request-summary');
  requestAnimationFrame(() => focus.focus());
}
function openRequest(service, source) {
  trigger = source;
  if (service && services.some(s => s.id === service)) form.elements.service.value = service;
  else if (picker?.value) form.elements.service.value = picker.value;
  form.elements.date.min = indiaToday();
  dialog.showModal();
  document.body.classList.add('dialog-open');
  showStep(1);
}
document.querySelectorAll('[data-request]').forEach(button => button.addEventListener('click', () => openRequest(button.dataset.request, button)));
document.querySelector('[data-close]').addEventListener('click', () => dialog.close());
dialog.addEventListener('click', event => { if (event.target === dialog) {const r=dialog.getBoundingClientRect(); if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom) dialog.close();} });
dialog.addEventListener('close', () => {document.body.classList.remove('dialog-open'); trigger?.focus();});
document.querySelectorAll('[data-back]').forEach(button => button.addEventListener('click', () => showStep(step-1)));
function showError(text, field) {error.textContent=text;error.hidden=false;form.elements[field]?.focus();}
form.addEventListener('submit', event => {
  event.preventDefault();
  const data = Object.fromEntries(new FormData(form));
  if (step === 1) {
    if (!services.some(s=>s.id===data.service)) {showError('Please choose an appliance.','service');return;}
    showStep(2);return;
  }
  const issue = validateRequest(data, services.map(s=>s.id));
  if (issue) {showError(issue.message,issue.field);return;}
  const service = services.find(s => s.id === data.service);
  message = buildRequestMessage(data, service.name);
  document.querySelector('#request-summary').textContent = message;
  document.querySelector('#send-whatsapp').href = `https://wa.me/919655333511?text=${encodeURIComponent(message)}`;
  document.querySelector('#send-email').href = `mailto:rishielectronics25@gmail.com?subject=${encodeURIComponent('Repair request: '+service.name)}&body=${encodeURIComponent(message)}`;
  showStep(3);
});
document.querySelector('#send-whatsapp').addEventListener('click', () => {status.textContent='Finish sending your message in WhatsApp. Your appointment is pending staff confirmation.';});
document.querySelector('#copy-request').addEventListener('click', async () => {
  try {await navigator.clipboard.writeText(message);status.textContent='Request copied. You can paste it into a message to the workshop.';}
  catch {const summary=document.querySelector('#request-summary');const range=document.createRange();range.selectNodeContents(summary);const selection=window.getSelection();selection.removeAllRanges();selection.addRange(range);status.textContent='Select and copy the request above, or use WhatsApp or email.';}
});
picker?.addEventListener('change', () => {form.elements.service.value=picker.value;});

const menuButton = document.querySelector('#menu-button');
const nav = document.querySelector('#main-nav');
function closeMenu(){menuButton.setAttribute('aria-expanded','false');nav.classList.remove('is-open');}
menuButton.addEventListener('click',()=>{const open=menuButton.getAttribute('aria-expanded')!=='true';menuButton.setAttribute('aria-expanded',String(open));nav.classList.toggle('is-open',open);});
nav.querySelectorAll('a').forEach(link=>link.addEventListener('click',closeMenu));
document.addEventListener('keydown',event=>{if(event.key==='Escape'&&menuButton.getAttribute('aria-expanded')==='true'){closeMenu();menuButton.focus();}});
document.addEventListener('click',event=>{if(!nav.contains(event.target)&&!menuButton.contains(event.target))closeMenu();});

const sections = document.querySelectorAll('main > section[id]');
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => entries.forEach(entry=>{if(entry.isIntersecting){document.querySelectorAll('[data-nav]').forEach(a=>{const active=a.dataset.nav===entry.target.id;a.classList.toggle('active',active);if(active)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current');});}}),{rootMargin:'-15% 0px -60% 0px'});
  sections.forEach(section=>observer.observe(section));
}
