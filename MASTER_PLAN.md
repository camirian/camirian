# Master Plan

## 1. Executive Summary

Facts:
- This repo is the public GitHub profile and portfolio hub for the `camirian` identity. Evidence: `README.md`, `SPEC.md`.
- The public wedge is Fieldheld Recorder, positioned as a synthetic CLI for replayable, reviewable, rollbackable autonomous-run evidence bundles. Evidence: `README.md`.
- The repo contains a generated YouTube banner asset and a Python banner generator. Evidence: `generate_banner.py`, `final_youtube_banner_master_2560.png`, `QUICKSTART.md`.
- The repo has explicit public-boundary rules: no private planning notes, credentials, personal contact details, customer data, employer/client material, or unsupported production/compliance claims. Evidence: `SPEC.md`, `SECURITY.md`, `PUBLIC_SURFACE_WAIVERS.md`.

Assumptions:
- This repo remains public-facing and should optimize for trust, clarity, and safe portfolio routing rather than product implementation.

Recommendations:
- Treat this as a public profile control plane: curated links, proof surfaces, generated visual asset workflow, and strict public-surface verification before any publish.
- Define "ready" as all public claims link to public-safe evidence, the banner regenerates, and public-export checks plus manual boundary review pass.

## 2. Current-State Findings, With File/Path Evidence

Facts:
- `README.md` lists live demos and portfolio repositories across Fieldheld/Governable Autonomy, Physical AI, and a knowledge-base lane.
- `SPEC.md` defines the goal, non-goals, public boundary, and success criteria for the public profile.
- `VERIFICATION_PLAN.md` requires a public-export gate and manual review before publishing profile changes.
- `PUBLIC_SURFACE_WAIVERS.md` narrows allowed public identity terms but does not waive checks for secrets or private data.
- `generate_banner.py` uses Pillow to generate `final_youtube_banner_master_2560.png`; `QUICKSTART.md` compiles and regenerates it.
- No root `AGENTS.md` was present in the inspected top-level file list, so workspace rules and repo docs provide the operating boundary.
- Recent commits show profile security guardrails and public profile identity waiver work. Evidence: `git log --oneline -5`.
- The working tree was clean before this plan was created. Evidence: `git status --short`.

Assumptions:
- The external demo links in `README.md` should be rechecked before future profile publication.

Recommendations:
- Add a lightweight link and claim verification routine rather than expanding product code in this repo.
- Keep strategy and unreleased roadmap details in private repos only.

## 3. Product Requirements

Target users:
- Public visitors evaluating technical range and proof surfaces.
- Recruiters, collaborators, and design partners looking for public evidence.
- The repo owner and agents maintaining a safe public profile.

Primary workflows:
- Update public portfolio links and descriptions.
- Regenerate profile/banner assets.
- Run public-surface and manual boundary checks.
- Preserve waivers and security policy.

Non-goals:
- No private strategy.
- No full resume vault.
- No customer pipeline.
- No production claims for linked demos unless those repos prove them.

Requirements:
- PR-1: Every listed project links to a public-safe repo or demo.
- PR-2: Every claim is either descriptive, evidence-backed, or removed.
- PR-3: Public-sensitive-term waivers stay narrow and documented.
- PR-4: Generated assets can be regenerated with a documented command.
- PR-5: No private planning, local machine, employer, customer, or secret material appears.
- PR-6: Manual visual review is required for generated images before publishing.

## 4. DORA AI Capability Alignment

Facts:
- The repo describes agent evidence workflows and governable autonomy, but its own implementation surface is profile docs and a banner generator.

Allowed AI use:
- Drafting public-safe summaries from already-public repos.
- Checking link consistency, claim consistency, and public-surface risk.
- Generating or reviewing visual asset variations from non-sensitive prompts.

Restricted AI use:
- Summarizing private strategy, personal career vault content, or unreleased repos into public copy.

Prohibited AI use:
- Publishing contact details, private planning, employer/client references, credentials, or unsupported claims.

DORA alignment actions:
- Data ecosystem: maintain a source register for each public link and demo.
- AI-accessible data: only use public repos, public videos, and this repo's checked-in files.
- Version control: small public profile changes; no generated scratch artifacts.
- Small batches: one profile section or asset change per change set.
- User-centricity: target job is public trust and reviewer routing.
- Internal platform: one command should compile/regenerate banner and one command should run public-surface checks.
- Missing evidence: no local script for link checking was found; add one or document an approved command.

## 5. Architecture Plan

Existing architecture:
- `README.md`: public profile content and portfolio routing.
- `generate_banner.py`: local asset generator.
- `final_youtube_banner_master_2560.png`: generated visual output.
- `SPEC.md`, `VERIFICATION_PLAN.md`, `PRE_RELEASE_CHECKLIST.md`, `PUBLIC_SURFACE_WAIVERS.md`, `SECURITY.md`: public boundary and release controls.

Proposed architecture:
- Keep the repo docs-first.
- Add an optional `scripts/verify_public_profile.py` or documented external preflight command to validate links, blocked terms, and local asset presence.
- Keep generated images at root only when intentionally public.
- Keep private strategy and detailed roadmap elsewhere.

Data flow:
1. Public-safe source repo or demo is selected.
2. Profile copy is drafted.
3. Public-surface checks run.
4. Manual review checks claims, links, and asset output.
5. Only reviewed content remains in `README.md`.

ADR candidates:
- Whether to pin external demo links in a machine-readable manifest.
- Whether generated banner source should remain Python/Pillow or move to a design asset workflow.

## 6. Feature Roadmap

Milestone 1: Profile source register
- Acceptance: each README link has a source type, status, and verification date in a local manifest or table.

Milestone 2: Public profile verification command
- Acceptance: a repeatable command checks local file presence, public links, and blocked private-boundary terms.

Milestone 3: Banner asset workflow hardening
- Acceptance: banner generation has dependency notes and visual review criteria.

Milestone 4: Claim quality pass
- Acceptance: descriptions avoid unsupported production, compliance, safety, employment, or customer assertions.

Milestone 5: Release gate consolidation
- Acceptance: `PRE_RELEASE_CHECKLIST.md` and `VERIFICATION_PLAN.md` align with the actual preflight command and manual review.

## 7. Parallelization Plan

Parallelizable workstreams:
- Link/source register.
- Public-copy claim review.
- Banner generator dependency and visual review docs.
- Verification script/procedure.

Sequential work:
- Public README updates should wait until link and claim review is complete.
- Waiver expansion must be reviewed before any new public identity terms are allowed.

Ownership boundaries:
- One worker owns public text.
- One worker owns verification tooling.
- One worker owns visual asset workflow.
- One reviewer owns final public-surface gate.

## 8. Task Backlog

- Build a public-link manifest for README demo and repo links; verify each URL intentionally belongs on the public profile.
- Add or document a local public-export check command; verify it does not read secrets.
- Add banner generator dependency notes for Pillow; verify `python3 -m py_compile generate_banner.py`.
- Add visual review criteria for `final_youtube_banner_master_2560.png`; verify dimensions after regeneration.
- Reconcile `PRE_RELEASE_CHECKLIST.md` with the actual verification command and rule pack.
- Add README claim review checklist; verify no unsupported production/compliance claims.

## 9. Testing And Verification Plan

Current checks:
- `python3 -m py_compile generate_banner.py`.
- `python3 generate_banner.py`.
- Public-export gate described in `VERIFICATION_PLAN.md` using the profile rule pack.

Planned checks:
- Link checker for README public links.
- Rule-pack validation for public-sensitive terms.
- Generated image dimension and file-presence check.
- Manual review for public claims, private-boundary terms, and external link intent.
- Git diff review before publishing.

## 10. Release Criteria

Ready for profile publication:
- Public-export gate passes.
- Manual review finds no private planning notes, secrets, customer data, personal contact details, or unsupported claims.
- All public links are intentional and reachable.
- Banner asset is visually reviewed after regeneration if changed.
- Waivers remain limited to explicitly public identity terms.

Not ready:
- Any link points to private, missing, or unreleased material.
- Any description claims production, regulated, safety, customer, or compliance readiness without public evidence.
- Any generated asset was changed without visual review.

## 11. Risks And Open Questions

Risks:
- High: profile README is public, so stale or overbroad claims directly affect trust.
- High: accidental private strategy leakage.
- Medium: external links can rot or point to changed content.
- Medium: generated image dependencies may differ across machines.

Open questions:
- Should public demo/link state be stored in a manifest?
- Should profile copy be generated from public repo metadata to reduce drift?
- Which external public check command is canonical if `repo_preflight.py` is outside this repo?

## 12. Recommended First Implementation Slice

Add a public-profile link and claim verification routine.

Why first:
- This repo is a public surface; public safety and claim accuracy matter more than new features.

Changes:
- Add a small verification script or documented checklist that checks README links, required files, and rule-pack availability.
- Align `VERIFICATION_PLAN.md` and `PRE_RELEASE_CHECKLIST.md` with that routine.

Does not change:
- No private strategy.
- No new portfolio claims.
- No publishing action.

Acceptance criteria:
- Verification command or checklist covers links, banner files, public-boundary terms, and claim review.
- Banner compile check still passes.
- README remains public-safe.
