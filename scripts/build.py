#!/usr/bin/env python3
"""
Static site generator for the Rehohub landing page.

Generates:
  index.html                 – brand landing page
  services/<slug>.html       – one landing page per subsidiary

All brand content (subsidiaries, products, links) lives in the DATA section
below so the home page and the subsidiary pages never drift apart.

Usage:  python3 scripts/build.py
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# =====================================================================
# DATA
# =====================================================================

CONTACT = {
    "phone": "+234 805 651 6548",
    "phone_href": "tel:+2348056516548",
    "email": "info@rehohub.com",
    "site": "www.rehohub.com",
}

# Subsidiaries (Brand Guidelines p.5–9). Each one is a service with its
# own landing page at services/<slug>.html
SUBSIDIARIES = [
    dict(slug="rheti", name="Rheti", tag="Education", layout="wide",
         tagline="Skills that build careers and companies.",
         desc="A training Institute that is focused on skills acquisition and development training tailored towards entrepreneurship and Business Mentorship. The Institute maximizes the use of technology and digital products in the training of their clients and is focused on reducing unemployment in Africa by increasing employability and entrepreneurship.",
         offers=[("Skills acquisition", "Hands-on, practical programmes that turn ambition into employable, in-demand skills."),
                 ("Business mentorship", "Founders are paired with experienced mentors to plan, launch and scale."),
                 ("Digital-first learning", "Technology-led training delivered through modern digital products.")]),
    dict(slug="rehocon", name="RehoCon", tag="Construction", layout="",
         tagline="Designing and building Africa's skylines and shorelines.",
         desc="This Subsidiary focuses on construction services, architectural designs, turn-key design and all forms of construction services at regional, national and international level. We specialize in the creation of islands and waterfront regions.",
         offers=[("Architectural design", "Concept-to-blueprint design for residential, commercial and civic spaces."),
                 ("Turn-key delivery", "End-to-end project delivery — you get the keys, we handle everything else."),
                 ("Islands & waterfronts", "Specialist engineering for land reclamation and waterfront regions.")]),
    dict(slug="rehofarm", name="RehoFarm", tag="Agriculture", layout="tall",
         tagline="Growing the African economy, one harvest at a time.",
         desc="An agricultural investment sector that focuses on cash crops like cocoa, rubber and palm tree with the intention to aid in the recovery of the African economy, reduction of unemployment and reduction of world hunger.",
         offers=[("Cash-crop investment", "Structured investment in cocoa, rubber and oil-palm plantations."),
                 ("Job creation", "Large-scale farming operations that create rural employment."),
                 ("Food security", "Contributing to the fight against hunger across Africa and beyond.")]),
    dict(slug="rehotrans", name="RehoTrans", tag="Logistics", layout="",
         tagline="Moving goods and people safely across Africa.",
         desc="A logistics company that serves the organization's supply chain system and provides road mobility to clients across the African region, utilizing road-worthy means of transportation and reducing risk to life and property. Inclusive in the plan is the amendment of the Nigerian railway system.",
         offers=[("Supply-chain logistics", "Reliable haulage that powers the entire Rehohub ecosystem."),
                 ("Road mobility", "Safe, road-worthy fleets moving clients across the region."),
                 ("Rail ambitions", "A long-term commitment to improving the Nigerian railway system.")]),
    dict(slug="rehoarts", name="RehoArts", tag="Arts & Culture", layout="",
         tagline="Preserving African history. Celebrating African talent.",
         desc="An arts exhibition and expo targeted subsidiary, focused on growing African history and cultural preservation by providing visibility to African talents in woodwork, painting, sculpture and arts. It is an award-giving sector for those that excel in their arts: music, painting and video.",
         offers=[("Exhibitions & expos", "Curated showcases that put African creatives on the world stage."),
                 ("Cultural preservation", "Documenting and celebrating African heritage and history."),
                 ("Awards", "Recognising excellence in music, painting, sculpture and video.")]),
    dict(slug="rehoevent", name="RehoEvent", tag="Events", layout="wide",
         tagline="Unforgettable events, flawlessly managed.",
         desc="A full-fledged event management organization that handles all kinds of event consultation, preparation, budgeting and management. We cover all sectors and also collaborate with other sectors.",
         offers=[("Consultation", "Expert guidance to shape the concept and experience of your event."),
                 ("Planning & budgeting", "Detailed preparation and transparent budgeting, start to finish."),
                 ("Full management", "On-the-day execution across corporate, social and public events.")]),
    dict(slug="rehofac", name="RehoFac", tag="Manufacturing", layout="",
         tagline="Turning raw materials into finished value.",
         desc="This is the manufacturing, plant and production sector of the organization. We focus on recycling, creation of products and creating end products for users from the raw materials provided by other sectors.",
         offers=[("Manufacturing", "Modern plants producing quality end products at scale."),
                 ("Recycling", "Circular production that reduces waste and protects the environment."),
                 ("Ecosystem sourcing", "Raw materials supplied directly by sister subsidiaries.")]),
    dict(slug="rehodez", name="RehoDez", tag="Branding", layout="",
         tagline="Bespoke design for every brand we touch.",
         desc="The organization's full branding sector, focused on creating bespoke designs for all branches or sectors in respect to all materials. Ranging across all services and external businesses, this sector collaborates and works with all other subsidiaries.",
         offers=[("Brand identity", "Logos, guidelines and visual systems built to last."),
                 ("Packaging & print", "Bespoke materials that make products stand out on the shelf."),
                 ("External clients", "Our design studio is open to businesses beyond the group.")]),
    dict(slug="rehotex", name="RehoTex", tag="Textiles", layout="",
         tagline="Fabric made with quality from the source.",
         desc="A textile and fabric creation business, focusing on ranching and wool plantation for biotech printing of materials with high quality produce for use or resale.",
         offers=[("Fabric creation", "High-quality textiles produced for fashion and industry."),
                 ("Ranching & wool", "Raw fibre sourced from our own ranching and wool plantations."),
                 ("Biotech printing", "Innovative printing processes for premium finished materials.")]),
    dict(slug="rehogive", name="RehoGive", tag="Charity", layout="full",
         tagline="Giving back to build African businesses.",
         desc="The company's charity arm that gives back in financial forms to the African space and focuses on building African businesses.",
         offers=[("Financial support", "Grants and giving that reach communities across Africa."),
                 ("Business building", "Backing African entrepreneurs with the capital to grow."),
                 ("Community impact", "Programmes that create lasting, measurable change.")]),
]

# Product categories. Replace the URLs below with the live web-app
# addresses and store listings as each product launches.
PRODUCTS = [
    dict(slug="aipay", name="AiPay", cat="Fintech · Payments", c1="#2185FF", c2="#1760BA", icon="pay",
         desc="Smart payments for everyday Africa. Send, receive and manage money instantly with a secure digital wallet built for individuals and businesses.",
         feats=["Instant transfers", "Bill payments", "Virtual cards", "Merchant tools"],
         web="https://aipay.rehohub.com",
         ios="https://apps.apple.com/app/aipay",
         android="https://play.google.com/store/apps/details?id=com.rehohub.aipay",
         screen=("Wallet", "₦248,500", "Available balance")),
    dict(slug="aimove", name="AiMove", cat="Mobility · Logistics", c1="#3d9bff", c2="#0c2a5e", icon="move",
         desc="Book rides, ship parcels and track deliveries in real time — powered by the RehoTrans network for safe, reliable movement.",
         feats=["Ride booking", "Parcel delivery", "Live tracking", "Fleet for business"],
         web="https://aimove.rehohub.com",
         ios="https://apps.apple.com/app/aimove",
         android="https://play.google.com/store/apps/details?id=com.rehohub.aimove",
         screen=("Trip", "12 min", "Driver arriving")),
    dict(slug="airise", name="AiRise", cat="EdTech · Careers", c1="#5aa9ff", c2="#1760BA", icon="rise",
         desc="Learn in-demand skills, get mentored by experts and grow your career or business — the digital home of Rheti training.",
         feats=["Courses", "Mentorship", "Certificates", "Job board"],
         web="https://airise.rehohub.com",
         ios="https://apps.apple.com/app/airise",
         android="https://play.google.com/store/apps/details?id=com.rehohub.airise",
         screen=("My learning", "78%", "Course progress")),
    dict(slug="greenfed", name="GreenFed", cat="AgriTech · Food", c1="#2185FF", c2="#0b4f8a", icon="leaf",
         desc="Invest in farms, buy fresh produce direct from growers and follow your harvest — connecting Africa's farms to its tables through RehoFarm.",
         feats=["Farm investment", "Fresh marketplace", "Harvest tracking", "Farmer support"],
         web="https://greenfed.rehohub.com",
         ios="https://apps.apple.com/app/greenfed",
         android="https://play.google.com/store/apps/details?id=com.rehohub.greenfed",
         screen=("Portfolio", "+18.4%", "Season returns")),
]

# =====================================================================
# ICONS
# =====================================================================

R_PATH = ('<path fill-rule="evenodd" d="M118.56 107.61c5.7-12.04 13.1-.34 18.93 0h13.29l-12.98-20.54c5.73-2.44 '
          '9.47-8.32 9.47-15.12 0-4.96-1.76-9.09-5.35-12.45-3.51-3.43-7.79-5.11-12.75-5.11h-22.3c24.96 12.14-.55 '
          '33.86 0 53.22z"/><circle cx="106.09" cy="69.29" r="4.87"/>')


def r_mark(cls="", label=None):
    """The Rehohub 'R' brand mark, drawn in currentColor."""
    aria = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true"'
    return f'<svg class="{cls}" viewBox="100 53 52 56" fill="currentColor" {aria}>{R_PATH}</svg>'


def logo_icon(cls="logo__icon"):
    return (f'<svg class="{cls}" viewBox="0 0 80 80" aria-hidden="true"><rect width="80" height="80" rx="12" fill="currentColor"/>'
            f'<g class="logo__r" transform="translate(40 40) scale(0.95) translate(-126 -81)">{R_PATH}</g></svg>')


def logo_icon_light(cls="logo__icon"):
    return (f'<svg class="{cls}" viewBox="0 0 80 80" aria-hidden="true"><rect width="80" height="80" rx="12" fill="#fff"/>'
            f'<g transform="translate(40 40) scale(0.95) translate(-126 -81)" fill="#1760BA">{R_PATH}</g></svg>')


def ico(name):
    s = 'viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"'
    paths = {
        "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
        "arrow-ne": '<path d="M7 17 17 7M8 7h9v9"/>',
        "pay": '<rect x="2" y="5" width="20" height="14" rx="3"/><path d="M2 10h20M6 15h4"/>',
        "move": '<path d="M5 17h-1a2 2 0 0 1-2-2v-4l2.5-5h11l2.5 5h2a2 2 0 0 1 2 2v2a2 2 0 0 1-2 2h-1"/><circle cx="7.5" cy="17" r="2"/><circle cx="16.5" cy="17" r="2"/><path d="M9.5 17h5"/>',
        "rise": '<path d="m3 17 6-6 4 4 8-8"/><path d="M14 7h7v7"/>',
        "leaf": '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10Z"/><path d="M2 21c0-3 1.9-5.4 5.1-6"/>',
        "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/>',
        "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
        "spark": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M5.6 18.4l2.8-2.8M15.6 8.4l2.8-2.8"/>',
        "users": '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
        "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
        "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
        "web": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/>',
        "check": '<path d="M20 6 9 17l-5-5"/>',
    }
    return f'<svg {s}>{paths[name]}</svg>'


APPLE = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.37 12.6c-.02-2.3 1.88-3.4 1.96-3.46-1.07-1.56-2.73-1.78-3.32-1.8-1.41-.14-2.76.83-3.47.83-.72 0-1.82-.81-2.99-.79-1.54.02-2.96.9-3.75 2.27-1.6 2.78-.41 6.89 1.15 9.14.76 1.1 1.67 2.34 2.86 2.3 1.15-.05 1.58-.74 2.97-.74 1.38 0 1.77.74 2.98.72 1.24-.02 2.02-1.12 2.77-2.23.87-1.28 1.23-2.52 1.25-2.58-.03-.01-2.39-.92-2.41-3.66zM14.1 5.86c.63-.77 1.06-1.83.94-2.89-.91.04-2.02.61-2.67 1.37-.58.67-1.1 1.76-.96 2.8 1.02.08 2.06-.52 2.69-1.28z"/></svg>')
PLAY = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#2185FF" d="M3.6 2.3 13.4 12l-9.8 9.7c-.4-.2-.6-.6-.6-1.1V3.4c0-.5.2-.9.6-1.1z"/>'
        '<path fill="#1760BA" d="m16.7 8.7-3.3 3.3-9.8-9.7c.2-.1.5-.1.8 0l12.3 6.4z"/>'
        '<path fill="#0c2a5e" d="m16.7 15.3-12.3 6.4c-.3.1-.6.1-.8 0l9.8-9.7 3.3 3.3z"/>'
        '<path fill="#5aa9ff" d="m20.4 12.9-3.7 2.4-3.3-3.3 3.3-3.3 3.7 2.4c.8.5.8 1.3 0 1.8z"/></svg>')

# =====================================================================
# SHARED LAYOUT
# =====================================================================


def head(title, desc, base):
    return f'''<!doctype html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<meta name="theme-color" content="#1760BA">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:type" content="website">
<link rel="icon" href="{base}assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}assets/css/styles.css">
<script>document.documentElement.classList.remove('no-js')</script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
'''


def header(base, solid=False):
    home = f"{base}index.html"
    return f'''<header class="header{' header--solid' if solid else ''}" id="top">
  <div class="container header__inner">
    <a class="logo" href="{home}" aria-label="Rehohub home">{logo_icon()}<span class="logo__word">Rehohub<span class="dot">.</span><sup>®</sup></span></a>
    <button class="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="nav"><span></span></button>
    <nav class="nav" id="nav" aria-label="Primary">
      <a class="nav__link" href="{home}#about">About</a>
      <a class="nav__link" href="{home}#services">Services</a>
      <a class="nav__link" href="{home}#products">Products</a>
      <a class="nav__link" href="{home}#contact">Contact</a>
      <a class="btn" href="{home}#products">Get our apps {ico("arrow")}</a>
    </nav>
  </div>
</header>
'''


def footer(base):
    home = f"{base}index.html"
    svc_links = "".join(f'<li><a href="{base}services/{s["slug"]}.html">{s["name"]}</a></li>' for s in SUBSIDIARIES[:5])
    svc_links2 = "".join(f'<li><a href="{base}services/{s["slug"]}.html">{s["name"]}</a></li>' for s in SUBSIDIARIES[5:])
    prod_links = "".join(f'<li><a href="{p["web"]}" target="_blank" rel="noopener">{p["name"]}</a></li>' for p in PRODUCTS)
    return f'''<footer class="footer">
  <div class="container">
    <div class="footer__grid">
      <div class="footer__about">
        <a class="logo logo--light" href="{home}" aria-label="Rehohub home">{logo_icon_light()}<span class="logo__word">Rehohub.<sup>®</sup></span></a>
        <p>A one-stop solution hub with sustainability and innovation at its core — serving Africa and reaching the world.</p>
      </div>
      <div><h4>Services</h4><ul>{svc_links}</ul></div>
      <div><h4>More</h4><ul>{svc_links2}</ul></div>
      <div><h4>Products</h4><ul>{prod_links}</ul>
        <h4 style="margin-top:28px">Contact</h4>
        <ul><li><a href="{CONTACT["phone_href"]}">{CONTACT["phone"]}</a></li><li><a href="mailto:{CONTACT["email"]}">{CONTACT["email"]}</a></li></ul>
      </div>
    </div>
    <div class="footer__big" aria-hidden="true">Rehohub.</div>
    <div class="footer__bottom">
      <span>© <span data-year>2026</span> Rehohub. All rights reserved.</span>
      <a href="#top">Back to top ↑</a>
    </div>
  </div>
</footer>
<script src="{base}assets/js/main.js" defer></script>
</body>
</html>
'''


def cta_block():
    return f'''<section class="section" id="contact">
  <div class="container">
    <div class="cta reveal">
      {r_mark("hero__ghost hero__ghost--a")}
      <div>
        <span class="eyebrow eyebrow--light">Let's build together</span>
        <h2 style="margin-top:18px">Your one-stop hub<br>starts here.</h2>
        <p>Partner with any Rehohub subsidiary, invest in our ecosystem or bring your next big project to life. Our team responds within one business day.</p>
      </div>
      <div class="cta__contact">
        <a href="mailto:{CONTACT["email"]}">{ico("mail")} {CONTACT["email"]}</a>
        <a href="{CONTACT["phone_href"]}">{ico("phone")} {CONTACT["phone"]}</a>
        <a href="https://{CONTACT["site"]}">{ico("web")} {CONTACT["site"]}</a>
      </div>
    </div>
  </div>
</section>
'''

# =====================================================================
# HOME PAGE
# =====================================================================


def orbit():
    n = len(SUBSIDIARIES)
    items = "".join(
        f'<div class="orbit__item" style="--a:{round(360 / n * i)}deg"><div class="orbit__chip">'
        f'<a href="services/{s["slug"]}.html">{s["name"]}</a></div></div>'
        for i, s in enumerate(SUBSIDIARIES))
    return f'''<div class="orbit reveal" style="--d:.2s">
        <div class="orbit__ring"></div><div class="orbit__ring orbit__ring--2"></div><div class="orbit__ring orbit__ring--3"></div>
        <div class="orbit__core">{r_mark(label="Rehohub")}</div>
        <div class="orbit__spin">{items}</div>
      </div>'''


def service_card(i, s):
    layout = f' svc--{s["layout"]}' if s["layout"] else ""
    short = s["desc"].split(". ")[0].rstrip(".") + "."
    return f'''<a class="svc{layout} reveal" style="--d:{(i % 3) * .08:.2f}s" href="services/{s["slug"]}.html">
        <img src="assets/img/{s["slug"]}.jpg" alt="" loading="lazy" width="422" height="281">
        <span class="svc__num">{i + 1:02d}</span>
        <span class="svc__tag">{s["tag"]}</span>
        <h3>{s["name"]}</h3>
        <p>{escape(short)}</p>
        <span class="svc__go">Explore {s["name"]} <i>{ico("arrow-ne")}</i></span>
      </a>'''


def phone_screen(p):
    t, big, sub = p["screen"]
    if p["icon"] == "rise" or p["icon"] == "leaf":
        middle = '<div class="ps-bars"><i style="height:40%"></i><i style="height:65%"></i><i style="height:50%"></i><i style="height:85%"></i><i style="height:70%"></i><i style="height:100%"></i></div>'
    else:
        middle = '<div class="ps-card"><i></i><i></i><i></i></div>'
    return f'''<div class="phone" aria-hidden="true"><div class="phone__screen">
          <span class="ps-title">{p["name"]} · {t}</span><span class="ps-big">{big}</span><span class="ps-sub">{sub}</span>
          {middle}<div class="ps-card"><i></i><i></i><i></i></div>
          <div class="ps-row"><i></i><i></i><i></i><i></i></div>
        </div></div>'''


def product_card(i, p):
    feats = "".join(f"<li>{f}</li>" for f in p["feats"])
    return f'''<article class="prod reveal" id="{p["slug"]}" style="--c1:{p["c1"]};--c2:{p["c2"]};--d:{(i % 2) * .1:.1f}s">
        <div>
          <span class="prod__cat">{p["cat"]}</span>
          <h3 class="prod__name"><span class="prod__icon">{ico(p["icon"])}</span>{p["name"]}</h3>
          <p class="prod__desc">{escape(p["desc"])}</p>
          <ul class="prod__feats">{feats}</ul>
          <div class="prod__actions">
            <a class="store store--web" href="{p["web"]}" target="_blank" rel="noopener" aria-label="Open {p["name"]} web app">{ico("web")}<span><small>Open the</small><b>Web App</b></span></a>
            <a class="store" href="{p["ios"]}" target="_blank" rel="noopener" aria-label="Download {p["name"]} on the App Store">{APPLE}<span><small>Download on the</small><b>App Store</b></span></a>
            <a class="store" href="{p["android"]}" target="_blank" rel="noopener" aria-label="Get {p["name"]} on Google Play">{PLAY}<span><small>Get it on</small><b>Google Play</b></span></a>
          </div>
        </div>
        {phone_screen(p)}
      </article>'''


def build_index():
    marquee_items = "".join(f"<span>{s['name']}</span>" for s in SUBSIDIARIES)
    services = "\n      ".join(service_card(i, s) for i, s in enumerate(SUBSIDIARIES))
    products = "\n      ".join(product_card(i, p) for i, p in enumerate(PRODUCTS))
    why = [("globe", "Pan-African reach", "Built for the African market, with the ambition to access markets worldwide."),
           ("shield", "Total ownership", "Minimal reliance on external suppliers means premium quality and fair pricing."),
           ("spark", "Innovation at the core", "Technology and sustainability drive every service and product we create."),
           ("users", "Built for YOU", "A digital ecosystem where the organisation truly serves its stakeholders.")]
    why_html = "".join(f'<div class="why__item reveal" style="--d:{i * .08:.2f}s"><div class="why__ico">{ico(a)}</div><h3>{b}</h3><p>{c}</p></div>' for i, (a, b, c) in enumerate(why))

    html = head("Rehohub — One hub. Endless services.",
                "Rehohub is a conglomerate of 10 service-providing subsidiaries and digital products serving the African market and beyond.", "")
    html += header("")
    html += f'''<main id="main">
<!-- ============ HERO ============ -->
<section class="hero">
  {r_mark("hero__ghost hero__ghost--a")}
  {r_mark("hero__ghost hero__ghost--b")}
  <div class="hero__glow"></div><div class="hero__grid"></div>
  <div class="container hero__inner">
    <div>
      <span class="hero__badge reveal"><b>NEW</b> AiPay, AiMove, AiRise &amp; GreenFed are here</span>
      <h1 class="reveal" style="--d:.08s">One hub.<br><span class="outline">Endless</span> <span class="swap" data-words="services.|solutions.|possibilities.|opportunities.">services.</span></h1>
      <p class="hero__lead reveal" style="--d:.16s">Rehohub is a conglomerate of ten subsidiaries and a growing family of digital products — expanding the frontier of technology and opening up opportunities to all consumers across Africa and beyond.</p>
      <div class="hero__ctas reveal" style="--d:.24s">
        <a class="btn btn--white" href="#services">Explore our services {ico("arrow")}</a>
        <a class="btn btn--ghost" href="#products">Discover products</a>
      </div>
      <div class="hero__meta reveal" style="--d:.32s">
        <div><strong data-count="10">10</strong>Subsidiaries</div>
        <div><strong data-count="4">4</strong>Digital products</div>
        <div><strong>1</strong>Ecosystem</div>
      </div>
    </div>
    {orbit()}
  </div>
  <a class="scroll-cue" href="#about" aria-label="Scroll to about section"></a>
</section>

<div class="marquee" aria-hidden="true"><div class="marquee__track">{marquee_items}{marquee_items}</div></div>

<!-- ============ ABOUT ============ -->
<section class="section" id="about">
  <div class="container about">
    <div class="about__media reveal">
      <div class="about__photo"><img src="assets/img/about.jpg" alt="A Rehohub professional at work" loading="lazy" width="447" height="620"></div>
      <div class="about__stamp">
        <svg viewBox="0 0 150 150" aria-hidden="true"><defs><path id="circ" d="M75 75m-58 0a58 58 0 1 1 116 0a58 58 0 1 1 -116 0"/></defs><text><textPath href="#circ">One-stop solution hub • Rehohub • Africa • </textPath></text></svg>
        <div><strong>10</strong><small>SUBSIDIARIES</small></div>
      </div>
    </div>
    <div class="about__copy reveal" style="--d:.1s">
      <span class="eyebrow">About us</span>
      <h2 class="title bar" style="margin-top:16px">A conglomerate of<br>service providers.</h2>
      <p class="lead">Rehohub itself has zero products and zero goods. Instead, under Rehohub lie ten major subsidiaries that provide a variety of services and functions to the African market — with the intention to also access foreign markets.</p>
      <p style="margin-top:18px;color:var(--ink-soft)">Our market objective is total ownership of the services we render, minimising supplier and external influence so we can deliver premium services at market-minimal pricing.</p>
      <div class="pillars">
        <div class="pillar"><h4>Sustainability</h4><p>Long-term thinking in every sector we operate in.</p></div>
        <div class="pillar"><h4>Innovation</h4><p>Technology that expands what's possible for consumers.</p></div>
      </div>
    </div>
  </div>
</section>

<!-- ============ MISSION / VISION ============ -->
<section class="section section--tint" style="padding-top:0;padding-bottom:0;background:linear-gradient(180deg,#fff 0,#fff 30%,var(--blue-50) 30%)">
  <div class="container mv">
    <article class="mv__card reveal">
      <img src="assets/img/mission.jpg" alt="" loading="lazy">
      <span class="eyebrow eyebrow--light">Our mission</span>
      <h3 style="margin-top:14px">Mission</h3>
      <p>To create a one-stop solution hub, with sustainability and innovation at its core, expanding the frontier of technology and opening up opportunities to all consumers through market-minimal pricing and premium services.</p>
    </article>
    <article class="mv__card reveal" style="--d:.1s">
      <img src="assets/img/vision.jpg" alt="" loading="lazy">
      <span class="eyebrow eyebrow--light">Our vision</span>
      <h3 style="margin-top:14px">Vision</h3>
      <p>To create a well-functional digitalised ecosystem where the organisation truly serves its stakeholders: <em>YOU</em></p>
    </article>
  </div>
</section>

<!-- ============ SERVICES ============ -->
<section class="section section--tint" id="services" style="padding-top:clamp(40px,6vw,80px)">
  <div class="container">
    <div class="section__head section__head--split">
      <div class="reveal">
        <span class="eyebrow">Our services</span>
        <h2 class="title bar" style="margin-top:16px">Ten subsidiaries.<br>One standard.</h2>
      </div>
      <p class="lead reveal" style="--d:.1s">From farms to fabrics, skylines to stages — each Rehohub subsidiary is a specialist in its field. Choose a service to visit its dedicated page.</p>
    </div>
    <div class="services">
      {services}
    </div>
  </div>
</section>

<div class="pattern" aria-hidden="true"></div>

<!-- ============ PRODUCTS ============ -->
<section class="section products-wrap" id="products">
  {r_mark("hero__ghost hero__ghost--a")}
  <div class="container">
    <div class="section__head section__head--split">
      <div class="reveal">
        <span class="eyebrow eyebrow--light">Product categories</span>
        <h2 class="title title--light bar bar--light" style="margin-top:16px">Digital products<br>for everyday life.</h2>
      </div>
      <p class="lead reveal" style="--d:.1s;color:rgba(255,255,255,.8)">Our ecosystem, in your pocket. Open any product in your browser or download the mobile app for iOS and Android.</p>
    </div>
    <div class="products">
      {products}
    </div>
  </div>
</section>

<!-- ============ WHY ============ -->
<section class="section">
  <div class="container">
    <div class="section__head" style="text-align:center;justify-items:center">
      <span class="eyebrow reveal">Why Rehohub</span>
      <h2 class="title bar bar--center reveal" style="--d:.08s">Premium services.<br>Market-minimal pricing.</h2>
    </div>
    <div class="why">{why_html}</div>
  </div>
</section>

{cta_block()}
</main>
'''
    html += footer("")
    (ROOT / "index.html").write_text(html, encoding="utf-8")

# =====================================================================
# SUBSIDIARY PAGES
# =====================================================================


CURRENT = ' aria-current="page"'


def build_service(idx, s):
    base = "../"
    offers = "".join(
        f'<div class="why__item reveal" style="--d:{i * .08:.2f}s"><span>{i + 1:02d}</span><div class="why__ico">{ico("check")}</div><h3>{escape(t)}</h3><p>{escape(d)}</p></div>'
        for i, (t, d) in enumerate(s["offers"]))
    siblings = "".join(
        f'<a href="{o["slug"]}.html"{CURRENT if o is s else ""}>{o["name"]}</a>' for o in SUBSIDIARIES)
    nxt = SUBSIDIARIES[(idx + 1) % len(SUBSIDIARIES)]
    html = head(f"{s['name']} — a Rehohub company", s["tagline"] + " " + s["desc"][:120], base)
    html += header(base)
    html += f'''<main id="main">
<section class="sub-hero">
  <img class="sub-hero__img" src="{base}assets/img/{s["slug"]}.jpg" alt="" width="422" height="281">
  {r_mark("hero__ghost hero__ghost--b")}
  <div class="container">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="{base}index.html">Rehohub</a><span>/</span><a href="{base}index.html#services">Services</a><span>/</span><span aria-current="page">{s["name"]}</span></nav>
    <span class="hero__badge"><b>{idx + 1:02d}</b> {s["tag"]}</span>
    <h1 style="margin-top:22px">{s["name"]}<span style="color:#9cc8ff">.</span></h1>
    <p class="tagline">{escape(s["tagline"])}</p>
    <div class="hero__ctas">
      <a class="btn btn--white" href="#contact">Work with {s["name"]} {ico("arrow")}</a>
      <a class="btn btn--ghost" href="#overview">Learn more</a>
    </div>
  </div>
</section>

<section class="section" id="overview">
  <div class="container sub-intro">
    <div class="reveal">
      <span class="eyebrow">{s["tag"]} · A Rehohub company</span>
      <h2 class="title bar" style="margin-top:16px">About {s["name"]}</h2>
      <p class="lead">{escape(s["desc"])}</p>
    </div>
    <div class="sub-intro__img reveal" style="--d:.1s"><img src="{base}assets/img/{s["slug"]}.jpg" alt="{s["name"]} — {s["tag"]}" loading="lazy" width="422" height="281"></div>
  </div>
</section>

<section class="section section--tint">
  <div class="container">
    <div class="section__head">
      <span class="eyebrow reveal">What we do</span>
      <h2 class="title bar reveal" style="--d:.08s">How {s["name"]} delivers.</h2>
    </div>
    <div class="offer">{offers}</div>
  </div>
</section>

<section class="section" style="padding-bottom:0">
  <div class="container">
    <div class="section__head section__head--split">
      <div class="reveal"><span class="eyebrow">The Rehohub family</span><h2 class="title bar" style="margin-top:16px">Explore other services.</h2></div>
      <div class="reveal" style="--d:.1s"><a class="btn" href="{nxt["slug"]}.html">Next: {nxt["name"]} {ico("arrow")}</a></div>
    </div>
    <div class="siblings reveal">{siblings}</div>
  </div>
</section>

{cta_block()}
</main>
'''
    html += footer(base)
    (ROOT / "services" / f"{s['slug']}.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    (ROOT / "services").mkdir(exist_ok=True)
    build_index()
    for i, s in enumerate(SUBSIDIARIES):
        build_service(i, s)
    print(f"Built index.html and {len(SUBSIDIARIES)} service pages.")
