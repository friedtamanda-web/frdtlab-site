# FRDT · SITE · Home mobile fix v1 — 2026-11-23

Live state: the 11/23 revert of "Clarify FRDT Lab homepage CTA" (78e5064) is deployed. These three bugs pre-date it.

1. Photo captions ("On stage · SMX", "Studio · Original work") are dark text on a dark pill → unreadable.
   Cause: the brand-2027 reskin remapped --ivory to dark ink; .cap still uses var(--ivory).
2. "FRDT Lab is where marketing strategy becomes infrastructure." — "INFRASTRUCTURE." runs past the right edge on phones (359px in a 326px column).
3. Footer tagline is right-aligned on phones while everything else is left-aligned.

## Patch — paste into index.html right before </head>

<style id="home-mobile-fix-2026-11-23">
.photo-fig .cap,.bridge-fig .cap{color:#F6F4F2!important}
@media(max-width:600px){#what h2{font-size:clamp(24px,7.6vw,33.6px)!important}.foot-tag{text-align:left!important}}
</style>

Verified in-browser on the live page at 390px: captions readable, H2 fits (326/326), zero overflowing text elements.
