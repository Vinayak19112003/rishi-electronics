"""Generate a buildless service website from the collected business catalogue."""
from pathlib import Path
import json, html, shutil
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent
DIST = ROOT / 'dist'
SOURCE = ROOT / 'research'
ORIGIN = 'https://rishi-electronics-repairs.candidhill128.chatgpt.site'
business = json.loads((SOURCE / 'business.json').read_text())
services = json.loads((SOURCE / 'services.json').read_text())
esc = html.escape
short_names = ['TV', 'Laptop', 'Mobile', 'Home Theater', 'Inverter / UPS', 'Washing Machine', 'Refrigerator', 'Air Conditioner', 'RO Purifier']
assets = DIST / 'assets'
assets.mkdir(exist_ok=True)
logo = Image.open(SOURCE / 'assets/header-logo.jpg').convert('RGB')
logo.resize((480, 235), Image.Resampling.LANCZOS).save(assets / 'rishi-original-logo.webp', 'WEBP', quality=94, method=6)
favicon = ImageOps.contain(Image.open(SOURCE / 'assets/favicon-online.png').convert('RGB'), (64,64), Image.Resampling.LANCZOS)
favicon_canvas = Image.new('RGB',(64,64),'black')
favicon_canvas.paste(favicon, ((64-favicon.width)//2,(64-favicon.height)//2))
favicon_canvas.save(assets / 'rishi-original-favicon.png')
for s, short in zip(services, short_names):
    s['short_name'] = short
    im = Image.open(SOURCE / s['image']).convert('RGB')
    im.thumbnail((520, 360), Image.Resampling.LANCZOS)
    s['delivery_image'] = f"/assets/{s['id']}.webp"
    im.save(DIST / s['delivery_image'].lstrip('/'), 'WEBP', quality=86, method=6)
im = Image.open(SOURCE / 'assets/shop-front.jpg').convert('RGB')
im.save(assets / 'workshop.webp', 'WEBP', quality=86, method=6)
hero_source = SOURCE / 'assets/appliances-original.png'
im = Image.open(hero_source).convert('RGB')
im.thumbnail((1100,800),Image.Resampling.LANCZOS)
im.save(assets / 'appliances.webp', 'WEBP', quality=86, method=6)
im.thumbnail((620,450),Image.Resampling.LANCZOS)
im.save(assets / 'appliances-small.webp', 'WEBP', quality=84, method=6)

paths = {
    'chip': '<rect x="6" y="6" width="20" height="20" rx="3"/><rect x="11" y="11" width="10" height="10" rx="1"/>' + ''.join(f'<path d="M{n} 2v4M{n} 26v4M2 {n}h4M26 {n}h4"/>' for n in [11,16,21]),
    'phone': '<path d="M7 3H4a1 1 0 0 0-1 1c0 9.4 7.6 17 17 17a1 1 0 0 0 1-1v-3l-5-2-2 2a14 14 0 0 1-7-7l2-2-2-5Z"/>',
    'whatsapp': '<path d="M21 11.5a9 9 0 0 1-13.6 7.8L3 21l1.6-4.5A9 9 0 1 1 21 11.5Z"/><path d="m8.5 7 1.3 2.4-.8 1a8 8 0 0 0 3.6 3.6l1-.8 2.4 1.3c-.4 2.8-3.5 1.9-5.5.6S6.8 9 8.5 7Z"/>',
    'pin': '<path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/>',
    'arrow': '<path d="M5 12h14m-6-6 6 6-6 6"/>',
    'chevron': '<path d="m9 5 7 7-7 7"/>',
    'wrench': '<path d="M21 3a6 6 0 0 1-7.6 7.6L6 18a2.1 2.1 0 0 1-3-3l7.4-7.4A6 6 0 0 1 18 0l-4 4 2 2 5-3Z" transform="translate(0 1) scale(.95)"/>',
    'message': '<path d="M21 11a9 9 0 0 1-9 9 9 9 0 0 1-4-.9L3 21l1.7-4.8A9 9 0 1 1 21 11Z"/><path d="M8 10h8M8 13h5"/>',
    'clipboard': '<rect x="6" y="4" width="12" height="17" rx="2"/><rect x="9" y="2" width="6" height="4" rx="1"/><path d="M9 11h6M9 15h4"/>',
    'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 6 9 7 9-7"/>',
    'menu': '<path d="M4 6h16M4 12h16M4 18h16"/>',
    'close': '<path d="m6 6 12 12M18 6 6 18"/>',
}
def icon(name, cls=''):
    view = '0 0 32 32' if name == 'chip' else '0 0 24 24'
    return f'<svg viewBox="{view}" aria-hidden="true" class="{cls}">{paths[name]}</svg>'

def brand():
    return '<a class="brand" href="/" aria-label="Rishi Electronics home"><img class="brand-logo" src="/assets/rishi-original-logo.webp" alt="Rishi Electronics original logo" width="480" height="235"><span class="brand-location">Palayamkottai,<br>Tirunelveli</span></a>'

def header():
    return f'''<a href="#main" class="skip">Skip to content</a><header class="site-header"><div class="wrap header-inner">{brand()}
    <nav id="main-nav" aria-label="Main navigation"><a href="/#home" data-nav="home" class="active">Home</a><a href="/#services" data-nav="services">Services</a><a href="/#how-it-works" data-nav="how-it-works">How it works</a><a href="/#visit-us" data-nav="visit-us">Visit us</a></nav>
    <a class="header-call" href="tel:+919655333511">{icon('phone')}<span>+91 96553 33511</span></a>
    <button class="menu-button" id="menu-button" aria-label="Open navigation" aria-expanded="false" aria-controls="main-nav">{icon('menu')}</button></div></header>'''

def footer():
    return f'''<footer class="footer"><div class="wrap"><div class="footer-top">{brand()}<div class="footer-links"><a href="/#services">Our services</a><a href="/privacy/">Privacy</a><a href="/terms/">Service enquiries</a><a href="mailto:rishielectronics25@gmail.com">Email us</a></div></div><div class="footer-bottom"><span>© 2026 Rishi Electronics.</span><span>Electronics &amp; appliance repairs in Palayamkottai.</span></div></div></footer>
    <div class="mobile-contact-bar" aria-label="Quick contact"><a class="button primary" href="tel:+919655333511">{icon('phone')}Call now</a><a class="button green" href="https://wa.me/919655333511" target="_blank" rel="noopener noreferrer">{icon('whatsapp')}WhatsApp</a></div>'''

options = '<option value="">Select an appliance</option>' + ''.join(f'<option value="{s["id"]}">{esc(s["short_name"])}</option>' for s in services)

def request_dialog():
    return f'''<dialog id="repair-dialog" aria-labelledby="request-title" aria-describedby="request-intro"><div class="dialog-top"><span class="eyebrow" id="step-label">STEP 1 OF 3</span><button class="close-button" data-close aria-label="Close repair request">{icon('close')}</button></div>
    <h2 id="request-title">What needs fixing?</h2><p class="intro" id="request-intro">A few details will help us understand your repair.</p><progress class="progress" id="step-progress" value="1" max="3" aria-label="Request progress"></progress>
    <form id="repair-form" novalidate><p id="form-error" class="error-message" role="alert" hidden></p>
    <div data-step="1"><label class="field"><span class="field-label">Choose your appliance</span><select name="service" required>{options}</select></label><label class="field"><span class="field-label">What is the problem? <span class="optional">(optional)</span></span><textarea name="problem" maxlength="1400" rows="4" placeholder="For example: not turning on, no display, leaking or making a noise."></textarea></label><div class="dialog-actions"><button class="button primary" type="submit">Continue {icon('arrow')}</button></div><p class="dialog-note">{icon('message')}Your request is prepared here. You choose when to send it in WhatsApp or email.</p></div>
    <div data-step="2" hidden><label class="field"><span class="field-label">Your name</span><input name="name" autocomplete="name" maxlength="80" required placeholder="Full name"></label><label class="field"><span class="field-label">Mobile number</span><input name="phone" type="tel" autocomplete="tel" inputmode="tel" maxlength="20" required placeholder="Your 10-digit mobile number"><small>You can include +91 and spaces.</small></label><div class="field-row"><label class="field"><span class="field-label">Preferred date <span class="optional">(optional)</span></span><input name="date" type="date"></label><label class="field"><span class="field-label">Preferred time <span class="optional">(optional)</span></span><select name="time"><option value="">No preference</option><option>9 AM – 12 PM</option><option>12 PM – 4 PM</option><option>4 PM – 7 PM</option></select></label></div><p class="dialog-note">{icon('clock')}Dates and times are preferences. Our team will confirm availability. Sunday is by appointment.</p><div class="dialog-actions"><button class="button" type="button" data-back>Back</button><button class="button primary" type="submit">Review request {icon('arrow')}</button></div><p class="dialog-note">Your details stay in this page until you choose to share them. Read our <a href="/privacy/" target="_blank" rel="noopener">privacy notice</a>.</p></div>
    <div data-step="3" hidden><p class="review-hint">Your message is ready. Open WhatsApp, review the message and tap send there. The workshop will confirm the next steps.</p><pre id="request-summary" class="review-summary" tabindex="-1" aria-label="Your repair request"></pre><a id="send-whatsapp" class="button green send-button" href="https://wa.me/919655333511" target="_blank" rel="noopener noreferrer">{icon('whatsapp')}Continue to WhatsApp {icon('arrow')}</a><div class="review-alternatives"><button type="button" data-back class="link-button">Edit details</button><button type="button" id="copy-request" class="link-button">Copy request</button><a id="send-email" class="link-button" href="mailto:rishielectronics25@gmail.com">Use email instead</a></div><p class="dialog-note">No appointment is reserved until our team confirms it. If you need help, <a href="tel:+919655333511">call the workshop</a>.</p></div><p id="request-status" class="request-status" role="status" aria-live="polite"></p></form></dialog>'''

def document(title, description, body, path='/'):
    schema = {'@context':'https://schema.org','@type':'LocalBusiness','name':business['name'],'url':ORIGIN,'telephone':business['contact']['phone_e164'],'email':business['contact']['email'],'address':{'@type':'PostalAddress','streetAddress':'H107, Kamarajar Salai, Anbunagar, Maharaja Nagar','addressLocality':'Palayamkottai, Tirunelveli','addressRegion':'Tamil Nadu','postalCode':'627011','addressCountry':'IN'},'openingHoursSpecification':[{'@type':'OpeningHoursSpecification','dayOfWeek':['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'],'opens':'09:00','closes':'20:00'}]}
    return f'''<!doctype html><html lang="en-IN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#006575"><title>{esc(title)}</title><meta name="description" content="{esc(description)}"><link rel="canonical" href="{ORIGIN}{path}"><meta property="og:type" content="website"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:url" content="{ORIGIN}{path}"><meta property="og:image" content="{ORIGIN}/assets/appliances.webp"><meta name="twitter:card" content="summary_large_image"><link rel="icon" href="/assets/rishi-original-favicon.png" type="image/png"><link rel="stylesheet" href="/styles.css?v=original-logo-20261021"><script type="application/ld+json">{json.dumps(schema)}</script></head><body>{header()}{body}{footer()}{request_dialog()}<script id="service-data" type="application/json">{json.dumps([{'id':s['id'],'name':s['name']} for s in services]).replace('<','&lt;')}</script><script type="module" src="/app.js"></script><noscript><div class="wrap"><p>Please call <a href="tel:+919655333511">+91 96553 33511</a> or <a href="https://wa.me/919655333511">contact us on WhatsApp</a> to request a repair.</p></div></noscript></body></html>'''

def service_card(s):
    small = ' small-source' if s['id'] in ['home-theater','inverter','ro-repair'] else ''
    return f'''<a class="service-card" href="/services/{s['suggested_page_slug']}/" aria-label="{esc(s['name'])} — view service details"><div class="service-image{small}"><img src="{s['delivery_image']}" alt="{esc(s['short_name'])}" width="260" height="136" decoding="async"></div><div class="service-caption"><h3>{esc(s['short_name'])}</h3><span class="card-arrow">{icon('chevron')}</span></div></a>'''

cards = ''.join(service_card(s) for s in services)
home = f'''<main id="main"><section id="home" class="wrap hero" aria-labelledby="hero-title"><div class="hero-copy"><p class="eyebrow">YOUR LOCAL REPAIR WORKSHOP</p><h1 id="hero-title">What needs fixing?</h1><p class="hero-lead">Choose your appliance. Tell us the problem.</p><label class="mobile-selector"><span class="field-label" hidden>Choose your appliance</span><select id="hero-service" aria-label="Choose your appliance">{options}</select></label><div class="hero-actions"><button class="button primary" data-request>{icon('wrench')}Request a repair {icon('arrow','arrow')}</button><a class="button" href="tel:+919655333511">{icon('phone')}Call now</a><a class="button whatsapp" href="https://wa.me/919655333511" target="_blank" rel="noopener noreferrer">{icon('whatsapp')}WhatsApp</a></div><p class="hero-note">{icon('clipboard')}<span>Send a request</span>{icon('chevron','tiny-arrow')}{icon('message')}<span>Our team confirms</span></p></div><div class="hero-visual" aria-hidden="true"><img src="/assets/appliances.webp" srcset="/assets/appliances-small.webp 620w, /assets/appliances.webp 1100w" sizes="(max-width:600px) 1px, 50vw" width="1100" height="733" alt="" fetchpriority="high"></div></section>
    <section class="wrap services-section" id="services" aria-labelledby="services-title"><div class="section-head"><div><p class="eyebrow">ELECTRONICS &amp; HOME APPLIANCES</p><h2 id="services-title">Our services</h2></div><p class="section-hint">Choose an appliance to get started</p></div><div class="service-grid">{cards}</div></section>
    <div class="wrap visit-strip">{icon('pin')}<div><h2>Visit our workshop</h2><p>Rishi Electronics · Palayamkottai, Tirunelveli</p></div><a class="button" href="{business['maps']['published_directions_url']}" target="_blank" rel="noopener noreferrer" aria-label="Get directions to Rishi Electronics">{icon('pin')}Get directions {icon('arrow','arrow')}</a></div>
    <section class="wrap process-section" id="how-it-works" aria-labelledby="process-title"><p class="eyebrow">A SIMPLE START</p><h2 id="process-title">From a problem to a conversation.</h2><div class="process-grid"><div class="process-item"><span class="step-number">01</span><div><h3>Choose your appliance</h3><p>Find your device or appliance in our service list.</p></div></div><div class="process-item"><span class="step-number">02</span><div><h3>Tell us what’s wrong</h3><p>Describe the problem and share your preferred date, if you have one.</p></div></div><div class="process-item"><span class="step-number">03</span><div><h3>Speak with our team</h3><p>Send your request on WhatsApp or call us. Our team confirms the next steps.</p></div></div></div></section>
    <section class="workshop-section" id="visit-us" aria-labelledby="workshop-title"><div class="wrap workshop-grid"><img class="workshop-photo" src="/assets/workshop.webp" alt="Published exterior photograph of the Rishi Electronics location" width="680" height="306" loading="lazy"><div class="workshop-copy"><p class="eyebrow">RIGHT HERE IN PALAYAMKOTTAI</p><h2 id="workshop-title">Let’s get it looked at.</h2><div class="contact-line">{icon('pin')}<address>H107, Kamarajar Salai,<br>Anbunagar, Maharaja Nagar,<br>Palayamkottai, Tirunelveli,<br>Tamil Nadu 627011</address></div><div class="contact-line">{icon('clock')}<p><strong>Monday – Saturday: 9 AM – 8 PM</strong><br>Sunday: by appointment</p></div><div class="contact-line">{icon('phone')}<a href="tel:+919655333511">+91 96553 33511</a></div><div class="contact-line">{icon('mail')}<a href="mailto:rishielectronics25@gmail.com">rishielectronics25@gmail.com</a></div><div class="workshop-actions"><a class="button primary" href="{business['maps']['published_directions_url']}" target="_blank" rel="noopener noreferrer">{icon('pin')}Get directions {icon('arrow','arrow')}</a><a class="button" href="tel:+919655333511">{icon('phone')}Call the workshop</a></div></div></div></section>
    <section class="wrap faq-section" aria-labelledby="faq-title"><div class="faq-intro"><p class="eyebrow">BEFORE YOU GET IN TOUCH</p><h2 id="faq-title">A little clarity helps.</h2><p>Have another question? Talk directly with the workshop.</p><a class="text-link" href="tel:+919655333511">Call +91 96553 33511 {icon('arrow')}</a></div><div class="faq-list"><details><summary>Does a repair request confirm my appointment?</summary><p>No. Your message starts an enquiry. The workshop will confirm availability, timing and the next steps directly with you.</p></details><details><summary>How much will the repair cost?</summary><p>Ask the workshop about diagnosis charges, parts and an estimate for your appliance. Prices and warranty terms are not published here.</p></details><details><summary>Can I ask about a home visit or pickup?</summary><p>Yes. Call or message the workshop with your locality and appliance details to check whether a home visit or pickup is available for your request.</p></details><details><summary>What information should I have ready?</summary><p>Your appliance type, brand and model if known, a short description of the fault, and a way to reach you. Do not share passwords, payment information or private device contents in your enquiry.</p></details></div></section></main>'''
(DIST / 'index.html').write_text(document('Rishi Electronics | Appliance & Electronics Repair in Tirunelveli','Choose from nine electronics and appliance repair services in Palayamkottai, Tirunelveli. Call, WhatsApp or prepare a repair request.', home))

for s in services:
    path=f"/services/{s['suggested_page_slug']}/"
    content=f'''<main id="main" class="wrap"><div class="breadcrumb"><a href="/">Home</a><span>/</span><a href="/#services">Services</a><span>/</span><span>{esc(s['short_name'])}</span></div><section class="detail-hero"><div><p class="eyebrow">PALAYAMKOTTAI · TIRUNELVELI</p><h1>{esc(s['name'])}</h1><p>{esc(s['draft_description'])}</p><button class="button primary" data-request="{s['id']}">{icon('wrench')}Request a repair {icon('arrow','arrow')}</button></div><img class="detail-image" src="{s['delivery_image']}" alt="{esc(s['short_name'])}" width="400" height="270"></section><section class="detail-copy"><div><h2>What you can enquire about</h2><ul class="work-list">{''.join('<li>'+esc(w)+'</li>' for w in s['supported_work'])}</ul><p>Share your model and the symptoms with the workshop so the team can confirm the work needed.</p></div><aside class="detail-aside"><h3>Talk it through with us.</h3><p>Ask about assessment, estimates, parts and availability before arranging your repair. Your appointment is confirmed directly by our team.</p><a class="text-link" href="tel:+919655333511">{icon('phone')}+91 96553 33511</a><br><a class="text-link" href="https://wa.me/919655333511" target="_blank" rel="noopener noreferrer">{icon('whatsapp')}Ask on WhatsApp {icon('arrow')}</a></aside></section><section class="other-services"><h2>Another appliance?</h2><div class="other-links">{''.join(f'<a href="/services/{other["suggested_page_slug"]}/">{esc(other["short_name"])}</a>' for other in services if other['id']!=s['id'])}</div></section></main>'''
    target=DIST/path.lstrip('/')
    target.mkdir(parents=True,exist_ok=True)
    (target/'index.html').write_text(document(f"{s['name']} in Tirunelveli | Rishi Electronics",s['draft_description']+' Contact Rishi Electronics in Palayamkottai, Tirunelveli.',content,path))

policies={
 'privacy':('Privacy notice','''<p>This website helps you contact Rishi Electronics about electronics and appliance repairs.</p><h2>Your repair request</h2><p>The request form prepares a message in your browser. This website does not submit the form to a business database or store your request in browser storage. Details remain in the current page until you choose to share them.</p><p>If you continue to WhatsApp or email, the details you entered are included in a draft message. Review them before sending. The service you choose and the workshop will then process the information you share.</p><h2>Information to include</h2><p>Share only information needed for your enquiry: your name, contact number, appliance, fault description and preferred timing. Do not include passwords, payment card numbers or sensitive device contents.</p><h2>External services</h2><p>WhatsApp, your email provider and Google Maps operate under their own privacy policies. Hosting providers may process technical information needed to serve and secure the website. No advertising trackers or analytics scripts have been added to this website.</p><h2>Questions about your information</h2><p>Contact the workshop at <a href="mailto:rishielectronics25@gmail.com">rishielectronics25@gmail.com</a> or <a href="tel:+919655333511">+91 96553 33511</a> about information you have shared directly with the business.</p>'''),
 'terms':('About service enquiries','''<p>This website provides service information and ways to contact Rishi Electronics in Palayamkottai, Tirunelveli.</p><h2>Requests and appointments</h2><p>Preparing or sending a request does not reserve an appointment. Preferred dates and times are requests. The workshop confirms availability, location and next steps directly with you.</p><h2>Diagnosis and estimates</h2><p>Service descriptions show the types of work you can ask about. The team must assess your appliance and confirm whether a particular repair is possible. Ask about diagnosis or visit charges, repair estimates, parts, turnaround and any warranty before agreeing to work.</p><h2>Visits and collection</h2><p>Confirm home visits, pickup or delivery with the workshop before making arrangements. The website does not promise a service radius or collection option.</p><h2>Contact and opening hours</h2><p>Published hours are Monday–Saturday, 9 AM–8 PM. Sunday is by appointment. Call <a href="tel:+919655333511">+91 96553 33511</a> if you need to confirm the shop is open before travelling.</p>''')
}
for slug,(title,body) in policies.items():
    target=DIST/slug;target.mkdir(exist_ok=True)
    content=f'<main id="main" class="wrap policy-page"><a class="text-link" href="/">← Back to home</a><h1 style="margin-top:25px">{title}</h1>{body}</main>'
    (target/'index.html').write_text(document(title+' | Rishi Electronics',title+' for the Rishi Electronics repair enquiry website.',content,'/'+slug+'/'))

urls=['/']+[f"/services/{s['suggested_page_slug']}/" for s in services]+['/privacy/','/terms/']
(DIST/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{ORIGIN}{u}</loc></url>' for u in urls)+'</urlset>')
(DIST/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+ORIGIN+'/sitemap.xml\n')
(DIST/'favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" rx="9" fill="#e6f4f2"/><g transform="translate(4 4)" fill="none" stroke="#006575" stroke-width="2" stroke-linecap="round">'+paths['chip']+'</g></svg>')
# Keep the supplied evidence in source control, outside the public website.
evidence=ROOT/'research';evidence.mkdir(exist_ok=True)
for p in SOURCE.iterdir():
    if p.suffix in ['.json','.md'] and p.resolve() != (evidence/p.name).resolve():shutil.copy2(p,evidence/p.name)
(evidence/'CURRENT-RECHECK.md').write_text('''# Recheck: 21 October 2026, India time

Reference design: user-selected teal and white appliance selector, compact product hero, nine service cards, mobile Call and WhatsApp bar.

The .online page was retrieved and its eight service categories, address, phone, email and hours matched the supplied package. The .com direct page retrieval was unavailable in this environment; search-indexed content corroborated the nine-service catalogue, including RO purifier repair. The earlier dated ZIP remains the audit trail for historic technical findings. No live ranking, uptime, review authenticity or form-delivery claims are made.

Contact: +91 96553 33511; rishielectronics25@gmail.com.
Hours: Monday–Saturday, 09:00–20:00; Sunday by appointment.
Address: H107, Kamarajar Salai, Anbunagar, Maharaja Nagar, Palayamkottai, Tirunelveli, Tamil Nadu 627011.

Differences retained: .com has RO purifier, .online omits it. Nine categories are kept in the rebuild. Unverified 5.0 rating/testimonials are omitted. Prices, warranties, founding year, legal entity, all-brand authorization and doorstep radius remain unconfirmed.

Repair requests are browser-local drafts and are handed to WhatsApp or email after explicit customer action. No request is automatically sent or claimed to be received. No customer data, secret form credentials, database or analytics is deployed.

The hero is a new illustrative AI-generated appliance arrangement. Service pictures and shop exterior come from the supplied original asset package, optimized as separate copies. Their reuse rights should be confirmed by the business before a public custom-domain launch. The original Rishi Electronics header logo and matching flame favicon are reused from the supplied previous-site assets, following the user's request.

The deployment is a separate owner-private Site. Existing .com/.online hosting and DNS are unchanged. The domain canonical/sitemap use the actual new Site origin.
''')
(ROOT/'README.md').write_text('''# Rishi Electronics

Buildless HTML, CSS and JavaScript website following the selected teal appliance-service design.

## Features
- Nine dedicated service pages, responsive homepage, keyboard-accessible request dialog.
- WhatsApp and email draft handoff; no automatic message sending or fake booking confirmations.
- Indian mobile-number validation and Asia/Kolkata date handling.
- Published workshop address, hours, phone and email; privacy and enquiry information.
- Optimized local WebP assets, sitemap and business structured data without unverified reviews.

The deployable website is `dist/`. Source evidence is in `research/` and is not part of the public static directory. `build_content.py` records how content and assets were generated from the supplied research archive. The finished dist directory is ready to serve as-is and needs no runtime dependencies.

Use `node --test tests/domain.test.mjs` for request logic checks. `python3 validate_site.py` checks the generated pages and local links. A real WhatsApp message, email or appointment has not been sent during testing.
''')
print('Generated',len(urls),'pages and optimized images.')
