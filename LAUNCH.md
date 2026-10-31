# SAG Website: Launch Handoff

Handoff from ZigTech LLC (Gerald Ziegler) to BLKing Consulting (Bobby King), 2026-10-31.
The site is fully built and verified on the test URL. This file lists exactly what remains to go live.

## Current state

| Item | Status |
|---|---|
| Pages | 39 pages built, accessibility checked (axe-core, desktop and mobile, zero violations) |
| Test URL | https://geraldz-zigtech-llc.github.io/SAG/ (changes to `https://<new-owner>.github.io/SAG/` after transfer) |
| Production domain | `www.submarinersadvocacygroup.org` (confirmed by David Bozarth, 2026-10-31) |
| Contact form | FormSubmit, recipient `public-affairs@submarinersadvocacygroup.org`; not yet activated |
| Donate | Zeffy form `42178bfd-6ec4-407b-afb2-2a4527857c8a` embedded and working |
| Search engines | Every page is `noindex` until launch (`SITE["preview"] = True` in `build/build.py`) |
| SAG contacts | David Bozarth (President/Executive Director); Scott Muranko (website lead) |

## Watch out: the old site holds the domain

The old SAG site was served from the `bl-king-consulting.github.io` repo. GitHub allows a custom domain on only one repo at a time, so `www.submarinersadvocacygroup.org` must be removed from the old repo's Pages settings (and its `CNAME` file deleted) before it can be added to this repo. Do this at cutover so the site is down for minutes, not hours.

## Launch steps

1. **Turn off preview mode.** In `build/build.py`, set `SITE["preview"] = False`. This removes `noindex`, points the Contact form `_next` redirect at `https://www.submarinersadvocacygroup.org/thank-you.html`, and makes the 404 page use `/` as its base path.
2. **Analytics.** In `build/templates/base.html`, replace both `G-XXXXXXXXXX` values with SAG's existing GA4 ID `G-RJXTRXGKXS` (taken from the old site; confirm SAG still uses that property).
3. **CNAME.** Create a file named `CNAME` at the repo root containing exactly `www.submarinersadvocacygroup.org`.
4. **Build and push.** `python build/build.py`, then commit and push.
5. **Release the domain from the old repo** (see the warning above).
6. **DNS for submarinersadvocacygroup.org.** Apex `@`: four A records `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` (optional AAAA `2606:50c0:8000::153` through `2606:50c0:8003::153`). `www`: CNAME to `<new-owner>.github.io`. GitHub redirects the apex to `www` automatically.
7. **Pages settings.** Custom domain `www.submarinersadvocacygroup.org`; check **Enforce HTTPS** once the DNS check passes (certificate can take up to 24 hours). Verify the domain under the owning account's Settings, Pages, Verified domains.
8. **Forwarding domains.** `4submariners.org`, `subwives.org`, and `subadvocates.org` forward (301) to `https://www.submarinersadvocacygroup.org` using registrar URL forwarding. **`subadvocates.org` is SAG's email domain: change only its web records (`@` and `www`). Do not touch its MX, SPF, DKIM, or DMARC records.**
9. **Activate the Contact form.** Submit the live form once. Someone at SAG opens `public-affairs@submarinersadvocacygroup.org`, finds FormSubmit's "Activate your form" email (check spam), and clicks the link. If that email never arrives, the address does not receive mail and must be set up first, since SAG's mail runs on `subadvocates.org`.
10. **Search engines.** Google Search Console Domain property for `submarinersadvocacygroup.org`, submit `sitemap.xml`, then import into Bing Webmaster Tools.
11. **Old URLs (optional).** The old site used `/about/`, `/donate/`, `/contact/`, `/calendar/`, `/blog/`, and `/2025/11/08/unseen-burden.html`. Small redirect pages at those paths keep old links and bookmarks working.

## Content still owed by SAG

- Amendment 2 PDF (button shows "PDF coming soon")
- Photos for Rodney Boucher and Edward Perry
- Rodney Boucher's bio and all 10 Regional Representative bios
- Online Store platform or URL (`store.html` is a "coming soon" placeholder)
- Social media links for the footer and `sameAs` schema
- Approval of the content corrections in `docs/site-plan.md` section 6 (typos left as SAG wrote them)
- Decision on carrying over the old site's events calendar, February 2025 white paper, and Executive Summary

## Reference

- `README.md`: structure, build process, common edits
- `ai-editing-guide.md`: guide for editing the site with an AI assistant
- `.github/master-checklist.md`: full build and launch checklist
- `docs/site-plan.md`: original page plan and content notes
