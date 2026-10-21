export const PHONE = '+919655333511';
export function normalizeIndianPhone(value) {
  const digits = String(value).replace(/[^0-9]/g, '');
  const local = digits.length === 12 && digits.startsWith('91') ? digits.slice(2) : digits;
  return /^[6-9][0-9]{9}$/.test(local) ? '+91' + local : null;
}
export function indiaToday(now = new Date()) {
  const parts = new Intl.DateTimeFormat('en-GB', {timeZone:'Asia/Kolkata',year:'numeric',month:'2-digit',day:'2-digit'}).formatToParts(now);
  const get = type => parts.find(p => p.type === type).value;
  return `${get('year')}-${get('month')}-${get('day')}`;
}
export function validateRequest(data, serviceIds, now = new Date()) {
  if (!serviceIds.includes(data.service)) return {field:'service', message:'Please choose an appliance.'};
  if (!String(data.name || '').trim()) return {field:'name', message:'Please enter your name.'};
  if (!normalizeIndianPhone(data.phone || '')) return {field:'phone', message:'Enter a valid Indian mobile number, with or without +91.'};
  if (data.date) {
    const parsed = new Date(data.date + 'T00:00:00Z');
    if (!/^\d{4}-\d{2}-\d{2}$/.test(data.date) || Number.isNaN(parsed.getTime()) || parsed.toISOString().slice(0,10) !== data.date || data.date < indiaToday(now)) return {field:'date', message:'Choose today or a future date.'};
  }
  return null;
}
export function buildRequestMessage(data, serviceName) {
  const lines = ['Hello Rishi Electronics, I would like to request a repair.', '', `Appliance: ${serviceName}`, `Name: ${data.name.trim()}`, `Mobile: ${normalizeIndianPhone(data.phone)}`];
  if (data.problem.trim()) lines.push(`Problem: ${data.problem.trim()}`);
  if (data.date) lines.push(`Preferred date: ${data.date}`);
  if (data.time) lines.push(`Preferred time: ${data.time}`);
  lines.push('', 'Please contact me to confirm availability and the next steps.');
  return lines.join('\n');
}
