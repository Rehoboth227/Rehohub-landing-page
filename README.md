# Rehohub — Brand Landing Page

A static, responsive landing site for **Rehohub**, built from the Rehohub Brand Guidelines.

## Structure

```
index.html              Home page: hero, about, mission/vision, services, products, contact
services/<slug>.html    A landing page for each of the 10 subsidiaries (services)
products/<slug>.html    A landing page for each product that has `page` data (AiPay, GreenFed, AiMove)
products/airise/        The AiRise mini-site (HR and employability): 9 section pages + 9 course pages
assets/media/<product>/ Product walkthrough videos (muted, looping) and their poster frames
assets/css/styles.css   Design system and all styles
assets/js/main.js       Interactions (menu, scroll reveal, rotating headline, counters)
assets/img/             Logo, favicon and photography from the brand guidelines
scripts/build.py        Generator for index.html, services/*.html and products/*.html
scripts/airise.py       Generator for the AiRise mini-site (called by build.py)
assets/js/airise.js     AiRise course filter, result calculator, certificate reader, checklist
```

## Brand application

| Guideline | Implementation |
|---|---|
| Colour palette `#1760BA` · `#2185FF` · `#FFFFFF` | CSS tokens `--blue-700`, `--blue-500`, `--white`; derived navy tints for depth |
| Typography: Hurme Geometric Sans 4 (Normal / Semibold / Black) | First in the font stack; **Outfit** (Google Fonts) is the web fallback. Self-host Hurme via `@font-face` if you hold a web licence |
| Logo, word mark and logo icon | The "R" mark is rebuilt as an SVG from the guidelines; full lock-up in the header, icon as the favicon and hero centrepiece |
| Clear space (50% of logomark height) | The logo always has padding around it, and no other elements sit inside that space |
| Heading underline bar device | `.bar` utility under section titles |
| Icon pattern (merchandise) | Animated R-pattern strip between Services and Products |

## Editing content

All subsidiaries, products and links live in the **DATA** section at the top of `scripts/build.py`.
Edit there, then regenerate:

```bash
python3 scripts/build.py
```

### Product pages

A product gets its own page when its `PRODUCTS` entry has a `page` dict (see `AIPAY_PAGE`).
The home-page card then links to it automatically. AiPay's yellow (`--ai-yellow`) is a campaign
accent taken from the AiPay posters and is used only on the AiPay page. GreenFed uses its own greens (`.theme-gf`) from the GreenFed logo, with Kaushan Script for its handwritten accents. AiMove content comes from the AiMove Android app
(github.com/Rehoboth227/Aimove); its fare estimator in `assets/js/main.js` mirrors the app's `PricingEngine.kt`,
so update both if pricing changes.

### Product links — replace before launch

The AiPay, AiMove, AiRise and GreenFed web-app and store URLs are **placeholders**
(e.g. `https://aipay.rehohub.com`, `com.rehohub.aipay`). Update `web`, `ios` and `android`
for each product in `PRODUCTS` once the apps are live.

## Running locally

No build step is needed to view the site. Open `index.html` in a browser, or run:

```bash
python3 -m http.server 8000
```

## AiRise mini-site

AiRise is built as an HR company site rather than a single page. Its content lives in `scripts/airise.py`
(courses, journey, HR services, platform modules, delivery options) and comes from the AiRise documents:
Executive Summary, Draft A requirements, Programme Overview, Assessment Pack and Certificates.

The Assessment Pack is the **facilitator edition**: only its structure and rules (marks, timings, pass marks,
result bands, re-sits, appeals, integrity) are published. Answer keys, model answers and marking guides are
deliberately left out and must stay private.
