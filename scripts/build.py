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
    dict(slug="rheti", name="Rheti", tag="Training Institute", layout="wide",
         tagline="Knowledge. Practice. Impact.",
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

# ---------------------------------------------------------------------
# Product landing pages. A product with a `page` entry gets its own
# products/<slug>.html. Source for AiPay: "Ai+Pay project requirement"
# (first draft), product walkthrough videos and campaign posters.
# ---------------------------------------------------------------------
AIPAY_PAGE = dict(
    email="aipay@rehohub.com",
    headline=("Shop local.", "Sell more.", "Get paid."),
    lead="AiPay is an e-store with an in-built payment system. Buyers find products near them, merchants get a ready-made store with customers already in it, and businesses get a payment gateway they can plug into any website.",
    hero_video="store",
    audiences=[
        ("cart", "Buyers", "Shop from stores around you",
         ["Search products within your location", "Add to cart and pay by card or bank transfer", "Track every order to your door", "Earn and spend loyalty points"]),
        ("store", "Merchants", "Your store, without building one",
         ["Create a verified, accredited store page", "Upload products, run discounts and promos", "Manage orders and stock in one dashboard", "Choose delivery: RehoGo, UPS or DHL"]),
        ("code", "Businesses", "A payment gateway for your website",
         ["Integrate AiPay into any system", "Accept and verify payments", "Track payouts and payment history", "Download receipts for every transaction"]),
    ],
    showcases=[
        dict(id="store", eyebrow="For buyers", title="An e-store that knows where you are.",
             body="Use your current location to find stores near you. Browse food and drinks, fashion, electronics and make-up, then check out in a few taps.",
             points=["Location-based search", "Cart and order summary", "Card or bank-transfer payment", "Instant payment confirmation"],
             video="checkout", label="AiPay store: add to cart, choose a payment method and pay"),
        dict(id="sell", eyebrow="For merchants", title="Open your store in minutes.",
             body="Sign up, tell us about your business, pin your location on the map and get your space verified. Once you're accredited, your products go live to buyers already shopping on AiPay.",
             points=["Business profile and verification", "Location pinned on the map", "Financial details for payouts", "Get accredited and go live"],
             video="onboarding", label="Merchant sign-up and profile set-up on AiPay"),
        dict(id="dashboard", eyebrow="Merchant dashboard", title="Every order, sale and naira in one view.",
             body="See your balance, visitors and sales at a glance. Move orders from processing to ready-to-ship to shipped, and get notified as soon as a new order comes in.",
             points=["Balance and sales reports", "Order pipeline", "Recent transactions", "Notification settings"],
             video="merchant-dashboard", label="AiPay merchant dashboard walkthrough"),
        dict(id="gateway", eyebrow="Payment gateway", title="Plug AiPay into your business.",
             body="Already have a website or app? Request the AiPay payment system and accept payments anywhere. Track transactions, verify payment status and download receipts from your gateway dashboard.",
             points=["Transaction overview", "Success, pending and failed status", "Full payment history", "Downloadable receipts"],
             video="gateway", label="AiPay payment gateway dashboard walkthrough"),
    ],
    tracking=["Order picked", "Processed", "Packed", "On route", "Delivered"],
    delivery=[("RehoGo", "Rehohub's own delivery network, with reviews for every drop-off."),
              ("UPS & DHL", "Merchants can choose trusted global couriers."),
              ("Pick-up", "Collect from the store and chat with the merchant."),
              ("Merchant delivery", "The store delivers to you directly.")],
    campaign=dict(
        eyebrow="AiPay for students",
        title="From side hustle to thriving business.",
        body="Are you a studentpreneur? Join AiPay to reach thousands of students, or shop the student market and buy at your own price.",
        perks=["Access to 4,000+ students", "2 FREE marketing slots weekly", "Smart logistics and growth tips", "Business growth training to scale faster"],
        stats=[("500%", "More visibility"), ("5X", "Revenue growth"), ("15,000+", "Students"), ("5★", "Delivery experience")],
        posters=[("poster-studentpreneur.jpg", "AiPay poster: From side hustle to thriving business. 500% more visibility, 5X revenue growth."),
                 ("poster-own-price.jpg", "AiPay poster: Buy at your own price. Spend less, buy more, with a 5-star delivery experience.")],
    ),
)

GREENFED_PAGE = dict(
    kind="greenfed",
    email="greenfed@rehohub.com",
    phone="+234 810 541 2715",
    tagline="Fresh food. Smarter you.",
    lead="GreenFed bridges the gap between people and good nutrition. Nutritionists build meal plans around your calorie and health needs, farm-fresh groceries arrive at your door every week, and a supportive community helps you stay on track.",
    pillars=[("leaf", "Nutritious choices", "Fuel your body with the best."),
             ("tag", "Affordable prices", "Healthy food for every budget."),
             ("truck", "Convenient delivery", "Freshness, right to your doorstep."),
             ("sprout", "Quality assured", "Carefully sourced. Always fresh.")],
    steps=[("Register", "Sign up with email or Google / Facebook and verify your account in one click."),
           ("Tell us about you", "Add your household, ages, health status and allergies."),
           ("Get your meal plan", "A nutritionist builds a dynamic plan around your calorie and health needs."),
           ("Receive it in 48 hours", "Your plan arrives by e-copy in your email and in the app."),
           ("Order fresh groceries", "Shop straight from your meal plan, or by preference."),
           ("Weekly delivery", "Farm-fresh produce delivered to your door every week.")],
    meal=dict(
        title="Meal plans made for your body.",
        body="Request a plan for yourself or for everyone at home, including family members with special needs. Each plan is built on calorie needs and is dynamic, so it changes as you do.",
        points=["Calorie and health-need based", "Multiple plans per household", "Pay by card or bank transfer", "See which nutritionist picked up your plan", "Delivered in under 48 hours", "Review every plan"]),
    grocery=dict(
        title="Farm-fresh groceries, every week.",
        body="Turn your meal plan into a grocery order with one tap, or build your own basket. We gather, check, pack and deliver, and you can follow each stage in the app and by email.",
        stages=["Order gathering", "Quality assurance", "Packaged", "En route · 30 min", "Delivered"]),
    community=dict(
        title="A community that eats well, together.",
        body="Join groups for allergies, health conditions, nutrition, and food & craft. Health professionals can sign up as handlers or community leaders. The community is open to everyone, even if you don't use meal planning or grocery delivery.",
        groups=["Allergies", "Health issues", "Nutrition", "Food & Craft", "Weight goals", "Rehabilitation support"]),
    boxes=[("basic", "Basic Box", "Staples & vegetables", "Affordable everyday essentials."),
           ("healthy", "Healthy Box", "Balanced meals", "Portioned ingredients for healthy meals."),
           ("fitness", "Fitness Box", "High protein", "For fitness and active lifestyles."),
           ("specialty", "Specialty Box", "Vegan · Diabetic · Gluten-free", "For unique dietary needs and preferences.")],
    team=[("Nutritionists", "Build and update every meal plan."),
          ("Supply managers", "Source and manage grocery orders."),
          ("Quality assurance", "Check every item before it ships."),
          ("Packaging & delivery", "Pack fresh and deliver on time."),
          ("Health specialists", "Guide and support the community."),
          ("Suppliers", "Partner farms that supply fresh produce.")],
    promise=[("Late delivery?", "Your next delivery is on us."),
             ("Poor quality?", "We recall it and resupply, fast.")],
)

# AiMove content comes from the AiMove Android app (github.com/Rehoboth227/Aimove,
# app name "REHOMOVE"): its screens, PricingEngine and API logs.
AIMOVE_PAGE = dict(
    kind="aimove",
    email=None,  # no AiMove address provided yet; falls back to info@rehohub.com
    lead="AiMove connects businesses and individuals with verified riders for fast, safe package delivery. You get a guaranteed price upfront, live GPS tracking and a wallet for paying, all in one app.",
    types=[("Instant express", "Picked up right away for urgent deliveries.", "+₦300"),
           ("Same-day", "Delivered today, at the standard rate.", "Standard"),
           ("Scheduled", "Choose a pickup date and time slot in advance.", "Plan ahead")],
    business=["Send a package in a few taps", "Book a rider in your area", "Schedule future pickups", "Track your item live on the map",
              "Chat with your rider", "Rate every delivery"],
    stages=[("Requested", "Your order is sent to riders nearby."), ("Picked up", "A verified rider collects your package."),
            ("In transit", "Follow it live with GPS and an ETA."), ("Delivered", "Confirmed with the recipient's 4-digit PIN.")],
    rider=["Accept nearby orders, filtered by payout or express", "Built-in GPS navigation", "Chat with the customer",
           "Proof of delivery with the customer PIN", "Track earnings, trips and rating", "Withdraw to your bank account"],
    wallet=[("Fund your wallet", "Top up with saved debit or credit cards."), ("Every naira tracked", "Search all credits and debits in your history."),
            ("PDF statements", "Export statements for your records."), ("Refer & earn", "Get a ₦500 bonus for each friend you invite.")],
    trust=[("Verified riders", "Driver's licence, vehicle and plate number on every profile."), ("Biometric login", "Fingerprint or Face ID sign-in."),
           ("Ratings & reviews", "Rate riders after every delivery."), ("Dispute protection", "PIN-confirmed delivery protects both sides.")],
)

# Product categories. Replace the URLs below with the live web-app
# addresses and store listings as each product launches.
PRODUCTS = [
    dict(slug="aipay", name="AiPay", cat="E-commerce · Payments", c1="#2185FF", c2="#1760BA", icon="cart",
         desc="An e-store with a built-in payment system. Shop from merchants near you, open your own online store, or plug the AiPay payment gateway into your business.",
         feats=["Local e-store", "Merchant stores", "Payment gateway", "Loyalty points"],
         web="https://aipay.rehohub.com",
         ios="https://apps.apple.com/app/aipay",
         android="https://play.google.com/store/apps/details?id=com.rehohub.aipay",
         screen=("Store", "₦6,000", "Payment confirmed"),
         page=AIPAY_PAGE),
    dict(slug="aimove", name="AiMove", cat="Logistics · Delivery", c1="#3d7bff", c2="#0c2a5e", icon="move",
         desc="Fast, safe package delivery. Get a guaranteed price upfront, book a verified rider, track your package live and pay from your wallet. Built for businesses, riders and developers.",
         feats=["Instant & same-day", "Scheduled pickups", "Live GPS tracking", "Delivery API"],
         web="https://aimove.rehohub.com",
         ios="https://apps.apple.com/app/aimove",
         android="https://play.google.com/store/apps/details?id=com.rehohub.aimove",
         screen=("Tracking", "12 min", "Rider on the way"),
         page=AIMOVE_PAGE),
    dict(slug="airise", name="AiRise", cat="HR · Employability", c1="#D4A12A", c2="#0D2357", icon="rise",
         desc="An HR company built around the employability journey. Train with the nine-course Employability Skills Series, get assessed and ranked, and get matched with employers. Organisations get HR services on demand.",
         feats=["Employability training", "Talent matching", "Certificates", "HR services"],
         web="https://www.airise.com.ng/signup",
         ios="https://apps.apple.com/app/airise",
         android="https://play.google.com/store/apps/details?id=com.rehohub.airise",
         screen=("My learning", "6 / 9", "Courses complete"),
         href="products/airise/index.html"),
    dict(slug="greenfed", name="GreenFed", cat="Food · Nutrition", c1="#7cc242", c2="#0a4a26", icon="leaf",
         desc="Fresh food, smarter you. Personal meal plans from nutritionists, farm-fresh groceries delivered weekly, and a community for healthier living.",
         feats=["Meal planning", "Weekly groceries", "Food boxes", "Health community"],
         web="https://greenfed.rehohub.com",
         ios="https://apps.apple.com/app/greenfed",
         android="https://play.google.com/store/apps/details?id=com.rehohub.greenfed",
         screen=("Meal plan", "1,850 kcal", "Today's target"),
         page=GREENFED_PAGE),
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


def aipay_logo(cls="ap-logo__icon"):
    """AiPay product mark: shopping cart with a sparkle badge (from the AiPay posters)."""
    return (f'<svg class="{cls}" viewBox="0 0 64 64" aria-hidden="true"><rect width="64" height="64" rx="14" fill="#1760BA"/>'
            '<path d="M12 18h6l5 22h20l5-15H21" fill="none" stroke="#fff" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>'
            '<circle cx="26" cy="48" r="3.6" fill="#fff"/><circle cx="40" cy="48" r="3.6" fill="#fff"/>'
            '<circle cx="47" cy="19" r="9" fill="#FFE600" stroke="#1760BA" stroke-width="2.5"/>'
            '<path d="M47 13.5l1.4 4.1 4.1 1.4-4.1 1.4L47 24.5l-1.4-4.1-4.1-1.4 4.1-1.4z" fill="#1760BA"/></svg>')


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
        "cart": '<circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h3l2.7 12.4a2 2 0 0 0 2 1.6h7.7a2 2 0 0 0 2-1.5L21 8H6.2"/>',
        "store": '<path d="M3 9l1.5-5h15L21 9"/><path d="M3 9a3 3 0 0 0 6 0 3 3 0 0 0 6 0 3 3 0 0 0 6 0"/><path d="M5 12v8h14v-8M10 20v-5h4v5"/>',
        "code": '<path d="m8 8-5 4 5 4M16 8l5 4-5 4M14 4l-4 16"/>',
        "truck": '<path d="M1 4h14v12H1zM15 9h4l4 4v3h-8"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/>',
        "pin": '<path d="M12 22s7-6.1 7-12a7 7 0 1 0-14 0c0 5.9 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/>',
        "tag": '<path d="M20.6 13.4 13.4 20.6a2 2 0 0 1-2.8 0L3 13V3h10l7.6 7.6a2 2 0 0 1 0 2.8z"/><circle cx="7.5" cy="7.5" r="1.5"/>',
        "sprout": '<path d="M12 22V11"/><path d="M12 11C12 7 9 4 4 4c0 4 3 7 8 7zM12 13c0-4 3-7 8-7 0 4-3 7-8 7z"/>',
        "heart": '<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 21l8.8-8.6a5.5 5.5 0 0 0 0-7.8z"/>',
        "plan": '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h5"/>',
        "bike": '<circle cx="5.5" cy="17.5" r="3.5"/><circle cx="18.5" cy="17.5" r="3.5"/><path d="M15 6h3l2 6M5.5 17.5 9 10h6l3.5 7.5M9 10 7 6H4"/>',
        "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
        "calendar": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
        "wallet": '<path d="M20 7V5a2 2 0 0 0-2-2H5a2 2 0 0 0 0 4h15v13H5a2 2 0 0 1-2-2V5"/><circle cx="16" cy="13.5" r="1.5"/>',
        "lock": '<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
        "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
        "id": '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="11" r="2.5"/><path d="M5.5 17a3.5 3.5 0 0 1 7 0M15 9h3M15 13h3"/>',
        "book": '<path d="M2 4h7a3 3 0 0 1 3 3v14a2 2 0 0 0-2-2H2zM22 4h-7a3 3 0 0 0-3 3v14a2 2 0 0 1 2-2h8z"/>',
        "chat": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
        "briefcase": '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2M2 13h20"/>',
        "refresh": '<path d="M21 12a9 9 0 1 1-3-6.7L21 8"/><path d="M21 3v5h-5"/>',
        "search": '<circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/>',
        "chart": '<path d="M3 3v18h18"/><path d="M7 16v-5M12 16V8M17 16v-8"/>',
        "star": '<path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>',
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
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Kaushan+Script&display=swap" rel="stylesheet">
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
    prod_links = "".join(
        f'<li><a href="{base}{p.get("href") or "products/" + p["slug"] + ".html"}">{p["name"]}</a></li>' if p.get("page") or p.get("href")
        else f'<li><a href="{p["web"]}" target="_blank" rel="noopener">{p["name"]}</a></li>' for p in PRODUCTS)
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


def cta_block(email=None, title="Your one-stop hub<br>starts here.", body=None, phone=None):
    email = email or CONTACT["email"]
    phone = phone or CONTACT["phone"]
    phone_href = "tel:" + "".join(ch for ch in phone if ch.isdigit() or ch == "+")
    body = body or "Partner with any Rehohub subsidiary, invest in our ecosystem or bring your next big project to life. Our team responds within one business day."
    return f'''<section class="section" id="contact">
  <div class="container">
    <div class="cta reveal">
      {r_mark("hero__ghost hero__ghost--a")}
      <div>
        <span class="eyebrow eyebrow--light">Let's build together</span>
        <h2 style="margin-top:18px">{title}</h2>
        <p>{body}</p>
      </div>
      <div class="cta__contact">
        <a href="mailto:{email}">{ico("mail")} {email}</a>
        <a href="{phone_href}">{ico("phone")} {phone}</a>
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
          <h3 class="prod__name"><span class="prod__icon">{ico(p["icon"])}</span>{f'<a href="{p.get("href") or "products/" + p["slug"] + ".html"}">{p["name"]}</a>' if p.get("page") or p.get("href") else p["name"]}</h3>
          <p class="prod__desc">{escape(p["desc"])}</p>
          <ul class="prod__feats">{feats}</ul>
          {f'<a class="prod__more" href="{p.get("href") or "products/" + p["slug"] + ".html"}">Explore {p["name"]} {ico("arrow")}</a>' if p.get("page") or p.get("href") else ""}
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
    if s["slug"] == "rheti":
        import rheti
        return rheti.build(globals(), idx, s)
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


# =====================================================================
# PRODUCT PAGES
# =====================================================================


def video(base, slug, name, label, cls=""):
    src = f"{base}assets/media/{slug}/{name}"
    return (f'<div class="browser {cls}"><div class="browser__bar" aria-hidden="true"><i></i><i></i><i></i><span>{slug}.rehohub.com</span></div>'
            f'<video class="browser__video" src="{src}.mp4" poster="{src}.jpg" autoplay muted loop playsinline preload="metadata" aria-label="{escape(label)}"></video></div>')


def store_buttons(p):
    return f'''<a class="store store--web" href="{p["web"]}" target="_blank" rel="noopener" aria-label="Open {p["name"]} web app">{ico("web")}<span><small>Open the</small><b>Web App</b></span></a>
          <a class="store" href="{p["ios"]}" target="_blank" rel="noopener" aria-label="Download {p["name"]} on the App Store">{APPLE}<span><small>Download on the</small><b>App Store</b></span></a>
          <a class="store" href="{p["android"]}" target="_blank" rel="noopener" aria-label="Get {p["name"]} on Google Play">{PLAY}<span><small>Get it on</small><b>Google Play</b></span></a>'''


def build_product(p):
    if p["page"].get("kind") == "greenfed":
        return build_greenfed(p)
    if p["page"].get("kind") == "aimove":
        return build_aimove(p)
    base = "../"
    d = p["page"]
    slug = p["slug"]
    h1, h2, h3 = d["headline"]
    audiences = "".join(
        f'''<article class="tier reveal" style="--d:{i * .08:.2f}s">
          <div class="tier__head"><span class="why__ico">{ico(ic)}</span><div><span class="tier__tag">{escape(who)}</span><h3>{escape(t)}</h3></div></div>
          <ul class="ticks">{"".join(f"<li>{ico('check')}{escape(x)}</li>" for x in pts)}</ul>
        </article>''' for i, (ic, who, t, pts) in enumerate(d["audiences"]))
    showcases = "".join(
        f'''<div class="show{' show--flip' if i % 2 else ''}" id="{sc["id"]}">
        <div class="show__copy reveal">
          <span class="eyebrow">{escape(sc["eyebrow"])}</span>
          <h2 class="title bar" style="margin-top:16px">{escape(sc["title"])}</h2>
          <p class="lead" style="margin-top:24px">{escape(sc["body"])}</p>
          <ul class="ticks ticks--grid">{"".join(f"<li>{ico('check')}{escape(x)}</li>" for x in sc["points"])}</ul>
        </div>
        <div class="show__media reveal" style="--d:.1s">{video(base, slug, sc["video"], sc["label"])}</div>
      </div>''' for i, sc in enumerate(d["showcases"]))
    track = "".join(f'<li class="reveal" style="--d:{i * .1:.1f}s"><span>{i + 1}</span>{escape(t)}</li>' for i, t in enumerate(d["tracking"]))
    deliv = "".join(f'<div class="deliv reveal" style="--d:{i * .08:.2f}s"><h4>{escape(a)}</h4><p>{escape(b)}</p></div>' for i, (a, b) in enumerate(d["delivery"]))
    c = d["campaign"]
    stats = "".join(f'<div class="ystat"><strong>{escape(a)}</strong><span>{escape(b)}</span></div>' for a, b in c["stats"])
    perks = "".join(f"<li>{ico('check')}{escape(x)}</li>" for x in c["perks"])
    posters = "".join(
        f'<figure class="poster reveal" style="--d:{i * .12:.2f}s"><img src="{base}assets/img/{slug}/{f}" alt="{escape(alt)}" loading="lazy" width="1080" height="1350"></figure>'
        for i, (f, alt) in enumerate(c["posters"]))

    html = head(f"{p['name']} — {h1} {h2} {h3} | Rehohub", d["lead"], base)
    html += header(base)
    html += f'''<main id="main" class="product-page">
<section class="p-hero">
  {r_mark("hero__ghost hero__ghost--a")}
  <div class="hero__glow"></div><div class="hero__grid"></div>
  <div class="container p-hero__inner">
    <div class="p-hero__copy">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="{base}index.html">Rehohub</a><span>/</span><a href="{base}index.html#products">Products</a><span>/</span><span aria-current="page">{p["name"]}</span></nav>
      <div class="ap-logo reveal">{aipay_logo()}<span>{p["name"]}</span><em>{escape(p["cat"])}</em></div>
      <h1 class="reveal" style="--d:.08s">{h1}<br>{h2}<br><span class="hl">{h3}</span></h1>
      <p class="hero__lead reveal" style="--d:.16s">{escape(d["lead"])}</p>
      <div class="hero__ctas reveal" style="--d:.24s">
        <a class="btn btn--yellow" href="{p["web"]}" target="_blank" rel="noopener">Start shopping {ico("arrow")}</a>
        <a class="btn btn--ghost" href="#sell">Open a store</a>
        <a class="btn btn--ghost" href="#gateway">Payment gateway</a>
      </div>
    </div>
    <div class="p-hero__media reveal" style="--d:.2s">
      {video(base, slug, d["hero_video"], "AiPay store walkthrough")}
      <div class="float-chip float-chip--a">{ico("pin")} Stores near you</div>
      <div class="float-chip float-chip--b"><b>₦6,000</b> Payment confirmed ✓</div>
    </div>
  </div>
</section>

<section class="section section--tint" id="who">
  <div class="container">
    <div class="section__head section__head--split">
      <div class="reveal"><span class="eyebrow">Built for everyone</span><h2 class="title bar" style="margin-top:16px">One platform,<br>three ways to use it.</h2></div>
      <p class="lead reveal" style="--d:.1s">Whether you're buying, selling or taking payments on your own site, AiPay links you to the same network of customers, merchants and delivery partners.</p>
    </div>
    <div class="tiers">{audiences}</div>
  </div>
</section>

<section class="section shows">
  <div class="container">{showcases}</div>
</section>

<section class="section products-wrap" id="delivery">
  {r_mark("hero__ghost hero__ghost--a")}
  <div class="container">
    <div class="section__head" style="text-align:center;justify-items:center">
      <span class="eyebrow eyebrow--light reveal">Delivery and tracking</span>
      <h2 class="title title--light bar bar--light bar--center reveal" style="--d:.08s">Follow your order<br>all the way home.</h2>
    </div>
    <ol class="track">{track}</ol>
    <div class="delivs">{deliv}</div>
  </div>
</section>

<section class="section" id="loyalty">
  <div class="container loyal">
    <div class="loyal__card reveal" aria-hidden="true">
      <div class="loyal__top">{aipay_logo("loyal__logo")}<span>AiPay Rewards</span></div>
      <div class="loyal__pts"><small>Loyalty points</small><strong>2,450</strong></div>
      <div class="loyal__bot"><span>Ade Johnson</span><span>Member since 2025</span></div>
    </div>
    <div class="reveal" style="--d:.1s">
      <span class="eyebrow">Loyalty</span>
      <h2 class="title bar" style="margin-top:16px">Every purchase pays you back.</h2>
      <p class="lead" style="margin-top:24px">Create an account and get a personal profile with your own loyalty card. Earn points every time you buy, then spend them on your next order.</p>
      <ul class="ticks" style="margin-top:24px"><li>{ico("check")}Points on every purchase</li><li>{ico("check")}Redeem points at checkout</li><li>{ico("check")}Review stores and deliveries</li><li>{ico("check")}Updates at every order stage</li></ul>
    </div>
  </div>
</section>

<section class="section campaign" id="students">
  <div class="container campaign__inner">
    <div class="campaign__copy reveal">
      <span class="eyebrow eyebrow--light">{escape(c["eyebrow"])}</span>
      <h2 class="title title--light" style="margin-top:16px">{escape(c["title"])}</h2>
      <p class="lead" style="margin-top:20px;color:rgba(255,255,255,.85)">{escape(c["body"])}</p>
      <div class="ystats">{stats}</div>
      <ul class="ticks ticks--light">{perks}</ul>
      <div class="hero__ctas"><a class="btn btn--yellow" href="{p["web"]}" target="_blank" rel="noopener">Join AiPay {ico("arrow")}</a></div>
    </div>
    <div class="posters">{posters}</div>
  </div>
</section>

<section class="section" id="download" style="padding-bottom:0">
  <div class="container">
    <div class="dl reveal">
      <div>{aipay_logo("dl__logo")}</div>
      <div><h2>Get {p["name"]} on any device.</h2><p>Open it in your browser or download the mobile app for iOS and Android.</p></div>
      <div class="prod__actions" style="--c1:{p["c1"]};--c2:{p["c2"]}">{store_buttons(p)}</div>
    </div>
  </div>
</section>

{cta_block(d["email"], "Talk to the<br>AiPay team.", "Questions about selling on AiPay, the payment gateway or a student partnership? Write to us and we'll get back to you.")}
</main>
'''
    html += footer(base)
    (ROOT / "products").mkdir(exist_ok=True)
    (ROOT / "products" / f"{slug}.html").write_text(html, encoding="utf-8")


def build_greenfed(p):
    base = "../"
    d = p["page"]
    slug = p["slug"]
    img = f"{base}assets/img/{slug}"
    pillars = "".join(f'<div class="gf-pillar reveal" style="--d:{i * .08:.2f}s"><span>{ico(a)}</span><h3>{escape(b)}</h3><p>{escape(c)}</p></div>' for i, (a, b, c) in enumerate(d["pillars"]))
    steps = "".join(f'<li class="reveal" style="--d:{i * .06:.2f}s"><b>{i + 1:02d}</b><h3>{escape(a)}</h3><p>{escape(b)}</p></li>' for i, (a, b) in enumerate(d["steps"]))
    m, g, c = d["meal"], d["grocery"], d["community"]
    mpoints = "".join(f"<li>{ico('check')}{escape(x)}</li>" for x in m["points"])
    stages = "".join(f'<li><span>{ico("check")}</span>{escape(x)}</li>' for x in g["stages"])
    groups = "".join(f"<span>{escape(x)}</span>" for x in c["groups"])
    boxes = "".join(f'''<article class="gf-box gf-box--{k} reveal" style="--d:{i * .08:.2f}s">
        <img src="{img}/box-{k}.jpg" alt="GreenFed {escape(n)}" loading="lazy" width="205" height="120">
        <h3>{escape(n)}</h3><b>{escape(t)}</b><p>{escape(x)}</p></article>''' for i, (k, n, t, x) in enumerate(d["boxes"]))
    team = "".join(f'<div class="gf-role"><h4>{escape(a)}</h4><p>{escape(b)}</p></div>' for a, b in d["team"])
    promise = "".join(f'<div class="gf-promise reveal" style="--d:{i * .1:.1f}s"><h3>{escape(a)}</h3><p>{escape(b)}</p></div>' for i, (a, b) in enumerate(d["promise"]))
    days = "".join(f'<li><span>{dname}</span><i style="width:{w}%"></i><em>{k} kcal</em></li>' for dname, w, k in
                   [("Mon", 82, "1,820"), ("Tue", 90, "1,900"), ("Wed", 76, "1,760"), ("Thu", 88, "1,880"), ("Fri", 80, "1,810")])

    html = head(f"{p['name']} — {d['tagline']} | Rehohub", d["lead"], base)
    html += header(base)
    html += f'''<main id="main" class="product-page theme-gf">
<section class="gf-hero">
  <div class="gf-hero__leaf gf-hero__leaf--a" aria-hidden="true">{ico("leaf")}</div>
  <div class="gf-hero__leaf gf-hero__leaf--b" aria-hidden="true">{ico("leaf")}</div>
  <div class="container gf-hero__inner">
    <div>
      <nav class="crumbs" aria-label="Breadcrumb"><a href="{base}index.html">Rehohub</a><span>/</span><a href="{base}index.html#products">Products</a><span>/</span><span aria-current="page">{p["name"]}</span></nav>
      <img class="gf-hero__logo reveal" src="{img}/logo-white.png" alt="GreenFed — Fresh food. Smarter you." width="900" height="517">
      <h1 class="reveal" style="--d:.08s">Fresh food.<br>Real nutrition.<br><span class="script">Delivered.</span></h1>
      <p class="hero__lead reveal" style="--d:.16s">{escape(d["lead"])}</p>
      <div class="hero__ctas reveal" style="--d:.24s">
        <a class="btn btn--lime" href="{p["web"]}" target="_blank" rel="noopener">Get my meal plan {ico("arrow")}</a>
        <a class="btn btn--ghost" href="#groceries">Order groceries</a>
        <a class="btn btn--ghost" href="#community">Join the community</a>
      </div>
    </div>
    <div class="gf-hero__media reveal" style="--d:.2s">
      <div class="gf-hero__photo"><img src="{img}/hero-box.jpg" alt="A GreenFed box full of fresh vegetables, fruit, eggs and fish" width="694" height="620"></div>
      <img class="gf-hero__badge" src="{img}/badge.png" alt="" width="480" height="480">
      <div class="float-chip float-chip--a">{ico("plan")} Meal plan in under 48 hrs</div>
      <div class="float-chip float-chip--c">{ico("truck")} Fresh, weekly delivery</div>
    </div>
  </div>
</section>

<section class="gf-pillars-wrap">
  <div class="container gf-pillars">{pillars}</div>
</section>

<section class="section" id="how">
  <div class="container">
    <div class="section__head section__head--split">
      <div class="reveal"><span class="eyebrow">How it works</span><h2 class="title bar" style="margin-top:16px">From sign-up to<br>your doorstep.</h2></div>
      <p class="lead reveal" style="--d:.1s">Six simple steps take you from a quick profile to a personal meal plan and fresh groceries every week.</p>
    </div>
    <ol class="gf-steps">{steps}</ol>
  </div>
</section>

<section class="section section--tint" id="meal-plans">
  <div class="container show">
    <div class="show__copy reveal">
      <span class="eyebrow">Meal planning</span>
      <h2 class="title bar" style="margin-top:16px">{escape(m["title"])}</h2>
      <p class="lead" style="margin-top:24px">{escape(m["body"])}</p>
      <ul class="ticks ticks--grid">{mpoints}</ul>
    </div>
    <div class="show__media reveal" style="--d:.1s" aria-hidden="true">
      <div class="gf-plan">
        <div class="gf-plan__head"><div><small>Weekly meal plan</small><strong>The Johnson family</strong></div><span>3 plans</span></div>
        <div class="gf-plan__who"><span class="on">Ade · 34</span><span>Bisi · 31</span><span>Tobi · 9 · nut allergy</span></div>
        <ul class="gf-plan__days">{days}</ul>
        <div class="gf-plan__foot"><div><small>Prepared by</small><b>Nutritionist A. Bello</b></div><span class="gf-ok">{ico("check")} Delivered in 36 hrs</span></div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="groceries">
  <div class="container show show--flip">
    <div class="show__copy reveal">
      <span class="eyebrow">Grocery delivery</span>
      <h2 class="title bar" style="margin-top:16px">{escape(g["title"])}</h2>
      <p class="lead" style="margin-top:24px">{escape(g["body"])}</p>
      <ul class="ticks" style="margin-top:28px"><li>{ico("check")}Order from your meal plan or by preference</li><li>{ico("check")}Updates by email and in the app</li><li>{ico("check")}Review every stage of the order</li></ul>
    </div>
    <div class="show__media reveal" style="--d:.1s">
      <div class="gf-track" aria-label="Grocery order stages"><div class="gf-track__head"><small>Order #GF-20481</small><strong>Your groceries are on the way</strong></div><ol>{stages}</ol></div>
    </div>
  </div>
</section>

<section class="section gf-boxes-wrap" id="boxes">
  <div class="container">
    <div class="section__head" style="text-align:center;justify-items:center">
      <span class="eyebrow eyebrow--light reveal">Our food boxes</span>
      <h2 class="title title--light bar bar--light bar--center reveal" style="--d:.08s">A box for every<br>kind of healthy.</h2>
    </div>
    <div class="gf-boxes">{boxes}</div>
  </div>
</section>

<section class="section" id="community">
  <div class="container show">
    <div class="show__copy reveal">
      <span class="eyebrow">Community</span>
      <h2 class="title bar" style="margin-top:16px">{escape(c["title"])}</h2>
      <p class="lead" style="margin-top:24px">{escape(c["body"])}</p>
      <div class="hero__ctas"><a class="btn btn--green" href="{p["web"]}" target="_blank" rel="noopener">Join the community {ico("arrow")}</a></div>
    </div>
    <div class="show__media reveal" style="--d:.1s">
      <div class="gf-community"><img src="{img}/badge.png" alt="" width="480" height="480"><div class="gf-groups">{groups}</div></div>
    </div>
  </div>
</section>

<section class="section section--tint" id="team">
  <div class="container">
    <div class="section__head section__head--split">
      <div class="reveal"><span class="eyebrow">The people behind your food</span><h2 class="title bar" style="margin-top:16px">Every order has<br>a team behind it.</h2></div>
      <p class="lead reveal" style="--d:.1s">Each order moves through specialists, and you can see who picked it up at every stage. Joined the team? Sign up on the employee side with the code in your employment letter.</p>
    </div>
    <div class="gf-roles reveal">{team}</div>
    <div class="gf-promises">{promise}</div>
  </div>
</section>

<section class="section" id="brand">
  <div class="container">
    <div class="section__head" style="text-align:center;justify-items:center">
      <span class="eyebrow reveal">Packed with care</span>
      <h2 class="title bar bar--center reveal" style="--d:.08s">Fresh from the farm,<br>beautifully packed.</h2>
    </div>
    <figure class="gf-board reveal"><img src="{img}/brand-board.jpg" alt="GreenFed packaging: insulated bags, produce boxes, cups, pouches, jars, juice bottles, meal-prep containers and stickers" loading="lazy" width="1080" height="720"></figure>
  </div>
</section>

<section class="section" id="download" style="padding-top:0;padding-bottom:0">
  <div class="container">
    <div class="dl dl--gf reveal">
      <div><img class="dl__img" src="{img}/badge.png" alt="" width="480" height="480"></div>
      <div><h2>Get {p["name"]} on any device.</h2><p>Plan meals, order groceries and join the community on the web or on your phone.</p></div>
      <div class="prod__actions" style="--c1:#2e8b3a;--c2:#0a4a26">{store_buttons(p)}</div>
    </div>
  </div>
</section>

{cta_block(d["email"], "Healthy people.<br>Stronger communities.", "Questions about meal plans, deliveries or joining the GreenFed team? Call or write to us.", d["phone"])}
</main>
'''
    html += footer(base)
    (ROOT / "products").mkdir(exist_ok=True)
    (ROOT / "products" / f"{slug}.html").write_text(html, encoding="utf-8")


def am_phone(inner, cls=""):
    return f'<div class="am-phone {cls}" aria-hidden="true"><div class="am-phone__screen">{inner}</div></div>'


def build_aimove(p):
    base = "../"
    d = p["page"]
    slug = p["slug"]
    img = f"{base}assets/img/{slug}"
    tick = lambda xs: "".join(f"<li>{ico('check')}{escape(x)}</li>" for x in xs)
    type_icons = ["bike", "clock", "calendar"]
    types = "".join(f'<div class="am-type reveal" style="--d:{i * .08:.2f}s"><span class="why__ico">{ico(type_icons[i])}</span><div><h3>{escape(a)} <em>{escape(c)}</em></h3><p>{escape(b)}</p></div></div>' for i, (a, b, c) in enumerate(d["types"]))
    stages = "".join(f'<li class="reveal" style="--d:{i * .1:.1f}s"><span>{i + 1}</span><h4>{escape(a)}</h4><p>{escape(b)}</p></li>' for i, (a, b) in enumerate(d["stages"]))
    wallet = "".join(f'<div class="pillar"><h4>{escape(a)}</h4><p>{escape(b)}</p></div>' for a, b in d["wallet"])
    trust_icons = ["shield", "lock", "star", "check"]
    trust = "".join(f'<div class="why__item reveal" style="--d:{i * .08:.2f}s"><div class="why__ico">{ico(trust_icons[i])}</div><h3>{escape(a)}</h3><p>{escape(b)}</p></div>' for i, (a, b) in enumerate(d["trust"]))

    track_phone = am_phone(f'''
      <div class="am-map"><svg viewBox="0 0 200 220" preserveAspectRatio="xMidYMid slice"><defs><pattern id="g" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0H0V20" fill="none" stroke="#dbe6ff" stroke-width="1"/></pattern></defs>
        <rect width="200" height="220" fill="#eef4ff"/><rect width="200" height="220" fill="url(#g)"/>
        <path d="M-10 150 Q60 120 90 160 T210 130" stroke="#fff" stroke-width="14" fill="none"/><path d="M60 -10 Q80 80 50 230" stroke="#fff" stroke-width="10" fill="none"/>
        <path class="am-route" d="M40 185 C70 150 60 110 100 100 S150 60 160 35" stroke="#0256FF" stroke-width="4" fill="none" stroke-linecap="round" stroke-dasharray="6 6"/>
        <circle cx="40" cy="185" r="7" fill="#0256FF"/><circle cx="160" cy="35" r="9" fill="#fff" stroke="#0256FF" stroke-width="4"/>
        <g class="am-rider"><circle r="11" fill="#0256FF"/><circle r="4" fill="#fff"/></g></svg>
        <span class="am-live">● LIVE</span></div>
      <div class="am-sheet"><div class="am-sheet__row"><div><small>Est. arrival</small><b>12 mins away</b></div><span class="am-chip">IN TRANSIT</span></div>
        <div class="am-rider-card"><span class="am-avatar">JJ</span><div><b>John Joshua</b><small>TVS Motorcycle · 4.9 ★</small></div><span class="am-msg">{ico("phone")}</span></div></div>''', "am-phone--hero")

    send_phone = am_phone(f'''
      <div class="am-app-head"><small>Hello Ken 👋</small><b>What would you like to do?</b></div>
      <div class="am-actions"><div class="on">{ico("move")}<b>Send a package</b></div><div>{ico("bike")}<b>Book a rider</b></div><div>{ico("wallet")}<b>Fund wallet</b></div><div>{ico("calendar")}<b>Schedule</b></div></div>
      <div class="am-fare"><small>Automated upfront fare</small><b>₦3,120</b><span>Guaranteed price</span></div>
      <div class="am-transit"><span class="am-dot"></span><div><b>Package in transit</b><small>Your rider is on the way</small></div></div>''')

    rider_phone = am_phone(f'''
      <div class="am-earn"><small>Available earnings</small><b>₦24,800</b><div class="am-earn__stats"><span><b>8</b>Trips today</span><span><b>4.9★</b>Rating</span><span><b>96%</b>Acceptance</span></div></div>
      <div class="am-filters"><span class="on">All (6)</span><span>High payout</span><span>Express</span></div>
      <div class="am-order"><div><span class="am-tag">EXPRESS</span><b>Ikeja → Lekki</b><small>2.8 km · 8 mins</small></div><strong>₦3,950</strong></div>
      <div class="am-order"><div><span class="am-tag am-tag--alt">SAME DAY</span><b>Yaba → Surulere</b><small>5.1 km · 15 mins</small></div><strong>₦2,410</strong></div>
      <div class="am-accept">Accept order &amp; start pickup</div>''')

    html = head(f"{p['name']}: send it, track it, done | Rehohub", d["lead"], base)
    html += header(base)
    html += f'''<main id="main" class="product-page theme-am">
<section class="p-hero am-hero">
  {r_mark("hero__ghost hero__ghost--a")}
  <div class="hero__glow"></div><div class="hero__grid"></div>
  <div class="container p-hero__inner">
    <div class="p-hero__copy">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="{base}index.html">Rehohub</a><span>/</span><a href="{base}index.html#products">Products</a><span>/</span><span aria-current="page">{p["name"]}</span></nav>
      <div class="ap-logo reveal"><img class="am-logo" src="{img}/mark-white.png" alt="" width="399" height="400"><span>{p["name"]}</span><em>{escape(p["cat"])}</em></div>
      <h1 class="reveal" style="--d:.08s">Send it.<br>Track it.<br><span class="hl-am">Done.</span></h1>
      <p class="hero__lead reveal" style="--d:.16s">{escape(d["lead"])}</p>
      <div class="hero__ctas reveal" style="--d:.24s">
        <a class="btn btn--white" href="{p["web"]}" target="_blank" rel="noopener">Send a package {ico("arrow")}</a>
        <a class="btn btn--ghost" href="#fare">Check a price</a>
        <a class="btn btn--ghost" href="#riders">Ride with us</a>
      </div>
    </div>
    <div class="p-hero__media am-hero__media reveal" style="--d:.2s">
      {track_phone}
      <div class="float-chip float-chip--a">{ico("shield")} Guaranteed upfront price</div>
      <div class="float-chip am-chip-b">{ico("pin")} Live GPS tracking</div>
    </div>
  </div>
</section>

<section class="am-types-wrap"><div class="container am-types">{types}</div></section>

<section class="section" id="business">
  <div class="container show">
    <div class="show__copy reveal">
      <span class="eyebrow">For businesses and individuals</span>
      <h2 class="title bar" style="margin-top:16px">Deliveries, sorted from your phone.</h2>
      <p class="lead" style="margin-top:24px">Add your pickup and drop-off, describe the package, and see the price before you pay. Then follow it to the door. Business accounts can add their CAC/RC number and a default pickup address.</p>
      <ul class="ticks ticks--grid">{tick(d["business"])}</ul>
    </div>
    <div class="show__media am-center reveal" style="--d:.1s">{send_phone}</div>
  </div>
</section>

<section class="section section--tint" id="fare">
  <div class="container">
    <div class="section__head section__head--split">
      <div class="reveal"><span class="eyebrow">Fare estimator</span><h2 class="title bar" style="margin-top:16px">Know the price<br>before you book.</h2></div>
      <p class="lead reveal" style="--d:.1s">AiMove works out your fare from distance and weight, and you always see the total before you pay. Try it below.</p>
    </div>
    <div class="fare reveal" data-fare>
      <form class="fare__form" onsubmit="return false">
        <label>Distance <output data-out="km">14.5 km</output><input type="range" name="km" min="1" max="60" step="0.5" value="14.5"></label>
        <label>Package weight <output data-out="kg">5 kg</output><input type="range" name="kg" min="1" max="80" step="1" value="5"></label>
        <fieldset><legend>Delivery type</legend>
          <label class="seg"><input type="radio" name="type" value="SAME_DAY" checked><span>Same-day</span></label>
          <label class="seg"><input type="radio" name="type" value="INSTANT"><span>Instant express</span></label>
        </fieldset>
        <label class="switch"><input type="checkbox" name="peak"><span></span>Peak hours (7–10 am, 5–8 pm)</label>
      </form>
      <div class="fare__out" aria-live="polite">
        <small>Estimated upfront fare</small>
        <strong data-out="total">₦2,540</strong>
        <ul>
          <li><span>Base booking fee</span><b>₦800</b></li>
          <li><span data-out="ratelabel">Distance (₦120/km, light parcel)</span><b data-out="dist">₦1,740</b></li>
          <li><span>Peak-hour surge</span><b data-out="peak">₦0</b></li>
          <li><span>Instant express</span><b data-out="express">₦0</b></li>
        </ul>
        <p>Rates per km: ₦120 up to 5 kg, ₦160 up to 20 kg, ₦220 up to 50 kg, ₦300 above 50 kg. This is an estimate; the app confirms your exact price before payment.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="tracking">
  <div class="container">
    <div class="section__head" style="text-align:center;justify-items:center">
      <span class="eyebrow reveal">Live tracking</span>
      <h2 class="title bar bar--center reveal" style="--d:.08s">Follow every step.</h2>
    </div>
    <ol class="am-stages">{stages}</ol>
  </div>
</section>

<section class="section products-wrap" id="riders">
  {r_mark("hero__ghost hero__ghost--a")}
  <div class="container show show--flip">
    <div class="show__copy reveal">
      <span class="eyebrow eyebrow--light">For riders</span>
      <h2 class="title title--light bar bar--light" style="margin-top:16px">Ride, deliver, get paid.</h2>
      <p class="lead" style="margin-top:24px;color:rgba(255,255,255,.82)">Join AiMove as a rider and pick up orders near you. You'll see each payout before you accept, and you can withdraw your earnings straight to your bank account.</p>
      <ul class="ticks ticks--light ticks--grid">{tick(d["rider"])}</ul>
      <div class="hero__ctas"><a class="btn btn--white" href="{p["web"]}" target="_blank" rel="noopener">Become a rider {ico("arrow")}</a></div>
    </div>
    <div class="show__media am-center reveal" style="--d:.1s">{rider_phone}</div>
  </div>
</section>

<section class="section" id="wallet">
  <div class="container about" style="align-items:start">
    <div class="reveal">
      <span class="eyebrow">Wallet &amp; payments</span>
      <h2 class="title bar" style="margin-top:16px">Pay from your AiMove wallet.</h2>
      <p class="lead" style="margin-top:24px">Pay for deliveries with your wallet or a card. Save several cards and bank accounts, and keep track of every transaction.</p>
      <div class="pillars">{wallet}</div>
    </div>
    <div class="reveal" style="--d:.1s" id="api">
      <span class="eyebrow">For developers</span>
      <h2 class="title bar" style="margin-top:16px">Plug deliveries into your platform.</h2>
      <p class="lead" style="margin-top:24px">Add AiMove to your own systems with the delivery API, and get status updates through webhooks.</p>
      <pre class="code" aria-label="Example API request"><code><span class="c-k">POST</span> /api/v1/deliveries/create
{{ <span class="c-s">"origin"</span>: <span class="c-v">"Lagos"</span>, <span class="c-s">"dest"</span>: <span class="c-v">"Abuja"</span>, <span class="c-s">"weight"</span>: <span class="c-n">5.0</span> }}

<span class="c-m">→ 201</span> {{ <span class="c-s">"status"</span>: <span class="c-v">"CREATED"</span>, <span class="c-s">"id"</span>: <span class="c-v">"pkg_1"</span> }}

<span class="c-k">GET</span>  /api/v1/deliveries/{{tracking}}/track
<span class="c-m">→ 200</span> {{ <span class="c-s">"status"</span>: <span class="c-v">"IN_TRANSIT"</span>, <span class="c-s">"eta"</span>: <span class="c-v">"25 mins"</span> }}

<span class="c-k">WEBHOOK</span> /api/v1/webhooks/status_update</code></pre>
      <ul class="ticks" style="margin-top:20px"><li>{ico("check")}Admins assign riders and see live GPS</li><li>{ico("check")}Real-time performance reports, exportable as PDF</li></ul>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="container">
    <div class="section__head" style="text-align:center;justify-items:center">
      <span class="eyebrow reveal">Safety and trust</span>
      <h2 class="title bar bar--center reveal" style="--d:.08s">Safe hands, every trip.</h2>
    </div>
    <div class="why">{trust}</div>
  </div>
</section>

<section class="section" id="download" style="padding-bottom:0">
  <div class="container">
    <div class="dl reveal">
      <div><img class="dl__logo am-dl-logo" src="{img}/mark-white.png" alt="" width="399" height="400"></div>
      <div><h2>Get {p["name"]} on any device.</h2><p>Send packages, ride and manage deliveries on the web or on your phone.</p></div>
      <div class="prod__actions" style="--c1:#3d7bff;--c2:#0256FF">{store_buttons(p)}</div>
    </div>
  </div>
</section>

{cta_block(d["email"], "Move anything,<br>anywhere.", "Questions about business deliveries, becoming a rider or the AiMove API? Our team is here to help.")}
</main>
'''
    html += footer(base)
    (ROOT / "products").mkdir(exist_ok=True)
    (ROOT / "products" / f"{slug}.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    (ROOT / "services").mkdir(exist_ok=True)
    build_index()
    for i, s in enumerate(SUBSIDIARIES):
        build_service(i, s)
    for p in PRODUCTS:
        if p.get("page"):
            build_product(p)
    import airise
    print(f"Built {airise.build(globals())} AiRise pages.")
    print(f"Built index.html and {len(SUBSIDIARIES)} service pages.")
