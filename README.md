# Rishi Electronics

Buildless HTML, CSS and JavaScript website following the selected teal appliance-service design.

## Features
- Nine dedicated service pages, responsive homepage, keyboard-accessible request dialog.
- WhatsApp and email draft handoff; no automatic message sending or fake booking confirmations.
- Indian mobile-number validation and Asia/Kolkata date handling.
- Published workshop address, hours, phone and email; privacy and enquiry information.
- Optimized local WebP assets, sitemap and business structured data without unverified reviews.

The deployable website is `dist/`. Source evidence is in `research/` and is not part of the public static directory. `build_content.py` records how content and assets were generated from the supplied research archive. The finished dist directory is ready to serve as-is and needs no runtime dependencies.

Use `node --test tests/domain.test.mjs` for request logic checks. `python3 validate_site.py` checks the generated pages and local links. A real WhatsApp message, email or appointment has not been sent during testing.
