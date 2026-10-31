# SAG Website: AI Editing Guide

Paste this whole file into ChatGPT, Claude, or another AI assistant before asking it to help edit the Submariners' Advocacy Group website. Coding tools that can read the repo (Claude Code, Cursor) can read this file directly.

## Instructions for the AI assistant

You are helping a volunteer edit the Submariners' Advocacy Group (SAG) website. Follow these rules on every edit.

1. **Edit data and templates, never generated HTML.** The `.html` pages are produced by `python build/build.py` from `build/templates/` and `build/data/`. Changes made directly to `.html` files are lost on the next build.
2. **Keep content in the JSON files valid.** Strings use double quotes; paragraphs in a `bio` list are separate strings separated by commas; no trailing comma after the last item.
3. **Preserve accessibility.** Every image needs `alt` text (empty `alt=""` only for decorative images). Keep one `<h1>` per page and do not skip heading levels. Keep form `<label for>` pairs. Do not remove focus outlines.
4. **Preserve SEO.** Keep page titles in the form `Page Name | Submariners’ Advocacy Group` (or `| SAG` for long article titles) and under 60 characters. Keep meta descriptions under about 155 characters.
5. **Facts appear in more than one place.** If an email address, phone number, name, or role changes, update every location listed in "Facts that repeat" below.
6. **Do not invent facts.** No statistics, credentials, dates, or claims that SAG has not supplied.
7. **Stop and tell the user to contact BLKing Consulting (Bobby King)** for anything in the "Stop" list at the end.

## Common tasks

### Add or update a board member's biography
File: `build/data/board.json`. Find the person by `"slug"` (for example `"rodney-boucher"`). Put each paragraph as its own string in `"bio"`:

```json
"bio": [
  "First paragraph.",
  "Second paragraph."
]
```

### Add a regional representative's biography
File: `build/data/regional.json`. Same pattern; the `"bio"` list is currently empty (`[]`) for every rep. Once a bio exists, the "coming soon" line disappears automatically.

### Add a headshot
Save the photo as a JPG, portrait orientation (2:3, at least 750 by 1125 pixels), named with the person's slug:
- Board: `assets/img/board/<slug>.jpg`
- Regional: `assets/img/regional/<slug>.jpg`

Then set `"photo": "assets/img/board/<slug>.jpg"` (or the regional path) for that person in the JSON. Alt text is generated automatically from the person's name.

### Link a report PDF
Save the PDF in `assets/docs/`. In `build/data/news.json`, under `"docs"`, set the matching entry's `"file"`:

| Key | Document |
|---|---|
| `press` | Press Release |
| `abstract` | Abstract |
| `full` | Full Report |
| `a1`, `a1rel` | Amendment 1 (both keys point to the same file) |
| `a2` | Amendment 2 |

Example: `"file": "assets/docs/unseen-burden-abstract.pdf"`

### Add the presentation video
In `build/data/news.json`, set `"video_url"` to `https://www.youtube-nocookie.com/embed/VIDEO_ID`, where `VIDEO_ID` is the part after `v=` in the YouTube link.

### Add a news article
In `build/data/news.json`, copy an existing entry in `"articles"` and change `slug` (lowercase words joined by hyphens), `title`, `short_title`, `summary`, `image`, `alt`, `w`, `h`, and `blocks`. Block types: `{"type": "p", "text": "..."}` for a paragraph, `{"type": "h2", "text": "..."}` for a heading, `{"type": "ul", "items": ["...", "..."]}` for a bullet list.

### Turn on the donation form
In `build/data/donate.json`, set `"zeffy_url"` to the Zeffy embed link SAG receives from Zeffy.

### After any edit
```powershell
python build/build.py
git add -A
git commit -m "Describe the change"
git push origin main
```
Then open the live page and confirm the change appears.

## Facts that repeat

| Fact | Locations |
|---|---|
| Public affairs email | `SITE["email"]` in `build/build.py` (footer, contact page, schema, llms.txt); `stories_email` in `build/data/donate.json` |
| David L. Bozarth contact details | `contact` in `build/data/news.json`; `llms.txt` section in `build/build.py` |
| Board member name or role | `build/data/board.json` (drives the board page, bio page, page title, and schema) |
| Regional rep name or region | `build/data/regional.json` |
| Organization description | `ORG` in `build/build.py`; `llms.txt` section in `build/build.py`; home page meta description |

## Pre-publish checklist

- [ ] Ran `python build/build.py` with no errors
- [ ] Every new image has meaningful alt text, or `alt=""` if decorative
- [ ] Headings go in order (one H1, then H2, then H3)
- [ ] Repeated facts updated in every location above
- [ ] Checked the page on a phone after pushing

## Stop and contact BLKing Consulting (Bobby King)

- DNS, the `CNAME` file, or GitHub Pages settings
- The Contact form (FormSubmit) setup, or messages not arriving
- The `SITE` settings, JSON-LD schema, `robots.txt`, `sitemap.xml`, or `llms.txt`
- Google Analytics, Search Console, or Bing Webmaster Tools
- Adding new page types, changing the navigation menu, or changing the design system in `site.css`
- Any page that will not build, or a site that looks broken after a push
