# FRDTLAB — Ship Guide (GitHub Pages → frdtlab.com)

Three pages, the images, and the support files. Deploy the **whole folder as-is**.
All your real links are already baked in (Substack, LinkedIn, Instagram, TikTok, hello@frdtlab.com).

> One thing to confirm: the contact email is set to **hello@frdtlab.com**. Set that up as a
> free forwarding address in GoDaddy (Email → Forwarding) so it lands in your inbox.

---

## PART 1 — Put the files on GitHub

**Option A — drag-and-drop (no terminal):**
1. On GitHub, create a new repository — name it `frdtlab-site` (Public).
2. On the repo page: **Add file → Upload files**.
3. Drag in **everything inside this folder** — `index.html`, `institution.html`, `guide.html`,
   `404.html`, `og-image.jpg`, `favicon.svg`, `robots.txt`, `sitemap.xml`, and the **`img`** folder.
   (Upload the *contents*, not the outer folder — `index.html` must sit at the repo root.)
4. **Commit changes.**

**Option B — terminal (if you prefer):**
```bash
cd path/to/this/folder
git init
git add .
git commit -m "FRDTLAB site"
git branch -M main
git remote add origin https://github.com/friedtamanda-web/frdtlab-site.git
git push -u origin main
```

---

## PART 2 — Turn on GitHub Pages + custom domain

1. Repo → **Settings → Pages**.
2. **Build and deployment → Source:** "Deploy from a branch". **Branch:** `main`, folder `/ (root)`. Save.
3. Wait ~1 minute. A temporary URL appears: `https://YOUR-USERNAME.github.io/frdtlab-site/`. Click it, confirm it loads.
4. Still in **Settings → Pages → Custom domain:** type `frdtlab.com` → **Save**.
   (This writes a `CNAME` file into the repo automatically — leave it there.)
5. Leave **Enforce HTTPS** unchecked for now; check it once the domain verifies (Part 3).

---

## PART 3 — The GoDaddy DNS records (REAL values — paste these)

GoDaddy → **My Products → DNS** for frdtlab.com. Add these. Delete any existing
"Parked" `A`/`CNAME` on `@` or `www` that conflict.

**Apex domain `frdtlab.com` — four A records (all four, same Name `@`):**

| Type | Name | Value | TTL |
|------|------|-------|-----|
| A | @ | `185.199.108.153` | 1 hour |
| A | @ | `185.199.109.153` | 1 hour |
| A | @ | `185.199.110.153` | 1 hour |
| A | @ | `185.199.111.153` | 1 hour |

**`www` subdomain — one CNAME:**

| Type | Name | Value | TTL |
|------|------|-------|-----|
| CNAME | www | `friedtamanda-web.github.io` | 1 hour |

> This is filled in for your account (`friedtamanda-web`). Keep the trailing `.github.io` —
> **no** repo name, **no** `https://`, **no** trailing slash.

**Optional but recommended — IPv6 (four AAAA records, Name `@`):**
`2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`

DNS propagates in minutes-to-hours. Back in **Settings → Pages**, GitHub will show
"DNS check successful" — then tick **Enforce HTTPS**. `https://frdtlab.com` is live.

---

## Updating the site later
- **Drag-drop:** repo → Add file → Upload files → replace → commit. Live in ~1 min.
- **Terminal:** edit files → `git add . && git commit -m "update" && git push`.

## After it's live (free, high-value)
1. **Google Search Console** (search.google.com/search-console) → add frdtlab.com → submit `sitemap.xml`.
2. **Test the share card:** paste `https://frdtlab.com` into the LinkedIn Post Inspector and opengraph.xyz — confirm the OG image renders.

---

## What's in this folder
```
index.html          Home — the manifesto / why FRDTLAB exists
institution.html    The Institution — proof, divisions, roadmap, stage recognition, join
guide.html          Infrastructure Era Marketing — the full training guide (your dark brand)
img/                14 photos (web-optimized)
og-image.jpg        Social share card
favicon.svg         Browser-tab mark
robots.txt          Search-engine welcome + sitemap pointer
sitemap.xml         All three pages, frdtlab.com URLs
404.html            Branded "page not found"
DEPLOY.md           This file
```

## Alternate host (if you skip GitHub)
Netlify: drag this folder onto **app.netlify.com/drop**, then Domain settings → add `frdtlab.com`.
Netlify gives you *its own* records (apex A `75.2.60.5`, `www` CNAME → `your-site.netlify.app`).
Use those instead of the GitHub records above — don't mix the two.
