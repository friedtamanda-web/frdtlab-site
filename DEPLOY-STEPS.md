# FRDTLAB — Deploy steps

This folder is the complete, ready-to-publish frdtlab.com site.

## What changed in this build
- Work With Me: Speaking block reframed to AI & Marketing only, with a #speaking anchor and a return link to The Unapologetic Leader for the leadership keynotes.
- Footer: removed the dead "Guide" link; fixed the Unapologetic link to point to theunapologeticleader.com (was a wrong domain).
- Includes the Signal Report PDF and the CNAME (frdtlab.com).

## Publish (GitHub Pages)
1. Open your frdtlab.com GitHub repo.
2. Upload the CONTENTS of this folder (not the folder itself), letting it overwrite existing files. Keep the CNAME file.
3. Commit to the branch GitHub Pages serves (usually `main`).
4. Pages redeploys in 1–2 minutes. Hard-refresh frdtlab.com/work-with-me.html to confirm the Speaking block reads "Speaking · AI & Marketing" and the #speaking anchor works.

## Note
There is no guide.html in this build, and nothing links to it. The old guide.html may still exist in the live repo from before — if you want it fully gone, delete guide.html directly in GitHub. Leaving it does no harm since nothing points to it.
