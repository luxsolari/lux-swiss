# Work log

## 2026-10-23 — Support changes prepared for pull request

- Lux approved the local arrangement and requested PRs for both repositories. Kept the reviewed Support via Agensi wording; explained that it can read as a donation although Agensi sells the skill. No copy change requested.
- Refreshed origin/main; both branches started at current main with no divergence. Reviewed scoped diffs and whitespace checks.
- Verification: static HTML parsed with Python HTMLParser; local browser and screenshot checks recorded above. This repository has no package build manifest.
- Desktop previews inspected; mobile layout remains unverified. Preparing feature/agensi-support for PR against main; no merge or production deployment authorized. Only ignored public-browser configuration exists locally in the website clone.
- Files: docs/index.html, CHANGELOG.md, JOURNAL.md.

## 2026-10-23 — Support callout hierarchy

- Grouped the free/open-source notice and both support buttons inside a named aside with a neutral left border, padding, a Support development label, and normal-size foreground text. Installation remains the main filled action above it.
- Verified the local browser accessibility tree and desktop screenshot: notice and both existing destination links are grouped visibly beneath installation. git diff --check passed. No build needed for this static markup edit; mobile rendering was not checked.
- No push or deployment. Files: docs/index.html, CHANGELOG.md, JOURNAL.md.

## 2026-10-23 — Buy Me a Coffee support placements

- Added Lux's supplied https://buymeacoffee.com/lux.solari profile at the agreed placements: Projects introduction button and blog footer text link in website; outlined button beside Agensi in the Lux Swiss installation section. Retained free/open-source notices and existing purchase/repository actions.
- Verified local browser trees show all three links with the supplied destination; inspected showcase screenshot with both outlined buttons side by side. Website lint passed after escaping a JSX apostrophe. Whitespace checks passed. React review: semantic anchors, descriptive labels, no new state, hooks, dependencies, or requests. Full build/test limitations remain as previously logged.
- Publication remains pending local review; no push or deployment. Files: docs/index.html, CHANGELOG.md, JOURNAL.md.

## 2026-10-23 — Support action as a button

- At Lux's request, moved the Agensi purchase link out of the notice into a separate outlined button using the existing btn btn-outlined styling. Retained the explicit free/open-source notice and optional-support wording.
- Verified the local installation section in the browser and inspected its desktop screenshot: notice above outlined Support via Agensi · $4.99 action, existing free installation above both. git diff --check passed.
- Public publication remains pending; no push or deployment. Files: docs/index.html, CHANGELOG.md, JOURNAL.md.

## 2026-10-23 — Approved Agensi support link

- Browser inspection of https://www.agensi.io/skills/lux-swiss-design-system-plugin confirmed the Lux Swiss listing and $4.99 purchase price after Lux supplied its approved URL.
- Added an optional purchase/support link to the small installation note. The note explicitly says Lux Swiss remains free and open source; existing free installation and license links remain.
- Verified local browser rendering and destination URL at http://127.0.0.1:3101/index.html#install; git diff --check passed. Updated the Unreleased changelog entry. No new build system or dependencies.
- Open: public publication awaits Lux's review. No push, PR, or deployment. No paid-only functionality suggested.
- Files: docs/index.html, CHANGELOG.md, JOURNAL.md.

## 2026-10-23 — Agensi support copy, awaiting listing approval

- Added a small muted note beside the existing installation instructions confirming Lux Swiss remains free and open source. Recorded it under Unreleased in CHANGELOG.md.
- Verified: Python HTMLParser accepted docs/index.html; assertions confirmed the free-install command and license links remain; git diff --check passed.
- Follow-up: browser verified the local showcase at http://127.0.0.1:3101/index.html#install renders the new note beside the original free installation instructions. Server runs outside restricted networking so the browser can reach it. No publication requested; Lux wants local review first.
- License inspection: design content uses CC BY-SA 4.0; tooling uses MIT/X11. No license changes or paid-only functionality claims.
- Open: Lux confirmed the Agensi listing is still under review. Purchase URL and $4.99 price are not publicly verified. Add the optional support link here only after approval. No browser render or automated build was run; this is a static HTML site without a package build manifest.
- Ruled out: guessed URLs, placeholder purchase actions, and claims of exclusive paid features. No push, PR, or deployment performed.
- Files: docs/index.html, CHANGELOG.md, JOURNAL.md.
