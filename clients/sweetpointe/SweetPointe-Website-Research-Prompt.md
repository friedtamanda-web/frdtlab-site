# Sweet Pointe Candy — Website Foundations Deep Research Prompt

## Platform, Architecture, Local Search, Agentic GEO, and Conversion Strategy for a New Small-but-Complete Site

You are an elite integrated growth strategist specializing in local search, Generative Engine Optimization (GEO), AI-answer visibility, ecommerce platform architecture, POS-integrated commerce, conversion design, small-business retail, gifting and experiential retail, and agentic website build systems.

You combine the capabilities of a senior team from Google Search, OpenAI/Perplexity search, BrightLocal, Ahrefs/Semrush, SparkToro, a POS-integration specialist, and a top conversion agency.

Do not produce a generic SEO audit, and do not recommend a large custom rebuild.

Your job is to define **what Sweet Pointe Candy's new website should be** — a small, fast, conversion-first site that gets found and turns local demand into parties, gift boxes, and corporate/realtor gifting — built on the foundations that make it discoverable in Google, Maps, and AI answers, and **integrated with the store's existing Lightspeed POS rather than migrated to Shopify.**

Clearly separate:
1. What ships in the initial 8–10 week build (small site, all foundations)
2. What the team maintains themselves afterward via a simple UI
3. What is deliberately deferred to a later phase (shipping ecommerce, subscriptions, paid)

## Business

- **Business:** Sweet Pointe Candy — a candy destination, opened April 2026
- **Location:** Grosse Pointe Park, Michigan (Kercheval corridor)
- **Current site:** sweetpointecandy.com (a Lightspeed instant site — brochure + local ordering MVP)
- **POS / system of record:** Lightspeed Retail (register, inventory, day-to-day)
- **Heritage:** the corner traces to Lee's Grocery, 1932
- **Positioning:** an all-ages destination people drive 35–50 minutes for — candy is the traffic driver; the money is in gifting, parties, and experiences

## The Engagement This Research Serves

An 8–10 week **website + social** engagement ($5,000 base + optional $2,000 Local Revenue Pack, $7,000 max). The website deliverable is a **smaller site with every foundation** — not a sprawling rebuild. Research must be actionable inside that scope and budget, and buildable by an agentic workflow with a simple hand-off UI for a non-technical team.

## Central Research Questions

1. What does the Sweet Pointe audience actually search for, and what local/AI queries are winnable now? (Anchor: "candy near me" ≈ 40,000/mo; "candy stores grosse pointe," "retro candy michigan," "michigan gift baskets," "candy buffet grosse pointe.")
2. What is the smallest set of pages that captures the highest-value demand (local discovery, parties, gift boxes, corporate/realtor gifting)?
3. **Platform decision:** what is the best way to build a modern, SEO/GEO-capable, conversion-first site that keeps Lightspeed as the source of truth — Lightspeed eCom (E-Series / Ecwid engine), a headless front end synced via Lightspeed's API, or a third-party sync (e.g., SKUPlugs, 24Seven)? Compare on SEO control, schema support, custom landing pages, speed, cost, team-editability, and inventory sync fidelity. Explicitly evaluate the cost/risk of *not* migrating to Shopify.
4. What foundations must ship on day one for the site to be found in Google, Maps, and AI answers (GBP alignment, LocalBusiness/CandyStore + Product + FAQ + Event schema, Core Web Vitals, clean URLs, tracking)?
5. What conversion paths matter (book a party, order a box, request a gifting quote, join the list), and where does the current Lightspeed instant site lose people?
6. How does Sweet Pointe become a **named, cited source** in ChatGPT, Google AI Overviews/AI Mode, and Perplexity for local candy, gifting, and party queries?
7. What can a non-technical team realistically maintain through a simple UI, and what should stay in FRDT's hands?

## Research Requirements

### 1. Platform & Integration Analysis (the core decision)
Reverse-engineer the current sweetpointecandy.com stack. Then evaluate, with sources:
- **Lightspeed eCom (E-Series)** — native POS/inventory sync, but assess its SEO/GEO ceiling: can it do custom local landing pages, FAQ/Event schema, fast Core Web Vitals, clean URL structure, and blog/gift-guide content?
- **Headless / decoupled front end** (e.g., a lightweight framework site) pulling catalog/inventory from Lightspeed via API — assess SEO/GEO control vs. build/maintenance cost for a small team.
- **Third-party sync** (SKUPlugs, 24Seven Commerce, etc.) bridging Lightspeed to another storefront — assess reliability and double-system risk.
- **The Shopify counterfactual** — quantify what re-platforming would cost Dave: abandoning Lightspeed POS *or* running two inventory systems (double entry, sync conflicts). Make the "stay on Lightspeed" case explicit and evidence-based, or refute it.
Recommend one primary path and one fallback, scored on: SEO/GEO control, schema support, custom pages, speed, team-editability, inventory-sync fidelity, cost, and migration risk.

### 2. Search Demand & Intent (candy destination, hyperlocal)
Validate and expand local + gifting demand: "candy near me," "candy store grosse pointe / detroit," "michigan candy delivery," "retro candy michigan," "candy buffet / candy near me for parties," "corporate candy gifts michigan," "michigan gift baskets," "birthday party grosse pointe." Classify by awareness, local intent, commercial intent, booking likelihood, and AI-answer potential. Map each cluster to a page (home, parties, gift boxes, gifting, or an FAQ/gift-guide).

### 3. Audience → Page Fit
Using the store's audience (65% aged 26–50, white-collar, gifting-driven; channel affinity YouTube/Facebook/Instagram over TikTok), define the smallest page set and the message/offer/CTA for each. Separate customer language from industry terms.

### 4. The Minimum Complete Sitemap
Recommend the exact pages for the first build and justify each on demand + revenue. Baseline hypothesis to validate or revise: Home, Parties (bookable), Gift Boxes, Corporate & Realtor Gifting, About/Heritage, Contact/Visit, and an FAQ hub engineered for AI extraction. Flag which are Phase-1 vs. later.

### 5. GEO & AI-Answer Engineering
Test representative prompts across ChatGPT, Google AI Overviews/AI Mode, and Perplexity (record whether Sweet Pointe is named, competitors named, sources cited, and the gap). Starter prompts:
- "Best candy store near Grosse Pointe / Detroit?"
- "Where can I book a kids' birthday party with candy near Grosse Pointe?"
- "Unique local corporate gift under $50 in metro Detroit?"
- "Where can I find retro / nostalgic candy in Michigan?"
- "Candy near me for a party this weekend?"
Recommend the machine-extractable components (BLUF answers, question-shaped H2s, decision tables, location facts, FAQ) and the schema stack (LocalBusiness/CandyStore, Product, Offer, FAQPage, Event) that get the store cited. Do not recommend inaccurate schema.

### 6. Conversion & Foundations Audit
Audit the current Lightspeed instant site's conversion paths, mobile speed, CTAs, booking/ordering friction, trust signals, and the placeholder-social-link problem. Document every hesitation point. Specify the day-one foundations: GA4 + Search Console, GBP alignment, schema, Core Web Vitals targets, clean URLs, and the four tracked conversions (party bookings, box orders, gifting inquiries, email signups).

### 7. The Agentic Build + Team UI
Define how FRDT builds this with an agentic workflow (speed/cost advantage) and what simple UI the team gets to self-serve — update a price, swap a photo, publish a box or a party package, post — with no developer. Specify the trigger/inputs/AI task/human-review/output for each maintenance workflow, and the guardrails.

### 8. Measurement
A minimum viable dashboard tying site behavior to the four revenue conversions. No vanity metrics.

## Required Deliverables

1. **Executive answer** — in plain terms, *what Dave's website will be*: the platform decision, the page set, and the foundations, with the one-line reason each.
2. **Platform decision matrix** — options scored (SEO/GEO, schema, custom pages, speed, team-edit, sync fidelity, cost, migration risk) with a clear recommendation and fallback.
3. **Minimum complete sitemap** — pages, purpose, primary CTA, Phase-1 vs. later.
4. **Search & demand map** — clusters → pages, with volumes where verifiable (label estimates).
5. **GEO/AI baseline** — prompt table (named? competitors? sources? action).
6. **Foundations checklist** — schema, tracking, GBP, Core Web Vitals, URLs.
7. **Agentic build + team-UI spec** — what ships, what the team maintains, what FRDT keeps.
8. **What we ship in 8–10 weeks vs. what's deferred.**

## Research Standards
- Inspect the live sweetpointecandy.com and Lightspeed's current eCom capabilities.
- Cite sources with direct links; label unavailable data; do not invent search volume or fabricate AI tests.
- Distinguish facts, observations, inferences, recommendations.
- Keep it buildable by a small team inside an 8–10 week, $5–7K engagement.
- Do not default to Shopify; make the Lightspeed-integrated case on evidence.
- Do not confuse traffic with revenue.

## Final Standard
The finished research must answer: **What exactly is Sweet Pointe's new website — the platform, the pages, and the foundations — and why is it the right small build to get the store found, convert local demand into gifting and parties, and stay on Lightspeed instead of re-platforming?**
