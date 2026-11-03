"""
Rheti (Rehohub Training Institute) subsidiary page.

Built from the Rehohub brand guidelines (Rheti entry), the Rheti brand guide
(logo meaning, palette, typography, brand essence) and "The Hack" programme poster.
Called from build.py's build_service() for the rheti subsidiary.
"""
from html import escape as e

BASE = "../"
HACK_LIST = "https://chat.whatsapp.com/Ga0LaFBzDSL5U7kRw0FTLn"
HANDLE = "@rheti.institute"

LOGO_MEANING = [
    ("r", "The iconic R from Rehohub", "Trust, reliability and innovation."),
    ("shield", "The shield", "Protection, excellence, standards and integrity."),
    ("book", "The open book", "Learning, knowledge and growth."),
    ("user", "A foundation for growth", "Empowerment and impact."),
]
ESSENCE = [
    ("book", "Education", "We ignite learning and curiosity."),
    ("users", "Empowerment", "We equip people with practical skills and confidence."),
    ("star", "Excellence", "We uphold high standards in everything we do."),
    ("chart", "Impact", "We build leaders who create value and transform communities."),
]
WHAT_WE_DO = [
    ("Skills acquisition", "Hands-on, practical training that turns ambition into skills people can use and get paid for."),
    ("Entrepreneurship training", "Programmes tailored to people starting and growing their own businesses."),
    ("Business mentorship", "Founders are paired with experienced mentors to plan, launch and scale."),
    ("Digital-first learning", "Technology and digital products are part of how every client is trained."),
]
BEFORE = [("plan", "register", "that business."), ("wallet", "spend", "your savings."), ("web", "build", "the website."), ("mail", "print", "the flyers.")]
STAGES = [("spark", "Idea", "Test whether you have a business or just an idea."), ("plan", "Plan", "Work out the customer, the money and the first steps."),
          ("store", "Build", "Set it up properly, in the right order."), ("rise", "Grow", "Build it to last and grow with impact.")]
PALETTE = [("Navy blue", "#0D2357"), ("Gold", "#D4A12A"), ("White", "#FFFFFF"), ("Charcoal", "#2F3640")]


def build(g, idx, s):
    head, header, footer, cta_block, ico, ROOT, SUBS = g["head"], g["header"], g["footer"], g["cta_block"], g["ico"], g["ROOT"], g["SUBSIDIARIES"]
    img = f"{BASE}assets/img/rheti"
    tick = lambda xs, cls="ticks": f'<ul class="{cls}">' + "".join(f"<li>{ico('check')}{e(x)}</li>" for x in xs) + "</ul>"
    r_glyph = f'<svg viewBox="100 53 52 56" fill="currentColor" aria-hidden="true">{g["R_PATH"]}</svg>'
    meaning = "".join(
        f'<li class="reveal" style="--d:{i * .07:.2f}s"><span>{r_glyph if k == "r" else ico(k)}</span><div><h3>{e(a)}</h3><p>{e(b)}</p></div></li>'
        for i, (k, a, b) in enumerate(LOGO_MEANING))
    essence = "".join(f'<div class="why__item reveal" style="--d:{i * .07:.2f}s"><div class="why__ico">{ico(a)}</div><h3>{e(b)}</h3><p>{e(c)}</p></div>' for i, (a, b, c) in enumerate(ESSENCE))
    what = "".join(f'<div class="rh-what reveal" style="--d:{(i % 2) * .08:.2f}s"><b>{i + 1:02d}</b><h3>{e(a)}</h3><p>{e(b)}</p></div>' for i, (a, b) in enumerate(WHAT_WE_DO))
    before = "".join(f'<li><span>{ico(a)}</span><p>Before you<br><b>{e(b)}</b> {e(c)}</p></li>' for a, b, c in BEFORE)
    stages = "".join(f'<li class="reveal" style="--d:{i * .08:.2f}s"><span>{ico(a)}</span><b>Stage {i + 1}</b><h3>{e(t)}</h3><p>{e(d)}</p></li>' for i, (a, t, d) in enumerate(STAGES))
    palette = "".join(f'<li><i style="background:{hx}"></i><b>{e(n)}</b><span>{hx}</span></li>' for n, hx in PALETTE)
    cur = ' aria-current="page"'
    siblings = "".join(f'<a href="{o["slug"]}.html"{cur if o is s else ""}>{o["name"]}</a>' for o in SUBS)
    nxt = SUBS[(idx + 1) % len(SUBS)]

    html = head("Rheti — Rehohub Training Institute | Knowledge. Practice. Impact.",
                "Rheti, the Rehohub Training Institute: skills acquisition, entrepreneurship training and business mentorship. Home of The Hack, 10 days to build a business that lasts.", BASE)
    html = html.replace("family=Kaushan+Script", "family=Poppins:wght@400;500;600;700;800").replace("<body>", '<body class="rh-body">')
    html += header(BASE)
    html += f'''<main id="main" class="theme-ar theme-rh">
<section class="ar-hero rh-hero">
  <div class="ar-hero__shield rh-shield" aria-hidden="true"></div>
  <div class="container ar-hero__inner">
    <div>
      <nav class="crumbs" aria-label="Breadcrumb"><a href="{BASE}index.html">Rehohub</a><span>/</span><a href="{BASE}index.html#services">Services</a><span>/</span><span aria-current="page">Rheti</span></nav>
      <img class="rh-hero__logo reveal" src="{img}/logo-light.png" alt="Rheti, Rehohub Training Institute: Knowledge. Practice. Impact. Learn, build, lead." width="900" height="467">
      <h1 class="reveal" style="--d:.08s">Knowledge.<br>Practice.<br><span class="gold">Impact.</span></h1>
      <p class="hero__lead reveal" style="--d:.16s">Rheti is the Rehohub Training Institute. We train people in practical skills, entrepreneurship and business mentorship, using technology and digital products, to reduce unemployment in Africa by making people more employable and more enterprising.</p>
      <div class="hero__ctas reveal" style="--d:.24s">
        <a class="btn btn--gold" href="#the-hack">Join The Hack {ico("arrow")}</a>
        <a class="btn btn--ghost" href="#what-we-do">What we teach</a>
      </div>
    </div>
    <div class="ar-hero__media reveal" style="--d:.2s">
      <div class="ar-hero__photo rh-photo"><img src="{img}/founder-thinking.jpg" alt="A young founder thinking through a business plan" width="384" height="580"></div>
      <div class="float-chip float-chip--a">{ico("spark")} 10 days to build smarter</div>
      <div class="float-chip ar-chip-gold">{ico("book")} Learn · Build · Lead</div>
    </div>
  </div>
</section>

<section class="rh-lbl-wrap"><div class="container"><ul class="rh-lbl reveal">
  <li><b>Learn</b><span>Practical skills, taught through real situations.</span></li>
  <li><b>Build</b><span>Businesses and careers that last.</span></li>
  <li><b>Lead</b><span>Leaders who create value in their communities.</span></li>
</ul></div></section>

<section class="section" id="what-we-do">
  <div class="container">
    <div class="section__head section__head--split">
      <div class="reveal"><span class="eyebrow">What we do</span><h2 class="title bar" style="margin-top:16px">Training that ends in action.</h2></div>
      <p class="lead reveal" style="--d:.1s">Rheti equips minds with practical skills and raises leaders who build impact. Every programme ends with something you can use: a skill, a plan or a business.</p>
    </div>
    <div class="rh-whats">{what}</div>
  </div>
</section>

<section class="section ar-dark rh-hack" id="the-hack">
  <div class="container">
    <div class="rh-hack__top">
      <div class="reveal">
        <span class="rh-hack__badge">{ico("spark")} The Hack<sup>®</sup></span>
        <h2 class="rh-hack__title">Before you build,<br><span class="gold">build right.</span></h2>
        <p class="lead" style="color:rgba(255,255,255,.82);margin-top:18px">The Hack is Rheti's 10-day programme on what it really takes to build a business. Build smarter. Build to last.</p>
        <ul class="rh-before">{before}</ul>
      </div>
      <div class="rh-hack__book reveal" style="--d:.1s">
        <img src="{img}/the-hack-book.jpg" alt="The Hack: 10 days to build a business that lasts. Idea, plan, build, grow. Build with purpose, grow with impact." width="343" height="510" loading="lazy">
      </div>
    </div>
    <div class="rh-question reveal">
      <span aria-hidden="true">?</span>
      <div><small>Ask yourself one question</small><p><b>Do I actually have a business</b>, or just an idea?</p></div>
    </div>
    <ol class="rh-stages">{stages}</ol>
    <div class="rh-join reveal">
      <div><h3>Welcome to <span class="gold">The Hack.</span></h3><p>Join the Business Builder List on WhatsApp to take part in the next 10 days, and follow {HANDLE} for daily business insights and practical strategies.</p></div>
      <a class="btn btn--gold" href="{HACK_LIST}" target="_blank" rel="noopener">{ico("chat")} Join the Business Builder List</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container rh-poster-row">
    <figure class="rh-poster reveal"><img src="{img}/the-hack-poster.jpg" alt="The Hack poster: Before you build, build right. Before you register that business, spend your savings, build the website or print the flyers, ask yourself: do I actually have a business, or just an idea?" width="1024" height="1536" loading="lazy"></figure>
    <div class="reveal" style="--d:.1s">
      <span class="eyebrow">Who The Hack is for</span>
      <h2 class="title bar" style="margin-top:16px">For anyone about to start.</h2>
      <p class="lead" style="margin-top:24px">If you're about to register a company, put your savings into a shop, pay for a website or print your first flyers, start here first. Ten days of focused thinking can save you months and money.</p>
      {tick(["Students and graduates with a business idea", "Side hustlers ready to go full-time", "First-time founders before they spend", "Small business owners who want to build to last"])}
      <div class="hero__ctas"><a class="btn" href="{HACK_LIST}" target="_blank" rel="noopener">Join on WhatsApp {ico("arrow")}</a></div>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="container">
    <div class="section__head" style="text-align:center;justify-items:center">
      <span class="eyebrow reveal">Brand essence</span>
      <h2 class="title bar bar--center reveal" style="--d:.08s">What Rheti stands for.</h2>
    </div>
    <div class="why">{essence}</div>
  </div>
</section>

<section class="section" id="our-mark">
  <div class="container show">
    <div class="reveal rh-mark-card"><img src="{img}/logo.png" alt="The Rheti logo: a shield holding the Rehohub R above an open book" width="900" height="467" loading="lazy">
      <ul class="rh-palette">{palette}</ul>
      <p class="rh-type"><b>Poppins Bold</b> for headlines · <span>Poppins Regular</span> for body text</p>
    </div>
    <div class="show__copy reveal" style="--d:.1s">
      <span class="eyebrow">Our mark</span>
      <h2 class="title bar" style="margin-top:16px">A shield, a book and the Rehohub R.</h2>
      <p class="lead" style="margin-top:24px">The Rheti logo joins the iconic R from the Rehohub family with a shield and an open book: knowledge, protection and transformation.</p>
      <ul class="rh-meaning">{meaning}</ul>
    </div>
  </div>
</section>

<section class="section section--tint" style="padding-top:clamp(48px,6vw,80px)">
  <div class="container">
    <div class="section__head" style="text-align:center;justify-items:center">
      <span class="eyebrow reveal">Rheti in the world</span>
      <h2 class="title bar bar--center reveal" style="--d:.08s">Recognisable everywhere we teach.</h2>
    </div>
    <figure class="rh-apps reveal"><img src="{img}/applications.jpg" alt="Rheti brand applications: app icon, stationery, student ID card, uniform and signage" width="920" height="180" loading="lazy"></figure>
  </div>
</section>

<section class="section">
  <div class="container rh-airise reveal">
    <img src="{BASE}assets/img/airise/mark.png" alt="" width="273" height="300">
    <div><span class="eyebrow">Looking for a job instead?</span><h2>Build your employability with AiRise.</h2><p>Rehohub's AiRise runs the nine-course Employability Skills Series and connects job-ready talent with employers.</p></div>
    <a class="btn" href="{BASE}products/airise/index.html">Explore AiRise {ico("arrow")}</a>
  </div>
</section>

<section class="section" style="padding-top:0;padding-bottom:0">
  <div class="container">
    <div class="section__head section__head--split">
      <div class="reveal"><span class="eyebrow">The Rehohub family</span><h2 class="title bar" style="margin-top:16px">Explore other services.</h2></div>
      <div class="reveal" style="--d:.1s"><a class="btn" href="{nxt["slug"]}.html">Next: {nxt["name"]} {ico("arrow")}</a></div>
    </div>
    <div class="siblings reveal">{siblings}</div>
  </div>
</section>

{cta_block(None, "Learn. Build.<br>Lead.", f"Want to train with Rheti, partner on a programme or bring The Hack to your school or organisation? Talk to us, and follow {HANDLE} for daily business insights.")}
</main>
'''
    html += footer(BASE)
    (ROOT / "services" / "rheti.html").write_text(html, encoding="utf-8")
