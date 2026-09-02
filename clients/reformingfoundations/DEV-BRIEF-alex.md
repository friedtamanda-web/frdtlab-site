# Reforming Foundations — Website Build · Scoping Brief

**For:** Alex (development)
**From:** Amanda Friedt · FRDT Lab
**Date:** August 2026
**Ask:** Review this and come back with a phased build estimate, timeline, recommended WordPress stack, and your open questions.

---

## 0. TL;DR

Reforming Foundations is a two-location Pilates studio in metro Detroit (Berkley + Rochester, MI) with a 550-hour teacher-training program. FRDT Lab is delivering a growth system; **you're scoping the website build on WordPress.**

Division of labor:
- **Amanda / FRDT:** UX research, information architecture, all copy, brand, SEO + schema *strategy*, photography (shoot day), page templates/wireframes.
- **Alex:** WordPress build, technical implementation, integrations, responsive/QA, schema *implementation*, the "easy-update" editing layer.

I need from you: **effort estimate by phase, a timeline, a recommended stack, build-vs-plugin calls, and a risks/dependencies list.**

---

## 1. ⚠️ The one decision that drives the whole estimate

The client-facing growth strategy was written around **keeping their existing Squarespace site + HelloWalla booking** ("no re-platforming, HelloWalla stays the source of truth"). We're now looking at WordPress instead. Before you estimate, we need to lock which of these you're building:

- **Option A — Full WordPress rebuild.** Replace Squarespace entirely. New site, migrate content, set up redirects from old URLs. HelloWalla still handles booking (embed/deep-link).
- **Option B — WordPress front-door only.** New guided-entry + marketing/SEO pages on WordPress, existing booking flow untouched. Lighter build, but two systems to keep visually consistent.

**Working assumption for this brief: Option A** (full WP build, HelloWalla retained as the booking system of record). **Please confirm or push back** — it changes everything below.

---

## 2. Business context (so the scope makes sense)

- **Two locations:** Berkley (flagship — 4.8★, 78 Google reviews) and Rochester. Real rooms, capped small classes (6–8, capped at 6 in Berkley).
- **RF School of Pilates:** a 550-hour teacher-training program. High-ticket funnel; currently invisible in search. Big priority.
- **Three audiences / three front doors:** (1) new to Pilates, (2) coming back after injury/PT, (3) training to become an instructor.
- **Booking today:** HelloWalla.
- **Known defects to fix:** a "phantom" third location baked into site metadata, a welcome offer missing its price, and no contact form on the contact page.

---

## 3. Site architecture (pages & templates)

Deliberately lean — "a few pages done right," not a sprawling rebuild. Amanda supplies final IA + copy; you build the templates.

| Page / template | Notes |
|---|---|
| Home | Entry point into the guided routing experience |
| **Guided front-door routing** | *Custom component* — 3 paths (new / comeback / teach) that route each visitor to the right offer + proof. Core feature. |
| Location page ×2 | Berkley, Rochester — each with LocalBusiness schema, NAP, hours, map |
| Welcome-offer page ×2 | Clearly priced, proof/testimonials, booking CTA |
| Membership | Pricing + upsell after welcome offer |
| **School of Pilates** landing | Teacher-training funnel → info-session inquiry |
| SEO content pages | "Is Pilates safe after physical therapy," beginner-intimidation page, private-vs-group comparison |
| About / founder | Credentials, story |
| Contact | **Working form** (currently missing) + routing/notifications |
| Pricing | Consolidated offers |

Reusable, branded **post/page template system** so new content drops into a consistent look without a designer.

---

## 4. Functionality to build

1. **Guided routing front door** — interactive selector (3 audiences) → correct offer + proof. Highest-value custom piece.
2. **Booking integration** — embed or deep-link into **HelloWalla**; do *not* rebuild booking. Need your recommendation on cleanest integration method.
3. **Contact / inquiry forms** — incl. a teacher-training info-session inquiry path (not a dead-end).
4. **Reviews engine** — surface best reviews across the site (not buried on home), plus a review-ask/response rhythm (the ask workflow may live outside WP — flag).
5. **Email capture + flows** — integrate an ESP (see §5). Flows themselves may be built in the ESP, but the site needs capture points + triggers.
6. **Analytics dashboard** — GA4 + Search Console + booking data into one view. Looker Studio is fine unless you'd suggest otherwise.
7. **Deposit / payments** — **already handled by existing Stripe payment links** (3 live `buy.stripe.com` URLs). These are just button links — no custom checkout needed.
8. **"Easy-update" editing layer** — the client's team must update a price, swap a photo, or add a testimonial **without a developer**. This is a hard requirement (ACF/block patterns/page-builder — your call).
9. **Agentic/automation layer** *(likely separate workstream)* — FRDT runs workflows that draft posts and flag SEO/schema gaps. Probably out of the core web build, but note any hooks/endpoints you'd want exposed.

---

## 5. Integrations checklist

- **HelloWalla** — booking (retain; integration method TBD → your reco)
- **GA4** + **Google Search Console** — tracking
- **ESP** — *which one?* (Klaviyo is in our stack; confirm)
- **Stripe** — payment links exist, just wire buttons
- **Google Business Profiles ×2** + directory profiles (Yelp, WellnessLiving, Tripadvisor) — NAP consistency + reviews source

---

## 6. SEO / technical requirements (Amanda leads strategy; you implement)

- **Schema:** LocalBusiness ×2 locations, Course / EducationalOrganization (teacher training), FAQPage, Review / AggregateRating, Service.
- **Metadata cleanup:** eliminate the phantom third location everywhere; consistent NAP.
- **Performance:** mobile-first, Core Web Vitals green.
- **Findability:** clean taxonomy/structure aimed at both Google and AI answer engines (GEO).
- **Migration hygiene (if Option A):** XML sitemap, robots, canonicals, and **301 redirects** from old Squarespace URLs — Amanda provides the URL map.

---

## 7. Explicitly OUT of scope (for the web build)

- Rebuilding booking (HelloWalla stays)
- Paid advertising setup/management
- Teacher-training curriculum / CEC program content
- Photo/video production (separate shoot day)
- The autonomous agentic marketing layer (separate workstream)
- Ongoing content writing beyond launch pages

---

## 8. Suggested phasing (mirrors the client plan, ~10–16 wks)

- **Phase 0 (wk 1–2):** Foundation — metadata/schema, both GBPs, contact form live, welcome-offer pricing fixed, GA4/GSC + dashboard wired.
- **Phase 1 (wk 3–8):** Guided front-door routing live, both offer pages, testimonials on pricing/location pages, first content gap closed.
- **Phase 2 (wk 9–16):** School of Pilates landing, post-PT + beginner content pages, reviews engine, email flows.
- **Phase 3 (mo 5+):** Expansion — CEC page, additional content hubs, re-test AI visibility.

---

## 9. What to send back

- Recommended **WP stack** (block theme + ACF? Bricks/GeneratePress? page-builder choice) + hosting reco
- **Effort estimate by phase** (hours or fixed) + confidence level
- **Timeline** aligned to the phases above
- **Build-vs-plugin** decisions (forms, reviews, schema, dashboard)
- **Risks & dependencies** — especially HelloWalla integration + Squarespace migration
- **What you need from Amanda**, and by when
- Your **assumptions**

---

## 10. Open questions

1. **Option A vs B** (full rebuild vs front-door-only)? — the big one.
2. Cleanest **HelloWalla** integration — iframe/embed, API, or deep link?
3. **ESP** — confirm Klaviyo (or your preference).
4. **Hosting** — your reco. Note: **client must own every account/asset from day one** (hard requirement).
5. Squarespace **content export + URL inventory** for redirects — who pulls it?
6. **Reviews** — pull live via Google API, or manual curation?
7. **Dashboard** — Looker Studio acceptable?
8. **Schema** — you own implementation from Amanda's spec, or just expose the fields?

---

*Note: client owns all accounts and assets from day one — please keep hosting, domains, and integrations in the client's name, nothing locked to us.*
