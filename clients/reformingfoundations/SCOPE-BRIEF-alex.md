# Reforming Foundations — Website Scope

**For a dev taking a look. What the job is — no pricing, no timeline.**

## The client
Reforming Foundations is a Pilates studio with two locations in metro Detroit (Berkley + Rochester, MI). They also run a 550-hour teacher-training program ("RF School of Pilates"). Booking currently runs through **HelloWalla**; the current site is on **Squarespace**.

## The job in one line
Build them a lean, fast, SEO-strong marketing site on **WordPress** that routes three different kinds of visitors to the right offer, keeps HelloWalla as the booking engine, and can be updated by their own team without a developer.

## First thing to settle
The current growth plan assumes they *stay* on Squarespace. We're now looking at WordPress instead. Before anything else, we need to agree on which build this is:
- **Full WordPress rebuild** (replace Squarespace; migrate content; redirect old URLs), or
- **WordPress front-end layered on** (new marketing/routing pages, existing booking flow untouched).

Everything below assumes the full rebuild, with **HelloWalla kept as the booking system of record** — confirm or push back.

## What gets built

**Pages (few pages, done well — not a sprawling site):**
- Home, feeding into a guided routing step
- A **guided "front door"** — the key custom piece: visitor picks new-to-Pilates / coming-back-after-injury / training-to-teach, and gets sent to the right offer + proof
- Two location pages (Berkley, Rochester)
- Two welcome-offer pages
- Membership page
- School of Pilates (teacher-training) landing page
- A handful of SEO content pages (e.g. "Pilates after physical therapy," beginner-nerves, private vs. group)
- About / founder
- Contact — with a **working contact form** (currently missing)

**Functionality:**
- Guided routing selector (custom)
- HelloWalla booking, embedded or deep-linked — not rebuilt
- Contact + teacher-training inquiry forms with notifications
- Reviews surfaced across the site (they have strong Google reviews)
- Email capture wired to their email platform (flows themselves live in the ESP)
- One analytics view pulling GA4 + Search Console + booking data
- Existing Stripe payment links just wired to buttons (no custom checkout)
- **An easy-edit setup** so their team can swap a price, photo, or testimonial without a dev — hard requirement
- Reusable, branded page/section templates

**SEO / technical (Amanda owns strategy; dev implements):**
- Structured data: two locations, the teacher-training program, FAQs, reviews, services
- Clean metadata + consistent name/address/phone across both locations (there's a stray "phantom" third location in the current metadata to kill)
- Mobile-first, fast (Core Web Vitals)
- Structure aimed at both Google and AI answer engines
- If it's a rebuild: sitemap, canonicals, and 301 redirects from the old Squarespace URLs (Amanda supplies the map)

## Not part of this
- Rebuilding booking (HelloWalla stays)
- Paid ads
- Teacher-training curriculum content
- Photo/video production (handled separately)
- Any always-on marketing automation layer
- Ongoing content writing beyond launch pages

## Who does what
- **Amanda / FRDT:** UX research, information architecture, all copy, brand, SEO + schema strategy, photography.
- **Dev (you):** the WordPress build, integrations, schema implementation, the easy-edit layer, responsive + QA.

## Worth knowing
- Client should **own every account and asset** (hosting, domain, integrations) from day one — nothing locked to us.
- Open items for you to weigh in on: cleanest HelloWalla integration method, WP stack/theme recommendation, hosting, and how reviews get pulled in.
