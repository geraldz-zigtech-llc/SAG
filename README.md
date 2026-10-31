# Submariners' Advocacy Group Website

Static website for the Submariners' Advocacy Group (SAG), built by ZigTech LLC and hosted on GitHub Pages.

| Item | Value |
|---|---|
| Repository | `geraldz-zigtech-llc/SAG` (transfers to SAG at handoff) |
| Test URL | https://geraldz-zigtech-llc.github.io/SAG/ |
| Production domain | `www.submarinersadvocacygroup.org` (confirmed by David Bozarth, 2026-10-31). `4submariners.org`, `subwives.org`, and `subadvocates.org` forward to it; `subadvocates.org` is also SAG's email domain |
| SAG website lead | Scott Muranko |
| Hosting | GitHub Pages, branch `main`, folder `/` (root) |
| Built by | ZigTech LLC, geraldz@zigtech-llc.com |

## How the site works

The site is plain HTML, CSS, and a small amount of JavaScript. GitHub Pages serves the files exactly as they are in the repo; nothing runs on GitHub's side.

The HTML pages are **generated** by a Python script from templates and data files. Edit the data or templates, run the script, and commit the regenerated HTML.

```powershell
pip install jinja2
python build/build.py
```

Never hand-edit a generated `.html` file; the next build overwrites it.

## Folder structure

| Path | Purpose |
|---|---|
| `index.html`, `mission.html`, `vision.html`, `core-values.html`, `about.html` | Generated top-level pages |
| `donate.html`, `contact.html`, `thank-you.html`, `store.html`, `404.html` | Generated top-level pages |
| `board/` | Board of Directors page and 10 bio pages (generated) |
| `regional/` | Regional Representatives page and 10 rep pages (generated) |
| `news/` | News and Articles page and 6 articles (generated) |
| `assets/css/site.css` | All styles; brand colors are CSS variables at the top |
| `assets/js/site.js` | Mobile menu and footer year |
| `assets/img/` | `brand/` (crest, watermark, Dolphins, favicons), `hero/`, `board/`, `regional/`, `news/` |
| `assets/docs/` | Report PDFs (Unseen Burden and amendments) once supplied |
| `build/build.py` | Page generator; also writes `sitemap.xml`, `robots.txt`, `llms.txt` |
| `build/templates/` | Jinja2 templates; `base.html` holds the header, nav, footer, and all meta tags |
| `build/data/` | Editable content: `about.json`, `board.json`, `regional.json`, `news.json`, `donate.json` |
| `content/`, `docs/` | Original text and PDFs from SAG's layout documents (reference only, not published content) |
| `.github/master-checklist.md` | Build and handoff checklist |

## Common edits

| Task | Where | Then |
|---|---|---|
| Add or change a board bio | `build/data/board.json`: the person's `bio` list, one string per paragraph | Run build, commit |
| Add a regional rep bio | `build/data/regional.json`: fill the empty `bio` list | Run build, commit |
| Add a headshot | Save as `assets/img/board/<slug>.jpg` or `assets/img/regional/<slug>.jpg`, set `photo` in the JSON | Run build, commit |
| Add a report PDF | Save in `assets/docs/`, set that document's `file` in `build/data/news.json` (for example `"assets/docs/unseen-burden-full-report.pdf"`) | Run build, commit |
| Add the presentation video | Set `video_url` in `build/data/news.json` to the YouTube embed URL (`https://www.youtube-nocookie.com/embed/<id>`) | Run build, commit |
| Add a news article | Add an entry to `articles` in `build/data/news.json`, copying an existing one | Run build, commit |
| Turn on the Zeffy donation form | Set `zeffy_url` in `build/data/donate.json` | Run build, commit |

## Do not change without ZigTech

- `CNAME` file, DNS records, and the GitHub Pages custom domain setting
- Contact form configuration in `build/build.py` and `build/templates/contact.html` (FormSubmit recipient, `_next`, `_autoresponse`, honeypot)
- `SITE` settings in `build/build.py` (domain, `preview` flag, email)
- `robots.txt`, `sitemap.xml`, `llms.txt` (generated; edit the generator, not the files)
- JSON-LD schema blocks in `build/build.py`
- Google Analytics Measurement ID in `build/templates/base.html`

## Launch steps (ZigTech)

1. Canonical domain is set in `SITE["url"]` in `build/build.py`.
2. Set `SITE["preview"] = False` to remove the noindex tag, and set the Contact form recipient.
3. Run the build, add a `CNAME` file containing the domain, commit, and push.
4. Update DNS (four GitHub Pages A records, optional AAAA records, `www` CNAME), set the custom domain in Pages settings, and enable Enforce HTTPS.
5. SAG submits the Contact form once and clicks the FormSubmit activation link.
6. Register the domain in Google Search Console and Bing Webmaster Tools and submit `sitemap.xml`.

## Contact

ZigTech LLC, Gerald Ziegler, geraldz@zigtech-llc.com
