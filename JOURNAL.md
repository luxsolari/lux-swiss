# Work log

## 2026-10-26 — Refine edition layout and support copy

- Remove duplicate install CTA and host-specific marketing/header wording. Retain concrete installation commands; preserve the open-source aside.
- Add brief thanks, one full-width primary action per card on a shared baseline, an optional coffee link, and a four-row semantic comparison table. Remove stacked nested-section bottom padding before the rules divider.
- Verification pending: philosophy/whitespace, desktop/mobile browser layout and remote checks. No native plugin, runtime, version, license, price or listing change. Files: docs/index.html, docs/assets/site.css, CHANGELOG.md, JOURNAL.md. Previous local readback preserved in a named stash.

## 2026-10-26 — Restore the original open-source aside

- At Lux's request, replace the compact comparison introduction with the original line: Open source has many virtues; paying for its own development is rarely one of them.
- Keep the concise edition descriptions, optional coffee route, paid workflow, corrected banners and all destinations. No extra support section is introduced; the same sentence is already retained on the personal site's Projects page.
- Verification pending at entry creation: philosophy/whitespace and exact live readback. Copy-only; no runtime, styling, price, license or Agensi listing change. Files: docs/index.html, CHANGELOG.md, JOURNAL.md.

## 2026-10-26 — Shorten the edition comparison

- Trim repeated support/product explanations to one short paragraph per edition plus an optional-coffee note. Shorten CTAs to Get the free plugin and Get Supporter Edition; retain their destinations and both support choices.
- Keep the existing evergreen present-tense copy, banner family/variant hierarchy and compact layout fixes. Condense footer requirements while retaining the image-tool requirement and linked reference-delivery details.
- Verification pending at entry creation: philosophy/whitespace and local rendered layout; no native plugin/runtime/version/license or Agensi product change. Files: docs/index.html, CHANGELOG.md, JOURNAL.md. Header grouping remains in the separate site PR.

## 2026-10-26 — Make Supporter Edition comparison evergreen

- At Lux's explicit request, describe Supporter Edition contents in the present tense and remove preparation/review notices from the public comparison and matching README. Keep the listing reference for current version/files/price, open-source completeness and image-tool/reference-delivery limits.
- Further correction: the family rename had left the old one-line banner typography in place, causing clipping and poor contrast over the artwork. Split the family label from the large short variant name in the responsive cover, standalone banner source and social-card source. Add compact-container spacing; no asset colors or shapes changed. Responsive/browser fit checks follow.
- Follow-up from Lux: make the two support routes explicit. The free card offers source plus an optional coffee thank-you; the paid card explains additional workflow and managed Agensi access. Remove the separate competing support aside.
- Removed the temporary planned-bundle sentence; no new bundle URL, price, availability badge, native identifier, version, runtime or license change.
- This is authorized forward-facing copy, not independent verification that the parallel Agensi submission has been approved. Publication/serving status remains recorded separately in the owner journal.
- Verification pending at entry creation: philosophy checks and whitespace; exact PR/merge/live readback follow. Files: docs/index.html, README.md, CHANGELOG.md, JOURNAL.md.

## 2026-10-26 — Explain Open Source and Supporter Edition

- Added an edition comparison to the showcase and README: free complete interface plugin versus paid Agensi workflow with the planned Image Direction companion and managed access. Preserve separate optional coffee support; remove fixed-price/donation-only purchase wording.
- Mark updated packs as in preparation/review; do not claim the new pack or bundle is live. State host/image-reference delivery limits and link to primary Agensi guidance. Native plugin names/identifiers, versions, licenses, theme and runtime remain unchanged.
- Verification pending at entry creation: philosophy checks, HTML/link validation and local layout inspection; checked PR and live readback follow. Prior JOURNAL-only verification note retained in named stash.
- Scope: docs/index.html, README.md, CHANGELOG.md, JOURNAL.md. Agensi listing edits remain in the separate active commercial task; no concurrent remote listing mutation here.

## 2026-10-26 — Unify the Lux Visual Systems family

- Changed active branding, repository/install identifiers and explicit skill/command references to the three owner-approved family names. Preserved historical changelog/journal entries, source snapshots, licenses, binary assets and version numbers. Source identifiers are a breaking migration; users must select/reinstall the new package.
- Site scope is project cards and their repository/demo links, plus an explicitly private Image Direction card without a private repository URL or a commercial availability claim.
- Verified locally: both six-test package suites and philosophy checks, 16 Codex catalogue tests and renamed package validators, 131 Hermes Python tests, eight image-library/contract tests and the Claude marketplace regression passed in UTF-8 with canonical Git line endings. Hosted PR CI and final remote links remain pending. No new release tag or version is invented.
- Open: checked PRs, remote repository renames, Pages URLs and installed/private-vault migration. Do not infer deployment from local edits.
- Ruled out: rewriting old releases/provenance and changing repository visibility or licenses. Relevant files: manifests, SKILL.md, package paths, README/docs, catalogues/validators and site lib/projects.ts where present.

## 2026-10-24 — Release 2.6.0 with separated artifacts

- Lux requested new releases via existing CI, explicitly authorizing administrator bypass where needed, and local Agensi packages. Bump script derived v2.6.0; synchronized manifest, changelog, and demo footer version labels.
- Both builders pass: native plugin ZIP has seven files and preserved manifest/skill layout; local Agensi ZIP has six files. All six package regression tests, philosophy check, and whitespace check pass. CI invokes/uploads only the public native-plugin builder and checksum.
- The screenshot-referenced private-packaging-pr.txt and other PR drafts were loose workspace files, not tracked in any repo. Archived them outside the workspace after a sandbox move failure. New PRs use inline descriptions, with no draft text files added to a repo.
- Preparing release PR and version tag; public CI publication and downloaded-asset verification still pending. No Agensi upload. Files: .claude-plugin/plugin.json, CHANGELOG.md, docs/*.html, JOURNAL.md.

## 2026-10-24 — Public artifact separation merged

- Merged PR #29 normally with minimal public native plugin packaging; Agensi-specific release assets remain removed. Read back main's workflow via GitHub API and verified only native plugin packaging is invoked/uploaded. Current release custom-asset count is zero.
- Next version-tag publication will attach the seven-file native plugin ZIP and checksum; no new release or historical tag rewrite performed. Local Agensi ZIPs remain available for manual submission. Post-merge audit entry is local only.

## 2026-10-24 — Minimal public native-plugin release artifact

- Lux requested slimming normal release artifacts and updating CI in both repos. Added a separate seven-file public plugin builder preserving .claude-plugin/plugin.json, skills/<name>/SKILL.md, theme, component reference, HOUSE-MARK.md, and both original licenses. Unlike the local Agensi ZIP, this keeps native plugin layout and does not flatten or adapt files.
- Release CI runs native-package tests and publishes only <name>-plugin-VERSION.zip plus checksum. The Agensi builder is never invoked or uploaded. Automatic GitHub Source code archives remain unmodified full snapshots; README explains the distinction and local build command.
- Verified three native-package regressions per repo (repeatable bytes/allowlist/native layout, missing theme rejection, unexpected skill-path rejection), philosophy compliance, and whitespace checks. Local candidates: 20,602 bytes. No new version tag or release requested for this CI change; next tagged release will attach the public native artifact.
- Preparing a new PR after #28's merge. Public Agensi assets have already been deleted; verified local copies retained. Files: scripts/package_plugin.py, scripts/test_package_plugin.py, .github/workflows/release.yml, README.md, CHANGELOG.md, JOURNAL.md.

## 2026-10-24 — Keep Agensi submission packages out of public releases

- Lux explicitly requested deletion of public Agensi build outputs. Removed the ZIP and checksum release assets, retaining verified copies in the task's local release-assets folders. Removed the marketplace build/test/upload step from Release CI; ordinary changelog-based release creation remains.
- Corrected README and release changelog wording so they no longer offer marketplace packages as public assets. Local packaging tools remain available for maintainer uploads. No source-archive, version-tag, native plugin, or Agensi listing deletion.
- Verified the workflow has no marketplace-builder invocation or release-upload command, while the normal release-create/edit path remains. Whitespace checks pass. Preparing a corrective PR; release-page notes will be refreshed from the corrected version section. No new version tag required.
- Files: .github/workflows/release.yml, README.md, CHANGELOG.md, JOURNAL.md.

## 2026-10-24 — v2.5.0 published through Release CI

- At Lux's explicit request, merged PR #27 without bypass at 9476246aedbc0df2b994059d4a51bb7ce953e5f3 and pushed signed annotated tag v2.5.0. Existing Release workflow run 40120621452 succeeded; no manual release creation used.
- Downloaded the published lux-swiss-agensi-2.5.0.zip and checksum to ../lux-swiss-release-assets; verified SHA-256 and all six payloads against the locally checked build. Agensi upload/update remains for Lux; no marketplace mutation performed.
- Post-release audit entry remains local only; no source changes after publication. Files: JOURNAL.md.

## 2026-10-24 — v2.5.0 release preparation via existing CI

- User requested a new Lux Swiss release and explicitly reiterated using the repository release machinery. Bump suggester recommends minor v2.5.0 from v2.4.0; synchronized plugin manifest, changelog dated 2026-10-24, and demo footer labels. Extended PR #27 to include release metadata.
- Rebuilt six-file lux-swiss-agensi-2.5.0.zip (19,955 bytes); three package regression tests, philosophy checker, changelog extraction, and whitespace checks passed. No design behavior changes. Release will be triggered by a signed version tag only after PR merge, using the existing Release workflow; no manual release publication.
- Open: merge PR, push tag, confirm CI and downloadable artifact checksum. No Agensi upload. Files: .claude-plugin/plugin.json, CHANGELOG.md, docs/*.html, JOURNAL.md and packaging changes from prior entry.

## 2026-10-24 — Preemptive Agensi packaging audit

- Latest v2.4.0 release has no attached assets; its source tree has 58 tracked files (current main has 60), exceeding the 50-file threshold quoted in Tri-Swiss's rejection. The skill itself needs three files plus the house-mark explanation and license notices. Repository plans and screenshot tooling are not runtime dependencies.
- Added the same six-file allowlist builder, metadata tags, endpoint-purpose disclosure/local font and chart alternatives, README artifact guidance, and existing Release CI asset attachment as Tri-Swiss. Kept the native plugin manifest/layout and repository history. No version bump or publication requested; changes remain under Unreleased. Candidate ZIP uses the current manifest version and is not an official v2.4.0 release asset.
- Three packaging regressions pass (reproducibility/exclusion, broken relative reference rejection, credential-shaped payload rejection), philosophy checker passes, builder verifies six-file ZIP contents and checksum, and whitespace checks pass. Candidate is 19,955 bytes. A bounded scan for GitHub/AWS/Stripe credential formats and private-key headers found no matches in tracked text; this is not an exhaustive secret audit or an Agensi approval claim.
- Set ZIP creator platform explicitly for stable metadata across Windows/Linux. Tests ran outside the sandbox due to its known temporary-directory restriction. No design tokens or components changed; no new visual checks needed.
- Preparing feature/agensi-package PR; no merge, tag, release, or Agensi upload. Files: scripts/package_agensi.py, scripts/test_package_agensi.py, skills/lux-swiss/SKILL.md, .github/workflows/release.yml, .gitignore, README.md, CHANGELOG.md, JOURNAL.md.

## 2026-10-24 — Approved merge and public verification

- Lux explicitly requested all three PRs be merged and made live. This repository's merge commit: 19ec21209d0f93444c07faff8ed1b0342bc8b7a3.
- GitHub Pages build completed without error. Browser verified the public installation support callout, spare-time joke, free/open-source notice, Agensi purchase and coffee destinations.
- Public verification was desktop/browser content and link inspection, not a new full test or mobile run. Tri-Swiss listing approval remains pending; no purchase URL or price was fabricated.
- This post-release audit entry is local only to avoid another publication cycle for log-only changes. No source changes after merge. Files: JOURNAL.md.

## 2026-10-24 — Review branches for pending Tri-Swiss listing

- Lux requested PR preparation and Coming soon on Agensi actions on the Tri-Swiss project card and demo while approval is pending. Used disabled native buttons without destination or price, retaining existing free access and coffee actions. Published the previously approved spare-time demo copy for review as well.
- HTML parsing and git diff --check passed. Copy-only addition; no new visual/mobile check.
- Updating existing draft PR #26. No merge or production deployment. Agensi destination and price remain pending approval for Tri-Swiss.
- Files: docs/index.html, CHANGELOG.md, JOURNAL.md.

## 2026-10-23 — Spare-time joke in demo support callout

- Added the approved Built in my spare time sentence and open-source-development joke before the existing free/open-source notice in the support aside. Preserved all existing buttons and destinations.
- Verified HTML parsing, one occurrence of the joke inside the support aside, and git diff --check. Copy-only local edit; no new browser, build, or mobile check. No push, merge, or deployment.
- Files: docs/index.html, CHANGELOG.md, JOURNAL.md.

## 2026-10-23 — Explicit Agensi purchase label

- At Lux's request, changed the Agensi action to Buy on Agensi · $4.99 to distinguish a skill purchase from a contribution. Destination, price, free/open-source notice, and Buy Me a Coffee action are unchanged.
- Verified the scoped diff and git diff --check. Copy-only edit; earlier build/test results remain applicable, with no new full run. Updating the existing PR branch; no merge or production deployment.
- Photography support was discussed as a possible /photos callout; no photography-specific changes authorized or made.
- Files: docs/index.html, JOURNAL.md.

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
