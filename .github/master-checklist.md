# SAG Website: Master Checklist

Source of truth for the SAG build. Mark items DONE with the final value used.

## Discovery
- [x] DONE: Layout deck (32 slides) and News mockup (9 pages) reviewed; site plan in `docs/site-plan.md`
- [x] DONE: Images extracted to `assets/img/`; page copy extracted to `content/`
- [x] DONE: Brand colors pixel sampled (`#241AEE`, `#DEDCFC`, `#292929`, `#7F7F7F`) and contrast measured
- [ ] Canonical domain confirmed (subadvocates.org vs submarinersadvocacygroup.org)
- [ ] Current host and DNS provider identified; DNS access granted
- [ ] GitHub repo owner decided (SAG org vs geraldz-zigtech-llc then transfer)
- [ ] Unified visual theme approved (deck style vs News style)

## Client dependencies
- [ ] Rodney Boucher photo and bio
- [ ] Edward Perry photo
- [ ] Regional Representative bios (10)
- [ ] Unseen Burden PDFs: Press Release, Abstract, Full Report, Amendment 1, Amendment 2
- [ ] YouTube URL for the Unseen Burden presentation
- [ ] Zeffy embed code
- [ ] Contact form recipient email
- [ ] Online Store URL or platform
- [ ] Nonprofit status and EIN (only if SAG wants it published)
- [ ] Social profiles and listings for `sameAs`
- [ ] Larger Vision hero image and crest
- [ ] Content corrections in `docs/site-plan.md` section 6 approved

## Build
- [ ] Shared template (header, nav, footer, watermark)
- [ ] Home, Mission, Vision, Core Values
- [ ] About plus Our Goals
- [ ] Board index plus 10 bios (template generated)
- [ ] Regional index plus 10 bios (template generated)
- [ ] News index plus 6 articles
- [ ] Donate (Zeffy)
- [ ] Contact (FormSubmit: honeypot, `_autoresponse`, absolute `_next`)
- [ ] `thank-you.html` (noindex, sitemap excluded, robots Disallow)
- [ ] `404.html`
- [ ] Favicon from crest

## SEO / GEO
- [ ] Canonical, OG/Twitter, viewport, titles under 60 characters
- [ ] JSON-LD: Organization/NGO, WebSite, BreadcrumbList, Person, Article
- [ ] `robots.txt`, `sitemap.xml`, `llms.txt`
- [ ] GA4 placeholder

## Verification
- [ ] Playwright plus axe-core, desktop and mobile, zero violations
- [ ] Watermark contrast verified on every page type

## Handoff
- [ ] `README.md`
- [ ] `ai-editing-guide.md`
- [ ] FormSubmit activation completed by SAG
- [ ] DNS cutover, CNAME, Enforce HTTPS, GitHub verified domain
- [ ] DNS and email security baseline (SPF, DKIM, DMARC, TLS-RPT, MTA-STS, CAA, DNSSEC)
- [ ] Search Console domain property, sitemap submitted, Bing import
