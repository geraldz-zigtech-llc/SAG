# SAG Website: Site Plan and Discovery

**Client:** Submariners' Advocacy Group (SAG), nonprofit
**Builder:** ZigTech LLC
**Sources:** `docs/SAG_Website_Layout_-_SM_d1.0.pdf` (32 slides, PowerPoint wireframe) and `docs/News_and_Articles_2.pdf` (9 pages, Canva mockup)
**Target:** static HTML on GitHub Pages, custom domain, ZigTech build standards (WCAG 2.1 AA, SEO/GEO baseline, FormSubmit, handoff docs)

---

## 1. Global elements (every page)

**Top nav (from both PDFs):** Home | About | SAG Online Store | News and Articles | Donate | Contact

**Footer (from News PDF):** three columns

| Column | Content |
|---|---|
| Author/Site info | public-affairs email (domain to be confirmed, see Open Items) |
| Navigation | About, Contact, Donate, Home, News and Articles, Online Store |
| About | "Members of the Silent Service have been faithful to their oaths and training and have been silent for far too long. SAG will advocate for all Submariners." |

Copyright line: "Copyright Submariners' Advocacy Group © 2025" (will render the current year).

**Tagline:** Submariners Helping Submariners

## 2. Page inventory and URL plan

| # | Page | URL | Source | Content status |
|---|---|---|---|---|
| 1 | Home | `/` | Slide 1 | Ready: hero, crest, title, tagline, buttons to Mission / Vision / Core Values |
| 2 | Mission | `/mission.html` | Slide 2 | Ready |
| 3 | Vision | `/vision.html` | Slide 3 | Ready (hero image too small, see Assets) |
| 4 | Core Values | `/core-values.html` | Slide 4 | Ready |
| 5 | About | `/about.html` | Slides 5, 6 | Ready: About text plus Our Goals; buttons to Board and Regional Reps |
| 6 | Board of Directors | `/board/` | Slides 7 to 9 | Ready: 10 cards |
| 7 to 16 | Board bios (10) | `/board/<name>.html` | Slides 10 to 19 | 9 ready; Rodney Boucher has no photo and no bio |
| 17 | Regional Representatives | `/regional/` | Slides 20 to 22 | 10 cards; Edward Perry has no photo |
| 18 to 27 | Regional rep bios (10) | `/regional/<name>.html` | Slides 23 to 32 | All 10 bios are PLACEHOLDER |
| 28 | News and Articles | `/news/` | News p1 | Ready: 6 article tiles plus 6 "NEW" slots for future posts |
| 29 | The Submarine Tradition | `/news/the-submarine-tradition.html` | News p2 | Ready |
| 30 | Why Submariners' Advocacy Group? | `/news/why-sag.html` | News p3 | Ready |
| 31 | Submarine Toxic, Hazardous, and Radiation Exposures | `/news/submarine-toxic-hazardous-radiation-exposures.html` | News p4 | Ready |
| 32 | The Unseen Burden | `/news/the-unseen-burden.html` | News p5 | Needs YouTube URL plus 3 PDFs |
| 33 | The Unseen Burden, Amendment 1 | `/news/unseen-burden-amendment-1.html` | News p6 | Needs PDF |
| 34 | The Unseen Burden, Amendment 2 | `/news/unseen-burden-amendment-2.html` | News p7 | Needs PDF |
| 35 | Donate | `/donate.html` | News p8 | Needs Zeffy embed code |
| 36 | Contact | `/contact.html` | News p9 | FormSubmit; needs recipient email |
| 37 | SAG Online Store | external link or `/store.html` | Nav only | No layout provided; platform unknown |
| 38 | Thank You | `/thank-you.html` | Standard | Build item (noindex, excluded from sitemap) |
| 39 | 404 | `/404.html` | Standard | Build item |

**Build approach recommendation:** the 20 bio pages share one layout (photo left, title bar, bio text, "Board of Directors Home" / "Regional Representatives Home" button). Generate them from one template with a small Python/Jinja2 script (same pattern as the Cutting Edge build) and commit the rendered static HTML. Adding a regional rep bio later becomes a one-file content edit. GitHub Pages still serves plain HTML with no build step on their side.

## 3. Design notes (measured from the PDFs)

| Token | Value | Where | Contrast |
|---|---|---|---|
| Primary blue | `#241AEE` | Nav bar, buttons, title bars | White on it: 8.55:1 (pass) |
| Page background | `#DEDCFC` (lavender) | Layout deck pages | Blue text on it: 6.41:1 (pass) |
| Dark background | `#292929` | News PDF pages | White text: 14.55:1 (pass); **blue text on it: 1.7:1 (fail)** |
| Footer grey | `#7F7F7F` | News PDF footer | Black text: 5.24:1 (pass) |

**Style conflict to resolve:** the two PDFs use different looks. The layout deck is lavender with blue title bars and a crest watermark; the News mockup is dark charcoal with a grey footer. Recommend one unified theme (the deck's blue/lavender for structure, the News pages' Dolphins banner as a section accent) so the site doesn't switch identity between About and News.

Crest watermark behind body text must be faded enough to keep text contrast at 4.5:1; verify with axe-core after build.

## 4. Extracted assets (in `assets/img/`)

| Folder | Files | Notes |
|---|---|---|
| `brand/` | `sag-crest.png` (400x456, transparent), `sag-watermark.png`, `dolphins.png` (362x113) | Request a vector or larger crest for favicon and OG image |
| `hero/` | home, mission, vision, core-values | `vision.jpg` is only 453x386; needs a larger original |
| `board/` | 9 headshots | Rodney Boucher missing |
| `regional/` | 9 headshots | Edward Perry missing |
| `news/` | 4 article images | Unseen Burden video thumbnail comes from YouTube embed |

All extracted text is in `content/` as markdown, one file per page, tagged with its source slide.

## 5. Open items for SAG (blocking or needed before launch)

1. **Canonical domain.** The PDFs use two domains: `public-affairs@submarinersadvocacygroup.org` (footer) and `public-affairs@subadvocates.org`, `dbozarth@subadvocates.org`, `www.subadvocates.org` (Donate and report pages). Which is the website domain, where is DNS hosted, and what currently hosts the site?
2. **GitHub ownership.** SAG organization account, or build under `geraldz-zigtech-llc` and transfer at handoff.
3. **SAG Online Store.** No page in the layout. Existing store URL or platform?
4. **Missing content:** Rodney Boucher photo and bio; Edward Perry photo; all 10 Regional Representative bios.
5. **Report files:** Press Release, Abstract, Full Report (59 pages), Amendment 1, Amendment 2 as PDFs; YouTube URL for "Watch the Presentation."
6. **Zeffy** donation form embed code or form URL.
7. **Contact form recipient** email address.
8. **Nonprofit status:** 501(c)(3) determination and EIN, if SAG wants tax deductibility language on the Donate page and in schema. Nothing will be stated without confirmation.
9. **Online presence** for `sameAs` schema and NAP check: Facebook, LinkedIn, YouTube channel, X, Google Business Profile, GuideStar/Candid listing.
10. **Larger originals** of the Vision hero image and the crest.

## 6. Content corrections to confirm with SAG (not changed silently)

| Location | As written | Suggested |
|---|---|---|
| News index tile | "The Unseen Burden, Amendment 2: Physiological Effects" | Page title is "Compounded Stressors" |
| Unseen Burden, Amendment 1, Amendment 2 pages | "recommmendations" | "recommendations" |
| Donate | "Transparancy", "organzations" | "Transparency", "organizations" |
| Donate, Transparency bullets | Travel = "resources and assistance to families"; Business Operations = "educational programs and training" | Descriptions look swapped from a template; SAG to supply accurate wording |
| Toxic Exposures article | "required to breath" | "breathe" |
| Toxic Exposures article | "estimated <300,000 Submariners" | Likely "approximately 300,000" |
| Regional cards | "Ed Perry" (card) vs "Edward Perry" (bio) | Pick one |
| Board cards | "Chuck Sanders" (card) vs "Charles 'Chuck' Sanders" (bio) | Fine as is; confirm |
| Footer | © 2025 | Current year |

**Punctuation:** the client copy uses em dashes in several bios and the About page. This is SAG's own voice; keep as written unless SAG wants them normalized.

## 7. Standard build items (ZigTech baseline)

`thank-you.html`, `404.html`, `robots.txt` (AI crawler entries, thank-you disallowed), `sitemap.xml`, `llms.txt`, canonical and OG/Twitter meta on every page, JSON-LD (`NGO`/`Organization`, `WebSite`, `BreadcrumbList` for board/regional/news hierarchy, `Person` on bio pages, `Article` on news pages), GA4 placeholder, favicon from crest, FormSubmit with honeypot/`_autoresponse`/absolute `_next`, `README.md`, `ai-editing-guide.md`, `.github/master-checklist.md`, DNS and email security baseline, Playwright plus axe-core at desktop and mobile.
