"""Static page generator for the SAG website.

Run from the repo root:  python build/build.py
Renders Jinja2 templates in build/templates to plain HTML at the repo root.
GitHub Pages serves the generated HTML; nothing runs on GitHub's side.
"""
import datetime
import pathlib

from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = pathlib.Path(__file__).resolve().parent.parent
env = Environment(loader=FileSystemLoader(ROOT / "build" / "templates"),
                  autoescape=select_autoescape(["html"]), trim_blocks=True, lstrip_blocks=True)

# Canonical domain is a working assumption until SAG confirms (site plan, open item 1).
SITE = {
    "name": "Submariners’ Advocacy Group",
    "url": "https://subadvocates.org",
    "email": "public-affairs@subadvocates.org",
    "preview": True,  # adds noindex while the site lives on the github.io test URL; set False at launch
    "year": datetime.date.today().year,
    "nav": [
        {"key": "home", "label": "Home", "href": "index.html"},
        {"key": "about", "label": "About", "href": "about.html"},
        {"key": "store", "label": "SAG Online Store", "href": "store.html"},
        {"key": "news", "label": "News and Articles", "href": "news/index.html"},
        {"key": "donate", "label": "Donate", "href": "donate.html"},
        {"key": "contact", "label": "Contact", "href": "contact.html"},
    ],
}

ORG = {
    "@context": "https://schema.org",
    "@type": "NGO",
    "@id": SITE["url"] + "/#organization",
    "name": "Submariners' Advocacy Group",
    "alternateName": "SAG",
    "url": SITE["url"] + "/",
    "logo": SITE["url"] + "/assets/img/brand/sag-crest.png",
    "email": SITE["email"],
    "slogan": "Submariners Helping Submariners",
    "foundingDate": "2024-04",
    "description": ("Nonprofit organization founded by U.S. Navy Submariners to advocate for the health, "
                    "recognition, and care of all U.S. Navy Submariners through scientific research, "
                    "public education, and legislative advocacy."),
    "knowsAbout": ["U.S. Navy submarine service", "Submarine atmospheric contaminants",
                   "Veteran toxic exposure", "Veterans advocacy"],
}
WEBSITE = {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE["url"] + "/#website",
           "name": "Submariners' Advocacy Group", "url": SITE["url"] + "/",
           "publisher": {"@id": SITE["url"] + "/#organization"}}

STATEMENTS = {
    "mission": {
        "heading": "Mission",
        "lead": ("To advocate for the health, recognition, and care of all U.S. Navy Submariners "
                 "through scientific research, public education, and legislative advocacy."),
        "list_intro": "We are committed to:",
        "items": [
            {"text": "Driving research into submarine-related atmospheric contaminants and other occupational exposures."},
            {"text": "Supporting legislation that protects and benefits Submariners."},
            {"text": "Educating veterans, families, healthcare providers, and policymakers."},
            {"text": ("Ensuring every Submariner has access to information, advocacy, and a voice when "
                      "facing service-connected health challenges.")},
        ],
        "image": "assets/img/hero/mission.jpg", "w": 835, "h": 714,
        "alt": "A U.S. Navy submarine surfaced through Arctic sea ice with a crew member on the ice",
        "description": ("SAG's mission: advocating for the health, recognition, and care of all U.S. Navy "
                        "Submariners through research, education, and legislative advocacy."),
    },
    "vision": {
        "heading": "Vision",
        "lead": ("A future where every U.S. Navy Submariner is recognized, supported, and cared for, and "
                 "where the health consequences of submarine service are fully understood, acknowledged, "
                 "and never ignored."),
        "list_intro": "We envision a future where:",
        "items": [
            {"text": "Scientific research advances understanding of submarine service-related health conditions."},
            {"text": "Every eligible Submariner receives timely access to earned healthcare, benefits, and compensation."},
            {"text": "Policymakers recognize the unique occupational hazards of submarine service."},
            {"text": "Veterans and their families never face these challenges alone."},
        ],
        "image": "assets/img/hero/vision.jpg", "w": 453, "h": 386,
        "alt": "A submarine on the surface at sunset with an aircraft carrier on the horizon",
        "description": ("SAG's vision: every U.S. Navy Submariner recognized, supported, and cared for, with "
                        "the health consequences of submarine service fully understood."),
    },
    "core-values": {
        "heading": "Core Values",
        "lead": ("Integrity. Professionalism. Courage. Three principles that define who we are and guide "
                 "everything we do."),
        "list_intro": "What each value means to us:",
        "items": [
            {"label": "Integrity.", "text": ("We lead with honesty, ethics, and accountability. Our advocacy "
                                             "is grounded in facts, transparency, and trust.")},
            {"label": "Professionalism.", "text": ("We pursue excellence through discipline, credibility, "
                                                   "and respect. Every action reflects our commitment to "
                                                   "those we serve.")},
            {"label": "Courage.", "text": ("We challenge injustice, confront difficult truths, and pursue "
                                           "meaningful change for every U.S. Navy Submariner.")},
        ],
        "image": "assets/img/hero/core-values.jpg", "w": 1171, "h": 1001,
        "alt": "A submarine breaking the ocean surface during an emergency surfacing",
        "description": ("SAG's core values of Integrity, Professionalism, and Courage guide its advocacy for "
                        "U.S. Navy Submariners and their families."),
    },
}
LABELS = {"mission": "Mission", "vision": "Vision", "core-values": "Core Values"}

HOME_CARDS = [
    {"title": "Mission", "href": "mission.html",
     "text": "Advocating for the health, recognition, and care of all U.S. Navy Submariners."},
    {"title": "Vision", "href": "vision.html",
     "text": "A future where the health consequences of submarine service are fully understood and never ignored."},
    {"title": "Core Values", "href": "core-values.html",
     "text": "Integrity. Professionalism. Courage."},
]


def breadcrumb(*trail):
    """trail: (name, path) pairs after Home, e.g. ("About", "/about.html")."""
    items = [("Home", "/")] + list(trail)
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i, "name": n, "item": SITE["url"] + p}
        for i, (n, p) in enumerate(items, 1)]}


def load(name):
    import json
    return json.loads((ROOT / "build" / "data" / name).read_text(encoding="utf-8"))


def short(text, limit=155):
    """Trim text to a meta description length on a word boundary."""
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(" ", 1)[0].rstrip(",;:") + "..."


def render(template, out, page, root="", **ctx):
    html = env.get_template(template).render(site=SITE, page=page, root=root, **ctx)
    (ROOT / out).write_text(html, encoding="utf-8")
    print("wrote", out)


def main():
    render("home.html", "index.html", {
        "title": "Home | Submariners’ Advocacy Group",
        "description": ("Nonprofit founded by U.S. Navy Submariners advocating for the health, recognition, "
                        "and care of every Submariner through research, education, and legislation."),
        "path": "/", "nav": "home", "body_class": "page-home", "schema": [ORG, WEBSITE],
    }, cards=HOME_CARDS)
    for slug, s in STATEMENTS.items():
        s = dict(s, others=[{"label": LABELS[k], "href": k + ".html"} for k in STATEMENTS if k != slug])
        render("statement.html", slug + ".html", {
            "title": f"{s['heading']} | Submariners’ Advocacy Group",
            "description": s["description"], "path": f"/{slug}.html", "nav": "home",
            "body_class": "page-statement", "og_image": s["image"],
            "schema": [breadcrumb((s["heading"], f"/{slug}.html"))],
        }, s=s)

    about = load("about.json")
    render("about.html", "about.html", {
        "title": "About | Submariners’ Advocacy Group",
        "description": short("SAG is a nonprofit founded by U.S. Navy Submariners. Earning your Dolphins is "
                             "membership enough: no applications, dues, or eligibility requirements."),
        "path": "/about.html", "nav": "about", "body_class": "page-about",
        "schema": [breadcrumb(("About", "/about.html"))],
    }, **about)

    board = load("board.json")
    (ROOT / "board").mkdir(exist_ok=True)
    render("people_index.html", "board/index.html", {
        "title": "Board of Directors | Submariners’ Advocacy Group",
        "description": ("Meet the Board of Directors of the Submariners’ Advocacy Group, qualified U.S. Navy "
                        "Submariners leading SAG's advocacy for the submarine community."),
        "path": "/board/", "nav": "about", "body_class": "page-people",
        "schema": [breadcrumb(("About", "/about.html"), ("Board of Directors", "/board/"))],
    }, root="../", heading="Board of Directors", people=board,
       intro=("Every member of SAG's leadership has completed the U.S. Navy's submarine qualification "
              "process and earned the Dolphins."))
    for m in board:
        path = f"/board/{m['slug']}.html"
        person = {"@context": "https://schema.org", "@type": "Person", "name": m["full_name"].replace("“", '"').replace("”", '"'),
                  "jobTitle": m["role"], "url": SITE["url"] + path,
                  "memberOf": {"@id": SITE["url"] + "/#organization"}}
        if m["photo"]:
            person["image"] = SITE["url"] + "/" + m["photo"]
        desc = short(m["bio"][0]) if m["bio"] else f"{m['name']}, {m['role']}, Submariners’ Advocacy Group."
        render("person.html", f"board/{m['slug']}.html", {
            "title": f"{m['name']} | Submariners’ Advocacy Group",
            "description": desc, "path": path, "nav": "about", "body_class": "page-bio",
            "og_image": m["photo"],
            "schema": [person, breadcrumb(("About", "/about.html"), ("Board of Directors", "/board/"),
                                          (m["name"], path))],
        }, root="../", m=m, back_label="Board of Directors Home")

    regional = load("regional.json")
    (ROOT / "regional").mkdir(exist_ok=True)
    render("people_index.html", "regional/index.html", {
        "title": "Regional Representatives | Submariners’ Advocacy Group",
        "description": ("Meet the Regional Representatives of the Submariners’ Advocacy Group, serving "
                        "Submariners from New England to the Pacific Northwest."),
        "path": "/regional/", "nav": "about", "body_class": "page-people",
        "schema": [breadcrumb(("About", "/about.html"), ("Regional Representatives", "/regional/"))],
    }, root="../", heading="Regional Representatives", people=regional,
       intro="Meet SAG's Regional Representatives, listed by region.")
    for m in regional:
        path = f"/regional/{m['slug']}.html"
        person = {"@context": "https://schema.org", "@type": "Person", "name": m["full_name"],
                  "jobTitle": m["bio_role"], "url": SITE["url"] + path,
                  "memberOf": {"@id": SITE["url"] + "/#organization"}}
        if m["photo"]:
            person["image"] = SITE["url"] + "/" + m["photo"]
        desc = short(m["bio"][0]) if m["bio"] else (
            f"{m['name']} is the Submariners’ Advocacy Group Regional Representative for the {m['region']} region.")
        render("person.html", f"regional/{m['slug']}.html", {
            "title": f"{m['name']} | Submariners’ Advocacy Group",
            "description": desc, "path": path, "nav": "about", "body_class": "page-bio",
            "og_image": m["photo"],
            "schema": [person, breadcrumb(("About", "/about.html"), ("Regional Representatives", "/regional/"),
                                          (m["name"], path))],
        }, root="../", m=m, back_label="Regional Representatives Home")


if __name__ == "__main__":
    main()
