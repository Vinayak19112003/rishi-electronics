# Rishi Electronics: website research and rebuild data

Research date: 14 October 2026, India time. Public website content, linked images, styles and scripts were inspected. Browser checks covered the desktop homepages and the .com booking dialog. No booking was submitted. This is a public-content audit, not access to private customer records, hosting accounts, analytics or the business inbox.

## 1. What the two websites establish

Both sites present the same Tirunelveli electronics and appliance repair business. They are closely related versions of a single-page service enquiry website. There is no linked product catalogue, cart, checkout or published price list. A rebuild should start as a local repair-service website unless the owner separately requests retail features.

| Item | Collected business data |
|---|---|
| Business | Rishi Electronics |
| Phone and linked WhatsApp | +91 96553 33511 |
| Email | rishielectronics25@gmail.com |
| Address | H107, Kamarajar Salai, Anbunagar, Maharaja Nagar, Palayamkottai, Tirunelveli, Tamil Nadu 627011 |
| Listed hours | Monday–Saturday, 9 AM–8 PM; Sunday by appointment |
| Observed website language | English |
| Public service catalogue | Nine distinct categories across the two sites |

These are consistently displayed public facts, not an independent certification of business operations. The WhatsApp link exists; the account was not contacted. The listed address is also consistent with the matching CallTirunelveli directory result, although that directory labels its locality Krishnapuram. Do not import unrelated Mumbai business listings found under the same name or older domain references.

## 2. Differences that matter for migration

| Area | .com | .online | Rebuild implication |
|---|---|---|---|
| Catalogue | 9 services | 8 services | RO purifier repair must not be lost |
| Booking selector | 9 choices | 8 choices | Keep cards, routes and form options synchronized |
| Main headings | Playfair Display | Poppins | Pick one deliberate type system |
| Body type | Inter | Inter | A useful shared starting point |
| Main colors | Purple, navy and cyan; gold accent | Blue and teal; amber accent | Existing designs do not use one consistent palette |
| Motion | Extra shapes, orbs, particles, scroll effects | Simpler slideshow and review motion | Preserve useful interactions and reduce decoration |
| Testimonials | Six original cards with named authors | Six original cards, including three generic labels | Verify evidence before publishing |
| Favicon | 64 × 64, about 4 KB | Different file, about 304 KB | Prefer a properly sized brand icon |

The websites share byte-identical downloaded copies of their common logo, shop photo, four hero backgrounds and eight common service pictures. This strongly indicates shared visual resources, but does not establish which deployment is authoritative. Choose the authoritative catalogue with the owner.

## 3. Service inventory

| Service | Publicly listed work, summarized | Presence |
|---|---|---|
| Television | Picture, power and software faults; LED/LCD/smart TV types | Both |
| Laptop | Hardware/software diagnosis; screens, batteries, keyboards and upgrades | Both |
| Mobile phone | Screens, batteries, liquid damage, charging connectors and software | Both |
| Home theater | Setup, maintenance, audiovisual faults and upgrades | Both |
| Inverter / UPS | Batteries, board faults and backup-power work | Both |
| Washing machine | Front/top-load and semi-automatic types; motors, drums and maintenance | Both |
| Refrigerator | Cooling, compressor, refrigerant and thermostat work | Both |
| Air conditioner | Installation, repair, cleaning, refrigerant and maintenance contracts | Both |
| RO purifier | Diagnosis, maintenance, filters and installation | .com only |

The structured catalogue contains suggested English copy, Tamil display labels, stable service IDs and asset references. These drafts are newly written. Scope statements do not prove brand authorization. No price, warranty, turnaround guarantee or exact home-visit coverage should be invented.

## 4. Existing visitor journey and booking data

The content order is home → services → shop information → reviews → contact → footer. Navigation uses page anchors rather than separate pages. Each service button opens the same appointment dialog and selects that service. Persistent call and WhatsApp buttons provide alternative enquiry routes.

The dialog contains name, phone, service, preferred date, preferred time and an optional problem description. The published time windows are 9 AM–12 PM, 12 PM–4 PM and 4 PM–7 PM. The evening request window ends one hour before the published closing time; this is not necessarily an error but should be confirmed.

The public script sends requests to Web3Forms. The recipient configuration is not exposed as an email address in the request code, so successful delivery to the published business email cannot be established from the page. The reviewed interface has no observed calendar availability check. Treat the date and time as preferences pending staff confirmation. The provider’s public form key is intentionally excluded from the rebuild dataset; configure a fresh approved destination.

For the rebuild, add a home-visit/shop-visit choice only after confirming what the business offers. Collect locality and address when a home visit is chosen. Keep the first interaction short and retain direct call/WhatsApp alternatives. Explain when staff will respond only after the business supplies an actual response standard.

## 5. Reviews and trust evidence

Both versions display a 5.0 Google rating without a review count. Their review button leads to a general name search rather than a verified place-specific review page. The .online authors include Happy Customer, Satisfied Customer and Local Resident; .com uses different names and wording for these positions. A matching television testimonial is assigned to Happy Customer on one site and Nagarajan Nagaraja.m on the other.

The script duplicates the six cards to create a scrolling loop. Twelve rendered cards are therefore not twelve unique reviews. The package records author labels and topic summaries, not full copied testimonials. The evidence does not justify declaring all reviews false, nor does it establish that they are authentic Google reviews. Verify them against the precise business profile and publish only attributable evidence. Obtain current rating and count before using a ratings badge or any rating schema.

## 6. Assets collected and quality assessment

Seventeen distinct local image files are included unchanged: one logo, one storefront photo, four hero backgrounds, nine service images and two favicon versions. The manifest lists original URLs, pixel dimensions, file sizes and SHA-256 hashes. Common files were deduplicated across domains.

| Asset type | Assessment | Recommended use |
|---|---|---|
| Logo | 1024 × 501 JPEG; roughly 736 KB | Obtain an original transparent/vector logo; generate a small delivery copy |
| Storefront | 680 × 306 photo | Useful location evidence; request a larger recent photo for a large hero |
| Hero images | Four 1024 × 1024 files; roughly 777–858 KB each | Select a suitable image and create responsive delivery sizes |
| Most service art | 1024 × 1024 | Suitable starting resolution for cards |
| Home theater | 275 × 183 | Avoid enlargement; replace for larger layouts |
| Inverter | 300 × 168 | Avoid enlargement; replace for larger layouts |
| RO purifier | 225 × 225 | Avoid enlargement; replace for larger layouts |

The .com local images total approximately 7.01 MB before optimization. This is the sum of collected files, not a measured initial page download or a performance score. The logo and illustrations do not all share a coherent visual style. The storefront photo includes additional signage; do not infer a legal connection between every business sign in the picture.

External Google/WhatsApp marks remain inventoried by URL and were not copied into the asset folder. Ownership and reuse rights were not independently established. For the new site, preserve the supplied originals and create separate WebP/AVIF or other delivery copies. Original bytes in this package have not been recompressed.

## 7. Technical and search audit

Both sites use public HTML, CSS and vanilla JavaScript. No framework build, shopping backend or customer login is linked in the inspected pages. .com also loads AOS and particles.js and adds a second stylesheet. The .online stylesheet imports Inter and Poppins; .com imports Inter and Playfair Display. Poppins is additionally declared as an accent font on .com but is not part of that observed import.

Both pages have one main heading, a description, keyword metadata and a viewport declaration. No canonical URL, Open Graph/Twitter preview metadata or JSON-LD was observed. Their robots.txt and sitemap.xml endpoints returned 404. Missing robots.txt does not itself stop indexing, but the sitemap and primary-domain setup should be resolved in the rebuild. Near-duplicate sites can leave search engines to choose a preferred URL; the audit does not measure an actual ranking penalty.

The bare .com domain loaded successfully. The www .com variant returned 502 in the research environment. The .online bare domain redirected to its www version. This is a concrete configuration item to investigate, not proof of an outage for every visitor. Both stylesheets reference images/background.jpg, which returned 404 on both hosts.

No analytics tag was observed in the retrieved HTML or scripts. This does not prove the business has no server-side analytics. Search Console, traffic, conversions, Core Web Vitals, hosting, DNS ownership and actual email-delivery records remain outside this audit.

## 8. Accessibility and mobile findings

The .com dialog opened and correctly preselected TV repair. Escape did not dismiss it. Its close element is a non-focusable span, no dialog role or aria-modal attribute was present, and focus remained on the triggering link. Replace it with an accessible dialog that moves focus, supports keyboard closure, traps focus while open and restores focus on exit.

The popup derives its earliest date from UTC using toISOString. Between midnight and 5:29 AM India time this can use the previous local date. Calculate booking dates in Asia/Kolkata. The phone field uses a ten-digit pattern; accepting +91 and spaces and then normalizing is a useful rebuild improvement.

Both stylesheets contain rules at 768 px and 480 px, including narrower layouts. No reduced-motion media rule was observed. Desktop .com had no measured horizontal overflow at the inspected viewport. Full mobile-device, screen-reader, keyboard and slow-network testing remains required; CSS breakpoint inspection is not a substitute for those tests. Images that had not loaded at the top of the page included lazy-loaded content and were not automatically classified as broken.

## 9. Recommended new website structure

Build a service website focused on helping a customer identify a repair and contact the shop. Suggested initial structure:

- Home: location, clear repair scope, service selector and immediate call/book actions.
- Services index and nine concise service pages: symptoms, actual work offered, enquiry action and relevant FAQ.
- About / workshop: current real photos, owner/team information when provided, and a practical repair process.
- Request a repair: compact form with pending-confirmation wording.
- Contact: exact address, hours, directions, call and WhatsApp.
- Privacy notice and service terms: based on actual data handling and business policy.

Use .com as the proposed primary domain if the business controls it and prefers it. Redirect the other domain and aliases only after ownership and destination are confirmed. Keep paths consistent with the catalogue IDs. Do not create separate locality pages with unsupported service coverage.

A strong homepage would put practical repair information above decorative animation: service categories, where the shop is, how to reach it, how a request is handled, and verified evidence. A restrained blue/navy palette with the existing brand mark is one design option, not a requirement. Tamil/English presentation would be useful for local visitors; Tamil is a proposed addition, not an existing site capability.

## 10. Data needed from the business before launch

| Missing information | Why it matters |
|---|---|
| Owner/legal name and any GST information | Accurate business identity and invoices |
| Confirmed services, brands and authorization | Prevent unsupported claims |
| Doorstep radius and locality coverage | Route enquiries correctly |
| Diagnosis/visit fees and estimates policy | Set customer expectations |
| Parts sourcing and repair warranty | Explain after-service responsibility |
| Pickup/delivery and payment methods | Clarify the real workflow |
| Current Google profile and review evidence | Publish reliable trust information |
| Booking destination and staff confirmation process | Ensure enquiries reach the business |
| Larger real workshop/technician photos | Improve credibility and visual quality |

Leave these values empty in production data until supplied. No prices, credentials, private customer data or invented guarantees were added.

## 11. Package contents and use

The ZIP contains business.json, services.json, booking.json, reviews-audit.json, assets-manifest.json, source-inventory.json, findings.json, NEW-WEBSITE-BRIEF.md, README.md and the original image assets. Use business.json as the shared contact source and services.json as the shared service list. Keep reviews excluded from publication until verified. The source inventory records discovered page anchors, external links, metadata and resource checks for traceability.

## 12. Sources and limits

- [Rishi Electronics .com](https://rishielectronics.com/): live homepage, linked assets and public scripts/styles inspected.
- [Rishi Electronics .online](https://www.rishielectronics.online/): live homepage, linked assets and public scripts/styles inspected.
- [Published directions link](https://maps.app.goo.gl/GQfMKw3diiBEmhEf7): redirect supplied business coordinates; the exact place and review details were not independently verified.
- [Matching local directory](https://www.calltirunelveli.com/rishi-electronics-in-krishnapuram-tirunelveli): a search result supports the matching name/address; no private directory contact access was used.

Coverage includes publicly linked content reachable at research time. No unlinked private/admin pages, customer records, historic snapshots or backend databases were accessed. No fabricated Lighthouse score, live ranking, traffic estimate, stock list or test booking is reported. Public facts, code observations, proposed design choices and unresolved business questions are deliberately distinguished.
