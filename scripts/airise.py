"""
AiRise mini-site: an HR company focused on the employability journey and training.

Generates products/airise/*.html from the AiRise documents:
  - AiRise Executive Summary          -> about.html, index.html
  - Draft A (AI+Rise requirements)    -> talent.html, employers.html, platform.html
  - Programme Overview                -> programme.html, course-*.html, facilitators.html
  - Assessment Pack (Facilitator Ed.) -> assessment.html (structure and rules only;
                                         answer keys and marking guides stay private)
  - Certificates                      -> certificates.html

Called from build.py: airise.build(globals())
"""
from html import escape

BASE = "../../"
WEB = "https://www.airise.com.ng/signup"
SOCIAL = "@airisenigeria"
INSTRUCTOR = "Joshua D. Obebe"

PHASES = [
    ("Respond", "Builds the habits of a professional."),
    ("Deliver", "Builds the ability to produce results with others."),
    ("Grow", "Builds the capacity to keep growing and to know yourself."),
]

COURSES = [
    dict(n=1, slug="adaptability", title="Adaptability", phase=1, hours=13,
         models=[("SHIFT", ["Sense the change", "Hold your reaction", "Investigate", "Fix a plan", "Track and tweak"])],
         use="Something changes and you need a calm, structured response.",
         ask="How do I cope when things change?",
         able="Respond to change with a clear method, recover from setbacks and keep learning.",
         dims=["Flexibility", "Resilience", "Openness", "Problem-solving"],
         signature="Real-world cases (Netflix, Kodak, Microsoft) and a scored self-assessment.",
         practice="Role-play module", builds=[],
         tools=["Four-step reset (Acknowledge, Separate, Act, Learn)", "STAR-L reflection (Situation, Task, Action, Result, Learning)", "SBI feedback (Situation, Behaviour, Impact)"],
         quiz="Components of adaptability, SHIFT, the reset, change stages, SBI and psychological safety."),
    dict(n=2, slug="initiative-and-proactivity", title="Initiative and Proactivity", phase=1, hours=16,
         models=[("SPARK", ["Spot the need", "Probe the facts and your authority", "Act on a safe first step", "Report early", "Keep going"])],
         use="You see a gap nobody owns and want to act without overstepping.",
         ask="What do I do when nobody tells me what to do?",
         able="Notice needs and act on them safely, within boundaries, and report early.",
         dims=["Anticipation", "Action", "Ownership", "Communication"],
         signature="The Initiative Ladder, three zones and worked workplace scenarios.",
         practice="Role-play module", builds=[1],
         tools=["Initiative Ladder and three zones (Green, Amber, Red)", "SIAA update (Situation, Impact, Action, Ask)"],
         quiz="The ladder, zones, SPARK, SIAA, the Impact Chain, motivation and boundaries."),
    dict(n=3, slug="communication-skills", title="Communication Skills", phase=1, hours=20,
         models=[("CLEAR", ["Context", "Lead with the main point", "Essential details", "Ask", "Read-back"]),
                 ("HEAR", ["Halt", "Engage", "Ask", "Repeat"])],
         use="You must be understood, or must truly understand.",
         ask="How do I make sure I am understood?",
         able="Speak, write, listen and give feedback clearly, and handle difficult conversations.",
         dims=["Clarity", "Listening", "Writing", "Presence"],
         signature="CLEAR and HEAR, with cases on trust, ambiguity and presentations.",
         practice="Role-play module", builds=[1, 2],
         tools=["DESC (Describe, Express, Specify, Consequences)", "SBI feedback"],
         quiz="CLEAR, HEAR, the non-verbal myth, channels, DESC, inference and stakeholders."),
    dict(n=4, slug="problem-solving", title="Problem-Solving", phase=2, hours=19,
         models=[("SOLVE", ["Spot and define", "Originate the causes", "List options", "Verify and choose", "Execute and evaluate"])],
         use="A problem keeps returning, or the cause is unclear.",
         ask="How do I find and fix the real problem?",
         able="Define problems, find root causes, choose and implement solutions, and measure results.",
         dims=["Defining", "Analysing", "Options", "Deciding and delivering"],
         signature="A running case, Greenfield Clinic, worked through SOLVE.",
         practice="Role-play module", builds=[1, 2, 3],
         tools=["5 Whys", "Fishbone diagram", "Decision matrix", "PDCA cycle"],
         quiz="Problem statements, 5 Whys, Pareto, the decision matrix, bias and interests."),
    dict(n=5, slug="work-ethics-and-reliability", title="Work Ethics and Reliability", phase=2, hours=21,
         models=[("KEEP", ["Know what was promised", "Estimate honestly", "Execute and track", "Proactively update and close"])],
         use="You make a commitment, or an ethical question arises.",
         ask="Can people count on me?",
         able="Keep commitments, act with integrity, own mistakes and earn trust.",
         dims=["Integrity", "Reliability", "Professionalism", "Ownership"],
         signature="Ethical dilemmas and the five-question integrity check.",
         practice="Practice activities", builds=[2, 3, 4],
         tools=["Five-question integrity check", "Four-part acknowledgement (Own it, Impact, Fix it, Prevent it)"],
         quiz="Accountability, the integrity check, KEEP, RAG status and above or below the line."),
    dict(n=6, slug="teamwork-and-collaboration", title="Teamwork and Collaboration", phase=2, hours=22,
         models=[("BUILD", ["Bond", "Unite around goals and roles", "Interact", "Lead and decide together", "Develop"])],
         use="You join, lead or repair a team.",
         ask="How do we achieve more together?",
         able="Build trust, share leadership, decide together and resolve conflict.",
         dims=["Contribution", "Communication", "Trust and conflict", "Inclusion and leadership"],
         signature="A running case, the Orbit Launch Team.",
         practice="Role-play module", builds=[1, 3, 4, 5],
         tools=["Team charter", "RACI and DACI", "Retrospective"],
         quiz="Team versus group, Project Aristotle, Tuckman, RACI, DACI, conflict and inclusion."),
    dict(n=7, slug="continuous-learning", title="Continuous Learning", phase=3, hours=20,
         models=[("LEARN", ["Locate the gap", "Establish goals and a plan", "Actively practise", "Reflect and get feedback", "Nurture the habit"])],
         use="You need a new skill or feel stuck.",
         ask="How do I keep growing?",
         able="Find skill gaps, plan and practise effectively, and learn from feedback.",
         dims=["Mindset", "Planning", "Practice", "Reflection and sharing"],
         signature="A running case, Amaka's learning year, with evidence-based study methods and templates.",
         practice="Practice activities", builds=[1, 2, 5],
         tools=["Retrieval practice", "Spacing", "Deliberate practice"],
         quiz="Evidence on learning styles, retrieval, output goals, the CRAAP test and deliberate practice."),
    dict(n=8, slug="networking-and-interpersonal-skills", title="Networking and Interpersonal Skills", phase=3, hours=21,
         models=[("BRIDGE", ["Brand", "Reach out", "Interact well", "Deepen", "Go beyond barriers", "Evaluate and sustain"])],
         use="You want to build relationships that open doors.",
         ask="Who will I grow with, and who will help me?",
         able="Build honest, lasting professional relationships, online and in person.",
         dims=["Mindset and purpose", "Presence", "Conversation and listening", "Follow-through and giving"],
         signature="A running case, Chidera's networking year, with message templates.",
         practice="Conversation practice", builds=[3, 5, 6, 7],
         tools=["Elevator pitch", "Follow-up message templates"],
         quiz="Weak ties, the pitch, follow-up, scams, graded exposure and feedforward."),
    dict(n=9, slug="self-awareness", title="Self-Awareness", phase=3, hours=21,
         models=[("SELF", ["See yourself clearly", "Engage your emotions", "Learn from others' views", "Follow through"])],
         use="You want to understand your impact and align action with values.",
         ask="Who am I, and how do I come across?",
         able="Know their values, strengths, emotions and blind spots, and act on them.",
         dims=["Self-knowledge", "Emotional awareness", "Openness to others", "Reflection and alignment"],
         signature="A running case, Zainab's turning point, with reflection tools and a personal operating manual.",
         practice="Personal exercises", builds=[1, 2, 3, 4, 5, 6, 7, 8],
         tools=["STOP pause", "Johari Window", "WOOP", "Personal operating manual"],
         quiz="Internal and external awareness, what versus why, STOP, ABC, Johari and WOOP."),
]

JOURNEY = [
    ("user", "Register", "Sign up with email or a third-party account, verify your email and set a password."),
    ("id", "Build your profile", "Add your bio, contacts and education, upload your documents and an official headshot. You get a reference ID."),
    ("book", "Learn", "Take the nine-course Employability Skills Series, at your own pace or in a cohort."),
    ("check", "Get assessed", "Course quizzes, a proctored final assessment and a practical role-play show what you can do."),
    ("rise", "Get ranked", "Your results and skills place you in the AiRise talent pool, ranked by job heading."),
    ("chat", "Interview", "AiRise schedules and organises interviews with employers looking for your skills."),
    ("briefcase", "Get placed", "Internships and SIWES, graduate jobs and managerial roles with partner employers."),
    ("refresh", "Keep growing", "Request reactivation when you want a new role or a career change."),
]

TALENT_TIERS = [
    ("Undergraduates", "Looking for internships or SIWES placements."),
    ("Graduates", "Looking for their first job or a better one."),
    ("Master's and above", "Experienced people looking for managerial roles."),
    ("Current employees", "Looking to grow their productivity through training and practical experience."),
]

HR_SERVICES = [
    ("search", "Recruitment and selection", "We find, screen and shortlist candidates who are ready to work."),
    ("chat", "Job interviews", "We organise and run interviews, so your team only meets the best fits."),
    ("chart", "Employee appraisal", "Structured performance reviews that are fair and easy to act on."),
    ("rise", "Productivity enhancement", "Practical programmes that lift performance in your existing team."),
    ("book", "Training and development", "The Employability Skills Series and targeted workshops for your staff."),
    ("users", "Development and retention", "Keep good people longer by investing in how they grow."),
]

EMPLOYER_FLOW = [
    ("Register your organisation", "Create an account for your start-up or multinational."),
    ("Search the talent pool", "Search by job heading and ranking, then cross-reference skills."),
    ("Request folders", "Pay for access to the folders of the candidates you want to see."),
    ("Interview", "AiRise organises interviews with your shortlist."),
    ("Hire", "Make a one-time employee request and agree the contract."),
    ("Develop and retain", "Use appraisal and training to keep your new hires growing."),
]

ADMIN_FUNCS = ["Access and manage the employee pool", "Monitor each learner's growth", "Send automated emails to people in the learning process",
               "Proctor examinations", "Organise interviews", "Update rankings automatically", "Talk to organisations in the chat room", "Provide support in the chat room"]

TALENT_FUNCS = ["Register, log in and verify by email", "Update profile, bio, contacts and education", "Upload required documents",
                "Get a reference ID with an official headshot", "Request opportunities", "Learn soft skills", "Take examinations",
                "Schedule interview calls", "Apply for jobs", "Request reactivation for a career or job change"]

EMPLOYER_FUNCS = ["Register and log in", "Assess the talent pool", "Search by job heading", "Advanced search by ranking and job heading",
                  "Cross-reference skills", "Pay for targeted employee folder access", "Request folders", "Make a one-time employee request", "Manage contracts"]

MODULES = [
    ("lock", "Accounts and verification", "Email or third-party sign-up, email verification, secure passwords."),
    ("id", "Profiles and reference IDs", "Bio, education, documents and headshot; a unique reference ID for each person."),
    ("book", "Learning", "The nine courses, about 140 modules, journals, trackers and 90-day plans."),
    ("check", "Assessment and proctoring", "Course quizzes, the four-part final assessment and practical role-plays."),
    ("rise", "Ranking engine", "Turns results, skills and progress into a ranking by job heading."),
    ("search", "Talent pool search", "Search, filter and cross-reference skills for employers."),
    ("wallet", "Folder access and payments", "Pay for targeted candidate folders and one-time requests."),
    ("calendar", "Interview scheduling", "Book interview calls between talent, employers and AiRise."),
    ("plan", "Contracts", "Agree and track the terms of each placement."),
    ("chat", "Chat and support", "A chat room connecting employers, talent and AiRise admins."),
    ("mail", "Automated emails", "Reminders and updates for everyone in the learning process."),
    ("star", "Certificates and verification", "Issue numbered certificates and let employers verify them."),
]

DELIVERY = [
    ("A", "Part-time cohort", "About 9 months", "One course a month: self-study plus a fortnightly facilitated session.", "About 5 hours a week", "Employees; community and professional bodies"),
    ("B", "Blended", "About 18 weeks", "One course every two weeks: weekly workshop plus self-study.", "About 10 hours a week", "Graduate trainee programmes; training academies"),
    ("C", "Intensive", "About 12 weeks", "A cohort with daily or near-daily sessions.", "About 14 to 15 hours a week", "Pre-employment bootcamps; final-year programmes"),
    ("D", "One phase only", "49 to 62 hours", "Phase 1 (about 49 hours), Phase 2 (about 62) or Phase 3 (about 62).", "As agreed", "Targeted needs; short sponsored programmes"),
    ("E", "Single course", "13 to 22 hours", "Any one course on its own.", "As agreed", "A specific skills gap; corporate workshops"),
    ("F", "Self-paced", "Flexible", "Learners work alone with an accountability partner.", "Flexible", "Remote or independent learners"),
]

EVERY_COURSE = [
    ("Assess", "Complete the 12-statement self-assessment and compare it with an outside view."),
    ("Learn and practise", "Work through the modules, practice activities and role-plays."),
    ("Apply", "Use the course's model on a real situation at work or study."),
    ("Plan", "Write a 90-day action plan with measurable goals."),
    ("Stay accountable", "Agree a partner, track a few measures and review weekly."),
    ("Reflect and complete", "Finish the course checklist and choose one habit to carry forward."),
]

COURSE_PARTS = [
    ("Opening situation", "A short real-life scene that shows why the skill matters."),
    ("Learning objectives", "What you will be able to do after the module."),
    ("Core ideas and tables", "Plain-language definitions, models, comparisons and checklists."),
    ("Worked examples", "Real-world cases and composite workplace examples."),
    ("Practice activities", "Tasks for individuals, pairs and groups."),
    ("Takeaway and \"Ask yourself\"", "The one idea to use tomorrow, and a reflective prompt."),
    ("Check questions", "Four questions per module, with hints."),
    ("Action planning", "A 90-day plan with goals, partner, measures and review rhythm."),
]

SESSION = [("0:00", "Check-in", "Partners report on their 90-day plan and last week's practice."),
           ("0:20", "Teach and discuss", "Key ideas, the model and one case."),
           ("1:10", "Break", ""),
           ("1:20", "Practice", "Activities, role-plays or conversations in small groups, with SBI feedback from observers."),
           ("2:30", "Plan", "Each learner commits to one action to try this week."),
           ("2:50", "Close", "A one-sentence reflection and next steps.")]

FACILITATOR_TIPS = [
    ("Prepare", "Read the course and the trainer notes, check real-world cases against original sources, and adapt names and examples to your learners."),
    ("Group size", "About 12 to 25 learners, split into groups of 3 to 5 for activities."),
    ("Create safety", "Agree ground rules on confidentiality, voluntary sharing and respect, especially for Self-Awareness, Teamwork and Work Ethics."),
    ("Insist on practice", "Keep teaching short and practice long. Most skills are learned by doing."),
    ("Use accountability partners", "Pair learners from the start; partners are central to follow-through."),
    ("Link to real work", "Ask learners to bring a live situation to each session, with confidentiality respected."),
]

CHECKLIST = ["Choose the delivery option and schedule", "Read the first course and its trainer notes; verify cases and adapt examples",
             "Set ground rules for confidentiality and voluntary sharing", "Pair learners as accountability partners",
             "Prepare learner packs: guide, journal, tracker, templates", "Plan baseline self-assessments and outside-view requests",
             "Book check-in sessions and the end-of-programme review"]

PAGES = [("index", "Overview"), ("talent", "For talent"), ("employers", "For employers"), ("programme", "Programme"),
         ("assessment", "Assessment"), ("certificates", "Certificates"), ("facilitators", "Facilitators"), ("platform", "Platform"), ("about", "About")]


def build(g):
    head, header, footer, cta_block, ico, r_mark, ROOT = g["head"], g["header"], g["footer"], g["cta_block"], g["ico"], g["r_mark"], g["ROOT"]
    out_dir = ROOT / "products" / "airise"
    out_dir.mkdir(parents=True, exist_ok=True)
    img = f"{BASE}assets/img/airise"
    e = escape
    tick = lambda xs, cls="ticks": f'<ul class="{cls}">' + "".join(f"<li>{ico('check')}{e(x)}</li>" for x in xs) + "</ul>"
    course_href = lambda c: f"course-{c['slug']}.html"
    lc = lambda t: t if t[:2].isupper() else t[0].lower() + t[1:]

    def subnav(active):
        cur = ' aria-current="page"'
        links = "".join(f'<a href="{k}.html"{cur if k == active else ""}>{v}</a>' for k, v in PAGES)
        return f'''<nav class="ar-nav" aria-label="AiRise">
  <div class="container ar-nav__inner">
    <a class="ar-nav__brand" href="index.html"><img src="{img}/mark.png" alt="" width="273" height="300"><span>AiRise</span></a>
    <div class="ar-nav__links">{links}</div>
    <a class="btn btn--gold ar-nav__cta" href="{WEB}" target="_blank" rel="noopener">Sign up free</a>
  </div>
</nav>'''

    def page(slug, title, desc, body, extra_js=False):
        html = head(f"{title} | AiRise", desc, BASE).replace("<body>", '<body class="ar-body">')
        html += header(BASE, solid=True)
        html += f'<main id="main" class="product-page theme-ar">\n{subnav(slug)}\n{body}\n'
        html += cta_block(None, "Ready to rise?", "Whether you're looking for your next role or your next hire, AiRise is the bridge. Talk to us.")
        html += "</main>\n"
        if extra_js:
            html += f'<script src="{BASE}assets/js/airise.js" defer></script>\n'
        html += footer(BASE)
        (out_dir / f"{slug}.html").write_text(html, encoding="utf-8")

    def hero(eyebrow, title, lead, ctas="", media="", cls=""):
        return f'''<section class="ar-hero {cls}">
  <div class="ar-hero__shield" aria-hidden="true"></div>
  <div class="container ar-hero__inner{' ar-hero__inner--solo' if not media else ''}">
    <div>
      <nav class="crumbs" aria-label="Breadcrumb"><a href="{BASE}index.html">Rehohub</a><span>/</span><a href="{BASE}index.html#products">Products</a><span>/</span><a href="index.html">AiRise</a></nav>
      <span class="ar-kicker reveal">{e(eyebrow)}</span>
      <h1 class="reveal" style="--d:.08s">{title}</h1>
      <p class="hero__lead reveal" style="--d:.16s">{lead}</p>
      {f'<div class="hero__ctas reveal" style="--d:.24s">{ctas}</div>' if ctas else ''}
    </div>
    {media}
  </div>
</section>'''

    def head2(eyebrow, title, lead="", center=False, light=False):
        if center:
            return f'''<div class="section__head" style="text-align:center;justify-items:center">
      <span class="eyebrow{' eyebrow--light' if light else ''} reveal">{e(eyebrow)}</span>
      <h2 class="title{' title--light' if light else ''} bar bar--center{' bar--light' if light else ''} reveal" style="--d:.08s">{title}</h2>
      {f'<p class="lead reveal" style="--d:.14s">{lead}</p>' if lead else ''}
    </div>'''
        return f'''<div class="section__head section__head--split">
      <div class="reveal"><span class="eyebrow{' eyebrow--light' if light else ''}">{e(eyebrow)}</span><h2 class="title{' title--light' if light else ''} bar{' bar--light' if light else ''}" style="margin-top:16px">{title}</h2></div>
      {f'<p class="lead reveal" style="--d:.1s">{lead}</p>' if lead else '<span></span>'}
    </div>'''

    def model_block(c, big=False):
        out = ""
        for name, words in c["models"]:
            letters = "".join(f'<li><b>{w[0]}</b><span>{e(w)}</span></li>' for w in words)
            out += f'<div class="ar-model{" ar-model--big" if big else ""}"><strong>{name}</strong><ol>{letters}</ol></div>'
        return out

    def course_card(c, i=0):
        names = " and ".join(m[0] for m in c["models"])
        return f'''<a class="ar-course reveal" style="--d:{(i % 3) * .07:.2f}s" href="{course_href(c)}" data-phase="{c["phase"]}">
        <span class="ar-course__n">{c["n"]:02d}</span>
        <span class="ar-course__phase">Phase {c["phase"]} · {PHASES[c["phase"] - 1][0]}</span>
        <h3>{e(c["title"])}</h3>
        <span class="ar-course__model">{names}</span>
        <p>“{e(c["ask"])}”</p>
        <span class="ar-course__meta">{ico("clock")} About {c["hours"]} hours <i>{ico("arrow-ne")}</i></span>
      </a>'''

    journey_html = "".join(
        f'<li class="reveal" style="--d:{i * .05:.2f}s"><span class="ar-journey__ico">{ico(ic)}</span><b>{i + 1:02d}</b><h3>{e(t)}</h3><p>{e(d)}</p></li>'
        for i, (ic, t, d) in enumerate(JOURNEY))

    phases_html = ""
    for i, (pname, pdesc) in enumerate(PHASES):
        items = "".join(f'<li><a href="{course_href(c)}">{e(c["title"])}</a></li>' for c in COURSES if c["phase"] == i + 1)
        phases_html += f'<div class="ar-phase reveal" style="--d:{i * .08:.2f}s"><span>Phase {i + 1}</span><h3>{pname}</h3><p>{e(pdesc)}</p><ul>{items}</ul></div>'

    # ------------------------------------------------------------------ index
    body = hero("Human resource solutions · Lagos pilot launch",
                'Skills today.<br><span class="gold">Opportunities</span><br>tomorrow.',
                "AiRise is an HR company that closes the gap between talent and opportunity. We train people to be job-ready, match them with employers, and help organisations hire, develop and keep great people.",
                f'<a class="btn btn--gold" href="{WEB}" target="_blank" rel="noopener">Sign up for free {ico("arrow")}</a><a class="btn btn--ghost" href="employers.html">I\'m hiring</a>',
                f'''<div class="ar-hero__media reveal" style="--d:.2s">
      <div class="ar-hero__photo"><img src="{img}/student.jpg" alt="A smiling student holding a laptop" width="501" height="473"></div>
      <img class="ar-hero__badge" src="{img}/logo.png" alt="AiRise: Learn. Grow. Lead." width="700" height="686">
      <div class="float-chip float-chip--a">{ico("briefcase")} Verified internships and jobs</div>
      <div class="float-chip ar-chip-gold">{ico("star")} 9 courses · 3 phases</div>
    </div>''')
    body += f'''
<section class="ar-split-wrap">
  <div class="container ar-split">
    <a class="ar-split__card reveal" href="talent.html">
      <span class="ar-split__tag">For talent</span>
      <h2>Stand out, get noticed and get hired.</h2>
      <p>Employers want more than degrees. They want proven skills, real experience and the right attitude. AiRise helps you build all three.</p>
      {tick(["Skill courses and certificates", "Verified internships and job opportunities", "Career matching and CV review", "Mentorship and coaching"])}
      <span class="ar-split__go">Start your journey {ico("arrow")}</span>
    </a>
    <a class="ar-split__card ar-split__card--dark reveal" style="--d:.1s" href="employers.html">
      <span class="ar-split__tag">For employers</span>
      <h2>Hire people who are ready on day one.</h2>
      <p>Get HR when you need it, without the cost of an in-house HR department. Find ranked, assessed candidates and develop the team you have.</p>
      {tick(["Recruitment and selection", "Interviews and appraisal", "Training and development", "Retention and productivity"], "ticks ticks--light")}
      <span class="ar-split__go">Find talent {ico("arrow")}</span>
    </a>
  </div>
</section>

<section class="section ar-problem">
  <div class="container ar-problem__inner">
    <div class="reveal"><strong class="ar-big">26M+</strong><p>Nigerian graduates are affected by unemployment, with similar challenges across Africa.</p></div>
    <div class="reveal" style="--d:.1s"><span class="eyebrow">Why AiRise</span><h2 class="title bar" style="margin-top:16px">Talent is everywhere. Opportunity isn't, yet.</h2>
      <p class="lead" style="margin-top:22px">Organisations struggle with high turnover while millions of graduates wait for a chance. AiRise develops talent from the post-secondary level with training, internships and skills, so employers get a steady flow of prepared candidates and lower turnover.</p></div>
  </div>
</section>

<section class="section section--tint" id="journey">
  <div class="container">
    {head2("The employability journey", "From sign-up<br>to your next role.", "Eight steps take you from creating your profile to getting placed, and keep you growing after that.")}
    <ol class="ar-journey">{journey_html}</ol>
  </div>
</section>

<section class="section ar-dark" id="programme">
  <div class="container">
    {head2("Employability Skills Series", "Nine courses.<br>Three phases.", "", light=True)}
    <div class="ar-phases">{phases_html}</div>
    <div class="ar-stats reveal">
      <div><strong>9</strong><span>Courses</span></div><div><strong>~140</strong><span>Modules</span></div>
      <div><strong>~173</strong><span>Hours of study</span></div><div><strong>90-day</strong><span>Action plan per course</span></div>
    </div>
    <div class="hero__ctas" style="justify-content:center"><a class="btn btn--gold" href="programme.html">Explore the programme {ico("arrow")}</a></div>
  </div>
</section>

<section class="section" id="services">
  <div class="container">
    {head2("HR services", "Need-based HR<br>for growing teams.", "Instead of a recurring in-house HR department, use AiRise for exactly what you need, when you need it.")}
    <div class="why ar-services">{"".join(f'<div class="why__item reveal" style="--d:{(i % 3) * .08:.2f}s"><div class="why__ico">{ico(a)}</div><h3>{e(b)}</h3><p>{e(c)}</p></div>' for i, (a, b, c) in enumerate(HR_SERVICES))}</div>
  </div>
</section>

<section class="section section--tint">
  <div class="container ar-offer reveal">
    <div><span class="ar-offer__tag">Launch offer</span><strong>100% free</strong><p>for the first 1,000 students. Valid for the first 30 days of launch.</p></div>
    <div><h2>Your career journey starts now.</h2><p>Built for students. Backed by employers. Join the Lagos pilot launch.</p>
      <div class="hero__ctas"><a class="btn btn--gold" href="{WEB}" target="_blank" rel="noopener">Sign up for free {ico("arrow")}</a><span class="ar-offer__url">{ico("web")} www.airise.com.ng/signup · {SOCIAL}</span></div></div>
    <img src="{img}/flyer.jpg" alt="AiRise Lagos pilot launch flyer: Skills today, opportunities tomorrow" loading="lazy" width="1086" height="1448">
  </div>
</section>'''
    page("index", "Skills today, opportunities tomorrow", "AiRise is an HR company focused on employability: training, assessment, talent matching and HR services for employers.", body)

    # ------------------------------------------------------------------ talent
    body = hero("For talent", 'Get job-ready.<br><span class="gold">Get hired.</span>',
                "Whether you're a student looking for SIWES, a graduate looking for your first job or an experienced professional ready to lead, AiRise trains you, proves your skills and connects you to employers.",
                f'<a class="btn btn--gold" href="{WEB}" target="_blank" rel="noopener">Create your profile {ico("arrow")}</a><a class="btn btn--ghost" href="programme.html">See the courses</a>')
    body += f'''
<section class="section">
  <div class="container">
    {head2("Who it's for", "Wherever you are<br>in your career.")}
    <div class="ar-tiers">{"".join(f'<div class="ar-tier reveal" style="--d:{i * .07:.2f}s"><h3>{e(a)}</h3><p>{e(b)}</p></div>' for i, (a, b) in enumerate(TALENT_TIERS))}</div>
  </div>
</section>
<section class="section section--tint">
  <div class="container">
    {head2("Your journey", "Eight steps<br>to your next role.")}
    <ol class="ar-journey">{journey_html}</ol>
  </div>
</section>
<section class="section">
  <div class="container show">
    <div class="show__copy reveal">
      <span class="eyebrow">Your AiRise profile</span>
      <h2 class="title bar" style="margin-top:16px">One profile that speaks for you.</h2>
      <p class="lead" style="margin-top:24px">Your profile brings together your education, documents, course results and certificates. Employers see a ranked, verified picture of what you can do.</p>
      {tick(TALENT_FUNCS, "ticks ticks--grid")}
    </div>
    <div class="show__media reveal" style="--d:.1s" aria-hidden="true">
      <div class="ar-profile">
        <div class="ar-profile__top"><span class="ar-avatar">AO</span><div><b>Amaka Okafor</b><small>Ref ID · AIR-T-000482</small></div><span class="ar-rank">Rank #12<br><small>Data Analyst</small></span></div>
        <div class="ar-profile__row"><span>Programme progress</span><b>6 of 9 courses</b></div>
        <div class="ar-bar"><i style="width:67%"></i></div>
        <div class="ar-profile__chips"><span class="on">SHIFT ✓</span><span class="on">SPARK ✓</span><span class="on">CLEAR ✓</span><span class="on">SOLVE ✓</span><span class="on">KEEP ✓</span><span class="on">BUILD ✓</span><span>LEARN</span><span>BRIDGE</span><span>SELF</span></div>
        <div class="ar-profile__row"><span>Documents</span><b class="ok">Verified</b></div>
        <div class="ar-profile__row"><span>Next</span><b>Interview · Thu 10:00</b></div>
      </div>
    </div>
  </div>
</section>
<section class="section ar-dark">
  <div class="container">
    {head2("Everything you need", "All in one place.", "", center=True, light=True)}
    <div class="ar-feats">{"".join(f'<div class="reveal" style="--d:{i * .06:.2f}s"><span>{ico(a)}</span><h3>{b}</h3></div>' for i, (a, b) in enumerate([("book", "Skill courses &amp; certifications"), ("briefcase", "Verified internships &amp; job opportunities"), ("search", "Career matching &amp; CV review"), ("users", "Mentorship &amp; coaching"), ("plan", "Career resources &amp; templates"), ("star", "Build. Learn. Get hired.")]))}</div>
  </div>
</section>'''
    page("talent", "For talent", "Get job-ready and hired with AiRise: training, assessment, a verified profile and connections to employers.", body)

    # ------------------------------------------------------------------ employers
    flow = "".join(f'<li class="reveal" style="--d:{i * .06:.2f}s"><span>{i + 1}</span><div><h3>{e(a)}</h3><p>{e(b)}</p></div></li>' for i, (a, b) in enumerate(EMPLOYER_FLOW))
    body = hero("For employers", 'HR when you need it.<br><span class="gold">Talent that\'s ready.</span>',
                "AiRise is your bridge to assessed, ranked candidates who need little or no training beyond your own onboarding. Use our HR services as you need them, without the cost of a full in-house HR department.",
                f'<a class="btn btn--gold" href="#contact">Talk to our team {ico("arrow")}</a><a class="btn btn--ghost" href="#hire">How hiring works</a>')
    body += f'''
<section class="section">
  <div class="container">
    {head2("HR services", "Everything HR,<br>on demand.", "From the first interview to long-term retention, pick the services your organisation needs.")}
    <div class="why ar-services">{"".join(f'<div class="why__item reveal" style="--d:{(i % 3) * .08:.2f}s"><div class="why__ico">{ico(a)}</div><h3>{e(b)}</h3><p>{e(c)}</p></div>' for i, (a, b, c) in enumerate(HR_SERVICES))}</div>
  </div>
</section>
<section class="section section--tint" id="hire">
  <div class="container show">
    <div class="show__copy reveal">
      <span class="eyebrow">How hiring works</span>
      <h2 class="title bar" style="margin-top:16px">From search to signed contract.</h2>
      <p class="lead" style="margin-top:24px">Every candidate in the AiRise talent pool has been trained and assessed. Search by the job you're hiring for and see who ranks highest.</p>
    </div>
    <ol class="ar-flow">{flow}</ol>
  </div>
</section>
<section class="section">
  <div class="container show show--flip">
    <div class="show__copy reveal">
      <span class="eyebrow">Train your team</span>
      <h2 class="title bar" style="margin-top:16px">Develop the people you already have.</h2>
      <p class="lead" style="margin-top:24px">The Employability Skills Series is built for current employees as well as new graduates. Run a single course as a corporate workshop, one phase for a targeted need, or the full series as a graduate trainee programme.</p>
      <div class="hero__ctas"><a class="btn" href="programme.html">See the programme {ico("arrow")}</a><a class="btn btn--outline" href="facilitators.html">Delivery options</a></div>
    </div>
    <div class="show__media reveal" style="--d:.1s">
      <div class="ar-why-card">
        <h3>Why it works</h3>
        {tick(["A steady flow of qualified candidates suited to your needs", "Lower turnover and better performance", "Pay for the service you need, not a whole department", "Certificates you can verify by number"])}
      </div>
    </div>
  </div>
</section>'''
    page("employers", "For employers", "Hire assessed, ranked talent and use AiRise HR services on demand: recruitment, interviews, appraisal, training and retention.", body)

    # ------------------------------------------------------------------ programme
    models_table = "".join(
        f'<tr><td>{c["n"]}</td><td><a href="{course_href(c)}">{e(c["title"])}</a></td><td><b>{" and ".join(m[0] for m in c["models"])}</b></td><td>{e("; ".join(", ".join(m[1]) for m in c["models"]))}</td><td>{e(c["use"])}</td></tr>'
        for c in COURSES)
    body = hero("AiRise Employability Skills Series", 'Start, hold and<br><span class="gold">grow a career.</span>',
                f"A nine-course programme for current employees, new graduates and prospective talent, taught by instructor {INSTRUCTOR}. Each course teaches a practical skill through real situations, worked examples, practice and action planning.",
                f'<a class="btn btn--gold" href="{WEB}" target="_blank" rel="noopener">Enrol for free {ico("arrow")}</a><a class="btn btn--ghost" href="#courses">Browse courses</a>')
    body += f'''
<section class="ar-stats-wrap"><div class="container"><div class="ar-stats ar-stats--light reveal">
  <div><strong>9</strong><span>Courses in 3 phases</span></div><div><strong>~140</strong><span>Modules</span></div>
  <div><strong>~173</strong><span>Hours, 13 to 22 per course</span></div><div><strong>~520</strong><span>Pages of course guides</span></div>
</div></div></section>

<section class="section" id="courses">
  <div class="container">
    {head2("The courses", "Respond. Deliver. Grow.", "Phase 1 builds the habits of a professional, Phase 2 the ability to produce results with others, and Phase 3 the capacity to keep growing and to know yourself.")}
    <div class="ar-tabs" role="tablist" aria-label="Filter courses by phase">
      <button role="tab" aria-selected="true" data-filter="all">All courses</button>
      {"".join(f'<button role="tab" aria-selected="false" data-filter="{i + 1}">Phase {i + 1}: {p}</button>' for i, (p, _) in enumerate(PHASES))}
    </div>
    <div class="ar-courses" data-courses>{"".join(course_card(c, i) for i, c in enumerate(COURSES))}</div>
  </div>
</section>

<section class="section section--tint">
  <div class="container">
    {head2("In every course", "Six things you'll do<br>every time.", "Every course follows the same rhythm, so you always know what to expect.")}
    <ol class="ar-every">{"".join(f'<li class="reveal" style="--d:{i * .06:.2f}s"><b>{i + 1}</b><h3>{e(a)}</h3><p>{e(b)}</p></li>' for i, (a, b) in enumerate(EVERY_COURSE))}</ol>
    <p class="ar-note reveal">In the final module of the last course, you bring all nine models together in a personal operating manual and choose one habit per quarter to keep practising.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    {head2("The nine models", "One memorable model<br>per course.", "Easy to remember and to use in the moment. Keep this table beside your desk.")}
    <div class="ar-table-wrap reveal"><table class="ar-table"><thead><tr><th>#</th><th>Course</th><th>Model</th><th>What the letters stand for</th><th>Use it when…</th></tr></thead><tbody>{models_table}</tbody></table></div>
  </div>
</section>

<section class="section section--tint">
  <div class="container show">
    <div class="show__copy reveal">
      <span class="eyebrow">How each course is built</span>
      <h2 class="title bar" style="margin-top:16px">A working guide, not a textbook.</h2>
      <p class="lead" style="margin-top:24px">Each module has objectives, a worked example, a practice activity, a takeaway and check questions. Later courses reuse earlier tools, so by the end you're applying nine connected models.</p>
    </div>
    <div class="ar-parts reveal" style="--d:.1s">{"".join(f'<div><h4>{e(a)}</h4><p>{e(b)}</p></div>' for a, b in COURSE_PARTS)}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    {head2("Measuring progress", "Know where you stand.", "Every course starts with the same kind of self-assessment, so you get a consistent baseline across all nine.")}
    <div class="ar-bands reveal">
      <div class="ar-bands__how"><h3>12 statements, rated 1 to 5</h3><p>Four dimensions of three statements each. Each dimension scores 3 to 15, and the total runs from 12 to 60. Ask two or three people to rate you on the same statements, then re-take it after your 90-day plan.</p></div>
      <div class="ar-band ar-band--strong"><strong>12–15</strong><span>Strong</span></div>
      <div class="ar-band ar-band--dev"><strong>8–11</strong><span>Developing</span></div>
      <div class="ar-band ar-band--pri"><strong>3–7</strong><span>Priority area</span></div>
    </div>
    <div class="hero__ctas"><a class="btn" href="assessment.html">How assessments work {ico("arrow")}</a><a class="btn btn--outline" href="certificates.html">Certificates</a></div>
  </div>
</section>'''
    page("programme", "Employability Skills Series", "Nine courses in three phases (Respond, Deliver, Grow), each with a memorable model, a self-assessment and a 90-day action plan.", body, extra_js=True)

    # ------------------------------------------------------------------ courses
    for i, c in enumerate(COURSES):
        prev_c = COURSES[i - 1] if i > 0 else None
        next_c = COURSES[i + 1] if i < len(COURSES) - 1 else None
        names = " and ".join(m[0] for m in c["models"])
        builds = "".join(f'<a href="{course_href(COURSES[b - 1])}">{e(COURSES[b - 1]["title"])}</a>' for b in c["builds"]) or '<span class="ar-muted">This is where the series starts.</span>'
        dims = "".join(f'<li><b>{e(d)}</b><span>3 statements · 3–15</span></li>' for d in c["dims"])
        body = hero(f"Course {c['n']} of 9 · Phase {c['phase']}: {PHASES[c['phase'] - 1][0]}",
                    e(c["title"]) + '<span class="gold">.</span>',
                    f"“{e(c['ask'])}” By the end, you'll be able to {e(lc(c['able']))}",
                    f'<a class="btn btn--gold" href="{WEB}" target="_blank" rel="noopener">Start this course {ico("arrow")}</a><a class="btn btn--ghost" href="programme.html#courses">All courses</a>',
                    f'<div class="ar-hero__model reveal" style="--d:.2s">{model_block(c, big=True)}</div>')
        body += f'''
<section class="ar-stats-wrap"><div class="container"><div class="ar-stats ar-stats--light reveal">
  <div><strong>~{c["hours"]}h</strong><span>Study time incl. activities</span></div><div><strong>{names}</strong><span>Core model</span></div>
  <div><strong>12</strong><span>Self-assessment statements</span></div><div><strong>90-day</strong><span>Action plan</span></div>
</div></div></section>

<section class="section">
  <div class="container show">
    <div class="show__copy reveal">
      <span class="eyebrow">The model</span>
      <h2 class="title bar" style="margin-top:16px">Use {names} when…</h2>
      <p class="lead" style="margin-top:24px">{e(c["use"])}</p>
      <p style="margin-top:18px;color:var(--ink-soft)">{e(c["signature"])}</p>
      <h3 class="ar-h3">Tools you'll pick up</h3>
      {tick(c["tools"])}
    </div>
    <div class="reveal" style="--d:.1s">
      <div class="ar-why-card ar-ask">
        <small>You start by asking</small><p class="ar-ask__q">“{e(c["ask"])}”</p>
        <small>You leave able to</small><p>{e(c["able"])}</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="container ar-course-grid">
    <div class="reveal">
      <span class="eyebrow">Self-assessment</span>
      <h2 class="title bar" style="margin-top:16px">Four dimensions you'll measure.</h2>
      <ul class="ar-dims">{dims}</ul>
    </div>
    <div class="reveal" style="--d:.1s">
      <span class="eyebrow">How you'll learn</span>
      <h2 class="title bar" style="margin-top:16px">Practice, not theory.</h2>
      {tick([c["practice"] + " with trainer notes for facilitators", "Worked real-world and illustrative cases", "Four check questions per module", "A 90-day action plan with an accountability partner"])}
      <h3 class="ar-h3">Builds on</h3>
      <div class="ar-links">{builds}</div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container ar-assess-strip reveal">
    <div><span class="eyebrow">Course assessment</span><h2>Pass the quiz, earn the certificate.</h2>
      <p>The quiz covers {e(lc(c["quiz"]))}</p></div>
    <ul>
      <li><b>Section A</b><span>10 multiple-choice questions · 10 minutes</span></li>
      <li><b>Section B</b><span>A realistic scenario using {names} · 20 minutes</span></li>
      <li><b>Pass mark</b><span>14 out of 20 (70%) · 18+ is a distinction</span></li>
    </ul>
    <a class="btn" href="certificates.html">About certificates {ico("arrow")}</a>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="container ar-pager">
    {f'<a href="{course_href(prev_c)}"><small>← Previous course</small><b>{e(prev_c["title"])}</b></a>' if prev_c else '<a href="programme.html"><small>← Back to</small><b>The programme</b></a>'}
    {f'<a class="next" href="{course_href(next_c)}"><small>Next course →</small><b>{e(next_c["title"])}</b></a>' if next_c else '<a class="next" href="assessment.html"><small>Next →</small><b>Final assessment</b></a>'}
  </div>
</section>'''
        page(f"course-{c['slug']}", c["title"], f"AiRise course {c['n']} of 9: {c['title']}. Model: {names}. {c['able']}", body)

    # ------------------------------------------------------------------ assessment
    parts = [("A", "Multiple choice", 27, "27 questions across the nine courses", "About 40 minutes, closed book"),
             ("B", "Integrated case", 30, "Applied analysis and communication across courses", "About 90 minutes, open book, no generative AI"),
             ("C", "Portfolio", 25, "Practice and reflection in your own context", "Submitted in advance"),
             ("D", "Practical", 18, "A role-play showing communication, judgement and openness to feedback", "About 15 minutes with an assessor")]
    body = hero("Assessment", 'Show what you<br><span class="gold">can really do.</span>',
                "AiRise assessments check three things: do you understand the models, can you apply them to realistic situations, and do you use them in your own work?")
    body += f'''
<section class="section">
  <div class="container">
    {head2("Course quizzes", "One quiz per course.", "Taken at the end of each course, or within a week of finishing it.")}
    <div class="ar-quiz reveal">
      <div><b>Section A</b><strong>10 marks</strong><p>Multiple choice on the course's models and ideas. 10 minutes, closed book, no devices.</p></div>
      <div><b>Section B</b><strong>10 marks</strong><p>Apply the course's model to a realistic scenario. 20 minutes.</p></div>
      <div class="ar-quiz__total"><b>Pass mark</b><strong>14 / 20</strong><p>18–20 is a pass with distinction. Below 14, you get feedback and can re-sit within four to six weeks.</p></div>
    </div>
    <div class="ar-rubric reveal">
      <h3>How scenario answers are marked</h3>
      <ul><li><b>Use of the model</b><span>0–3</span></li><li><b>Application to the scenario</b><span>0–3</span></li><li><b>Judgement and reasoning</b><span>0–2</span></li><li><b>Communication</b><span>0–2</span></li></ul>
      <p>Markers mark against the criteria, not a single model answer. Concise answers that hit the criteria score fully.</p>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="container">
    {head2("Final assessment", "Four parts.<br>100 marks.", "Taken after all nine courses. You need 70 overall and at least 50% in each part.")}
    <div class="ar-parts4">{"".join(f'<div class="reveal" style="--d:{i * .07:.2f}s"><span>Part {a}</span><h3>{e(b)}</h3><strong>{m} marks</strong><p>{e(d)}</p><small>{e(t)}</small></div>' for i, (a, b, m, d, t) in enumerate(parts))}</div>
  </div>
</section>

<section class="section" id="calculator">
  <div class="container">
    {head2("Result calculator", "Work out your result.", "Enter your marks for each part to see your overall result.")}
    <div class="ar-calc reveal" data-grade>
      <form onsubmit="return false">
        {"".join(f'<label>Part {a}: {e(b)} <span>out of {m}</span><input type="number" inputmode="numeric" min="0" max="{m}" name="p{a}" value="{round(m * .78)}" data-max="{m}"></label>' for a, b, m, _, _ in parts)}
      </form>
      <div class="ar-calc__out" aria-live="polite">
        <small>Your total</small><strong data-g="total">78</strong><span class="ar-calc__res" data-g="result">Merit</span>
        <p data-g="why">At least 50% in every part.</p>
        <ul class="ar-calc__bands"><li><b>85–100</b> Distinction</li><li><b>75–84</b> Merit</li><li><b>70–74</b> Pass</li><li><b>Below 70</b> Not yet passed</li></ul>
      </div>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="container">
    {head2("Fair and transparent", "The rules, up front.")}
    <div class="why">{"".join(f'<div class="why__item reveal" style="--d:{i * .07:.2f}s"><div class="why__ico">{ico(a)}</div><h3>{e(b)}</h3><p>{e(c)}</p></div>' for i, (a, b, c) in enumerate([
        ("shield", "Your own work", "Answers must be your own. You can use generative AI to study during the courses, but not to answer any assessment or write your portfolio."),
        ("users", "Accessible", "Ask for adjustments in advance: extra time (25% is common), a reader or scribe, large print, a quiet room or language support."),
        ("refresh", "Re-sits and appeals", "Re-sit a quiz or a failed part within four to six weeks, up to two times. Ask for a re-mark within ten working days."),
        ("lock", "Your data", "Results and portfolios are stored securely and used only as explained, in line with the Nigeria Data Protection Act 2023.")]))}</div>
    <p class="ar-note reveal">Results are returned within seven working days for quizzes and fourteen for the final assessment. Pass marks and timings are AiRise defaults and will be reviewed after the first cohort.</p>
  </div>
</section>'''
    page("assessment", "Assessment", "How AiRise assessments work: course quizzes, the four-part final assessment, result bands, re-sits, appeals and integrity rules.", body, extra_js=True)

    # ------------------------------------------------------------------ certificates
    certs = "".join(f'<li><b>Course {c["n"]}</b>{e(c["title"])} <em>{" and ".join(m[0] for m in c["models"])}</em></li>' for c in COURSES)
    body = hero("Certificates", 'Proof of skills,<br><span class="gold">not just attendance.</span>',
                "AiRise certificates show you completed the work and demonstrated competence through assessment. Every certificate has a unique number that employers can verify.")
    body += f'''
<section class="section">
  <div class="container show">
    <div class="show__copy reveal">
      <span class="eyebrow">Three kinds of certificate</span>
      <h2 class="title bar" style="margin-top:16px">Earn as you go.</h2>
      <div class="ar-certtypes">
        <div><h3>Course certificate</h3><p>Pass the course quiz (14 out of 20 or more), complete the course checklist and meet attendance (for example 80% of facilitated sessions).</p></div>
        <div><h3>Programme certificate</h3><p>Earn all nine course certificates and pass the final assessment (70 overall and at least 50% in each part).</p></div>
        <div class="gold-card"><h3>Programme certificate with Distinction</h3><p>As above, with 85 or more on the final assessment.</p></div>
      </div>
    </div>
    <div class="reveal" style="--d:.1s">
      <div class="ar-cert" aria-label="Example certificate">
        <div class="ar-cert__in">
          <img src="{img}/logo.png" alt="" width="700" height="686">
          <small>AiRise Employability Skills Training</small>
          <h3>Certificate of Completion</h3>
          <p>This is to certify that</p>
          <strong class="ar-cert__name">Learner name</strong>
          <p>has successfully completed the course<br><b>Communication Skills</b><br>Phase 1 · Course 3 of 9 · Model: CLEAR and HEAR · About 20 hours</p>
          <div class="ar-cert__foot"><span><i>{INSTRUCTOR}</i>Instructor</span><span><i>AIR-C3-2026-001</i>Certificate No.</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--tint" id="verify">
  <div class="container show">
    <div class="show__copy reveal">
      <span class="eyebrow">For employers</span>
      <h2 class="title bar" style="margin-top:16px">Check a certificate number.</h2>
      <p class="lead" style="margin-top:24px">Certificate numbers follow one scheme: <b>AIR-C3-2026-001</b> is course 3, issued in 2026, serial 001. <b>AIR-P-2026-001</b> is a programme certificate. Enter a number to read it, then contact AiRise to confirm it's genuine.</p>
    </div>
    <div class="ar-verify reveal" style="--d:.1s" data-verify>
      <label for="certno">Certificate number</label>
      <div class="ar-verify__row"><input id="certno" type="text" placeholder="AIR-C3-2026-001" autocomplete="off" spellcheck="false"><button class="btn" type="button">Check</button></div>
      <div class="ar-verify__out" aria-live="polite"></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    {head2("The full set", "Eleven certificates.", "One for each course, one for the full programme and one for the programme with distinction.")}
    <ol class="ar-certlist reveal">{certs}<li class="p"><b>Programme</b>All nine courses and the final assessment</li><li class="p d"><b>Distinction</b>The programme, with 85+ on the final assessment</li></ol>
    <p class="ar-note reveal">AiRise certificates are certificates of completion and competence. They are not an accredited qualification.</p>
  </div>
</section>'''
    page("certificates", "Certificates", "AiRise course and programme certificates: what they mean, how to earn them and how employers can check a certificate number.", body, extra_js=True)

    # ------------------------------------------------------------------ facilitators
    delivery = "".join(f'<div class="ar-deliv reveal" style="--d:{(i % 3) * .07:.2f}s"><span>{a}</span><h3>{e(b)}</h3><strong>{e(c)}</strong><p>{e(d)}</p><dl><dt>Load</dt><dd>{e(l)}</dd><dt>Suits</dt><dd>{e(s)}</dd></dl></div>' for i, (a, b, c, d, l, s) in enumerate(DELIVERY))
    session = "".join(f'<li><time>{a}</time><div><b>{e(b)}</b>{f"<p>{e(c)}</p>" if c else ""}</div></li>' for a, b, c in SESSION)
    tips = "".join(f'<div class="pillar"><h4>{e(a)}</h4><p>{e(b)}</p></div>' for a, b in FACILITATOR_TIPS)
    checks = "".join(f'<li><label><input type="checkbox" data-key="{i}"><span>{e(x)}</span></label></li>' for i, x in enumerate(CHECKLIST))
    body = hero("For facilitators and partners", 'Run the series<br><span class="gold">your way.</span>',
                "Universities, employers, training academies and community bodies can deliver the AiRise Employability Skills Series. Choose a format, follow the session plan and keep practice at the centre.",
                f'<a class="btn btn--gold" href="#contact">Partner with AiRise {ico("arrow")}</a><a class="btn btn--ghost" href="#checklist">Quick-start checklist</a>')
    body += f'''
<section class="section">
  <div class="container">
    {head2("Delivery options", "Six ways to deliver.", "These timings are suggestions based on each course's designed study time. Pilot with a first cohort and adjust.")}
    <div class="ar-delivs">{delivery}</div>
  </div>
</section>
<section class="section section--tint">
  <div class="container show">
    <div class="show__copy reveal">
      <span class="eyebrow">A suggested workshop</span>
      <h2 class="title bar" style="margin-top:16px">Three hours, built around practice.</h2>
      <p class="lead" style="margin-top:24px">Every session starts with accountability and ends with a commitment. Most of the time goes to practice in pairs and small groups.</p>
    </div>
    <ol class="ar-session reveal" style="--d:.1s">{session}</ol>
  </div>
</section>
<section class="section">
  <div class="container">
    {head2("Facilitator guidance", "What great sessions have in common.")}
    <div class="pillars ar-tips">{tips}</div>
  </div>
</section>
<section class="section section--tint" id="checklist">
  <div class="container show">
    <div class="show__copy reveal">
      <span class="eyebrow">Quick start</span>
      <h2 class="title bar" style="margin-top:16px">Before your first cohort.</h2>
      <p class="lead" style="margin-top:24px">Tick these off as you go. Your progress is saved in this browser.</p>
      <h3 class="ar-h3">Each learner needs</h3>
      {tick(["The course guide (Word or PDF) and a journal", "A simple tracker for goals and weekly reviews", "An accountability partner and, ideally, a mentor", "Time in their calendar and a quiet place to reflect"])}
    </div>
    <div class="ar-check reveal" style="--d:.1s" data-checklist><div class="ar-check__bar"><i></i></div><p class="ar-check__count" aria-live="polite"></p><ul>{checks}</ul></div>
  </div>
</section>
<section class="section">
  <div class="container">
    {head2("Quality and safety", "Handled with care.")}
    <div class="why">{"".join(f'<div class="why__item reveal" style="--d:{i * .07:.2f}s"><div class="why__ico">{ico(a)}</div><h3>{e(b)}</h3><p>{e(c)}</p></div>' for i, (a, b, c) in enumerate([
        ("heart", "Wellbeing", "Self-Awareness includes reflective exercises. Facilitators are not therapists: keep sharing voluntary and know your referral routes."),
        ("users", "Culture and context", "Examples draw on Nigerian and global workplaces. Adapt names, norms and examples to your learners and avoid stereotypes."),
        ("check", "Verify cases", "Check real-world cases against original sources before teaching. Illustrative cases are composites, not real people."),
        ("shield", "Law and policy", "References to law and workplace policy are general. Learners should check what applies where they work.")]))}</div>
  </div>
</section>'''
    page("facilitators", "For facilitators", "Deliver the AiRise Employability Skills Series: six delivery options, a three-hour session plan, facilitator guidance and a quick-start checklist.", body, extra_js=True)

    # ------------------------------------------------------------------ platform
    diagram = f'''<svg class="ar-diagram" viewBox="0 0 1000 460" role="img" aria-labelledby="dg-t dg-d">
  <title id="dg-t">How the AiRise platform connects talent and employers</title>
  <desc id="dg-d">Talent register, learn and get assessed. AiRise admins proctor exams, rank candidates and organise interviews. Employers search the ranked talent pool, request folders and hire.</desc>
  <defs><marker id="arw" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="currentColor"/></marker></defs>
  <g class="dg-col"><rect x="20" y="30" width="250" height="400" rx="22"/><text x="145" y="72" class="dg-h">Talent · Tier 1</text>
    {"".join(f'<g class="dg-item"><rect x="44" y="{100 + i * 52}" width="202" height="40" rx="10"/><text x="145" y="{125 + i * 52}">{t}</text></g>' for i, t in enumerate(["Register &amp; profile", "Upload documents", "Learn 9 courses", "Take assessments", "Interview &amp; get placed", "Request reactivation"]))}</g>
  <g class="dg-col dg-col--mid"><rect x="375" y="30" width="250" height="400" rx="22"/><text x="500" y="72" class="dg-h">AiRise · Tier 3</text>
    {"".join(f'<g class="dg-item"><rect x="399" y="{100 + i * 52}" width="202" height="40" rx="10"/><text x="500" y="{125 + i * 52}">{t}</text></g>' for i, t in enumerate(["Monitor growth", "Proctor examinations", "Ranking engine", "Organise interviews", "Automated emails", "Chat &amp; support"]))}</g>
  <g class="dg-col"><rect x="730" y="30" width="250" height="400" rx="22"/><text x="855" y="72" class="dg-h">Employers · Tier 2</text>
    {"".join(f'<g class="dg-item"><rect x="754" y="{100 + i * 52}" width="202" height="40" rx="10"/><text x="855" y="{125 + i * 52}">{t}</text></g>' for i, t in enumerate(["Search talent pool", "Filter by job &amp; rank", "Cross-reference skills", "Request folders", "One-time hire request", "Contracts"]))}</g>
  <g class="dg-arrows"><path d="M250 172 H395" marker-end="url(#arw)"/><path d="M395 320 H250" marker-end="url(#arw)"/><path d="M605 224 H750" marker-end="url(#arw)"/><path d="M750 276 H605" marker-end="url(#arw)"/></g>
  <g class="dg-lbl"><text x="322" y="160">results</text><text x="322" y="340">interviews</text><text x="678" y="212">ranked pool</text><text x="678" y="298">requests</text></g>
</svg>'''
    roles = [("Talent · Tier 1", "Students, graduates and experienced professionals building their employability.", TALENT_FUNCS),
             ("Employers · Tier 2", "Start-ups and multinationals hiring people who need little or no training.", EMPLOYER_FUNCS),
             ("AiRise admin · Tier 3", "AiRise's internal team, the mediator between talent and employers.", ADMIN_FUNCS)]
    roadmap = [("done", "Done", "Nine educational resources on employability skills; HRM proficiency training for the team."),
               ("now", "In progress", "The minimum viable product (MVP) for web and mobile."),
               ("next", "Next", "Lagos pilot launch, built for students and backed by employers."),
               ("later", "3–5 years", "A trusted global brand for hiring, staff development and capacity building.")]
    body = hero("Platform and system design", 'One platform.<br><span class="gold">Three sides.</span>',
                "AiRise is a one-stop HRM platform. Talent learn and prove their skills, employers find and hire them, and the AiRise team connects the two, all on web and mobile.")
    body += f'''
<section class="section">
  <div class="container">
    {head2("How it fits together", "The AiRise system.", "", center=True)}
    <div class="ar-diagram-wrap reveal">{diagram}</div>
  </div>
</section>
<section class="section section--tint">
  <div class="container">
    {head2("Users and roles", "Built for three tiers of users.")}
    <div class="ar-roles">{"".join(f'<article class="tier reveal" style="--d:{i * .08:.2f}s"><span class="tier__tag">{e(a)}</span><p style="margin:8px 0 18px;color:var(--ink-soft)">{e(b)}</p>{tick(fs)}</article>' for i, (a, b, fs) in enumerate(roles))}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    {head2("Platform modules", "Twelve building blocks.", "The parts of the AiRise web and mobile platform, and what each one does.")}
    <div class="ar-modules">{"".join(f'<div class="reveal" style="--d:{(i % 4) * .05:.2f}s"><span>{ico(a)}</span><h3>{e(b)}</h3><p>{e(c)}</p></div>' for i, (a, b, c) in enumerate(MODULES))}</div>
  </div>
</section>
<section class="section ar-dark">
  <div class="container">
    {head2("Roadmap", "Where we are.", "", center=True, light=True)}
    <ol class="ar-road">{"".join(f'<li class="ar-road--{k} reveal" style="--d:{i * .08:.2f}s"><span>{e(t)}</span><p>{e(d)}</p></li>' for i, (k, t, d) in enumerate(roadmap))}</ol>
  </div>
</section>'''
    page("platform", "Platform", "The AiRise system: three tiers of users (talent, employers, admin), twelve platform modules and the product roadmap.", body)

    # ------------------------------------------------------------------ about
    body = hero("About AiRise", 'Closing the gap between<br><span class="gold">talent and opportunity.</span>',
                "Established in 2022, AiRise offers all-inclusive human resource management solutions. Our goal is to become the leading platform for tackling talent underutilisation, unemployment and human resource problems in Africa and beyond.")
    body += f'''
<section class="section">
  <div class="container about">
    <div class="reveal"><img class="ar-about-logo" src="{img}/logo.png" alt="AiRise: Learn. Grow. Lead." width="700" height="686"></div>
    <div class="reveal" style="--d:.1s">
      <span class="eyebrow">Our approach</span>
      <h2 class="title bar" style="margin-top:16px">We develop talent before it's hired.</h2>
      <p class="lead" style="margin-top:24px">We focus on talent at the post-secondary level, giving people the training, internships and skills that make them highly employable. Employers get a consistent flow of qualified candidates suited to their needs, with lower turnover and better performance.</p>
      <p style="margin-top:18px;color:var(--ink-soft)">Our dual-market approach serves companies that want to hire efficiently and job seekers who need opportunities and skills, from students to seasoned professionals.</p>
    </div>
  </div>
</section>
<section class="section section--tint">
  <div class="container">
    {head2("The impact we're working for", "Three outcomes.", "", center=True)}
    <div class="why ar-3">{"".join(f'<div class="why__item reveal" style="--d:{i * .08:.2f}s"><div class="why__ico">{ico(a)}</div><h3>{e(b)}</h3><p>{e(c)}</p></div>' for i, (a, b, c) in enumerate([
        ("briefcase", "Job creation", "Facilitating meaningful employment opportunities."),
        ("chart", "Organisational efficiency", "Improving employee retention and organisational performance."),
        ("rise", "Talent empowerment", "Equipping people with in-demand skills and real-world experience.")]))}</div>
  </div>
</section>
<section class="section">
  <div class="container ar-instructor reveal">
    <span class="ar-avatar ar-avatar--lg">JO</span>
    <div><span class="eyebrow">Instructor</span><h2>{INSTRUCTOR}</h2><p>Instructor for the AiRise Employability Skills Training and author of the nine-course series and its models: SHIFT, SPARK, CLEAR and HEAR, SOLVE, KEEP, BUILD, LEARN, BRIDGE and SELF.</p></div>
  </div>
</section>
<section class="section section--tint">
  <div class="container">
    {head2("Part of Rehohub", "A Rehohub company.", "AiRise is one of Rehohub's digital products, alongside AiPay, AiMove and GreenFed.")}
    <div class="hero__ctas"><a class="btn" href="{BASE}index.html#products">See all Rehohub products {ico("arrow")}</a><a class="btn btn--outline" href="platform.html">Our roadmap</a></div>
  </div>
</section>'''
    page("about", "About", "AiRise, established in 2022, is an HR company tackling unemployment and talent underutilisation through training, assessment and talent matching.", body)
    return len(PAGES) - 1 + len(COURSES) + 1
