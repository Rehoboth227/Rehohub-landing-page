# Rehohub — Brand Landing Page

A static, responsive landing site for **Rehohub**, built from the Rehohub Brand Guidelines.

## Structure

```
index.html              Home page: hero, about, mission/vision, services, products, contact
services/<slug>.html    A landing page for each of the 10 subsidiaries (services)
assets/css/styles.css   Design system and all styles
assets/js/main.js       Interactions (menu, scroll reveal, rotating headline, counters)
assets/img/             Logo, favicon and photography from the brand guidelines
scripts/build.py        Generator for index.html and services/*.html
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

### Product links — replace before launch

The AiPay, AiMove, AiRise and GreenFed web-app and store URLs are **placeholders**
(e.g. `https://aipay.rehohub.com`, `com.rehohub.aipay`). Update `web`, `ios` and `android`
for each product in `PRODUCTS` once the apps are live.

## Running locally

No build step is needed to view the site. Open `index.html` in a browser, or run:

```bash
python3 -m http.server 8000
```
