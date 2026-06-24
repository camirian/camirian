# Master Plan (Canonical)

> **Relationship to the root `MASTER_PLAN.md`:** a root `MASTER_PLAN.md` already
> existed when this document was written and is **not overwritten**. This file
> (`docs/MASTER_PLAN.md`) is the **canonical** plan and supersedes the root one.
>
> FACT: the root plan describes the public wedge as "Fieldheld Recorder" and a
> Fieldheld/Governable-Autonomy framing. The current `README.md` (working tree)
> has been rewritten to a broader "Applied AI · Agentic Systems · Robotics
> Simulation" framing and **no longer links `fieldheld-recorder`**. The root plan
> is therefore **stale** relative to the current README. This document plans
> against the current state.

Each section separates **FACTS** (evidence in the repo), **ASSUMPTIONS**
(reasonable but unverified), and **RECOMMENDATIONS** (proposed actions).

---

## 1. Executive Summary

**FACTS**
- This repo is the public GitHub profile/portfolio repository for the `camirian`
  identity; its `README.md` renders on the GitHub profile page. Evidence:
  `README.md`, `SPEC.md`, `AGENTS.md`.
- It is explicitly a *sanitized publication surface, not a planning workspace*.
  Evidence: `AGENTS.md`.
- The only executable artifact is `generate_banner.py` (Pillow), which renders
  `final_youtube_banner_master_2560.png`. Evidence: `generate_banner.py`,
  `QUICKSTART.md`, `.devcontainer/Dockerfile`.
- Public-boundary controls exist: `SPEC.md`, `SECURITY.md`,
  `PUBLIC_SURFACE_WAIVERS.md`, `VERIFICATION_PLAN.md`, `PRE_RELEASE_CHECKLIST.md`,
  and a rule-pack `public-profile-rule-pack.json`.

**ASSUMPTIONS**
- The repo stays public-facing and should optimize for trust, clarity, and safe
  portfolio routing rather than product implementation.

**RECOMMENDATIONS**
- Treat the repo as a documentation-first public control plane: curated links,
  proof surfaces, a reproducible banner workflow, and a strict, *internally
  consistent* public-export gate before any publish.

---

## 2. Current-State Findings (with file evidence)

**FACTS**
- `README.md` (working tree) presents a positioning statement and a "Selected
  public work" table linking `agentic-systems-verifier-case-study` and two
  robotics demo videos. It states robotics source lives in private clean-room
  repos with sanitized exports.
- `git diff README.md` shows an **uncommitted rewrite**: the prior README linked
  `fieldheld-recorder` and three demos under a Fieldheld framing; the new one
  drops `fieldheld-recorder` and narrows the table. This is preserved user work.
- `SPEC.md` defines goal, non-goals, public boundary, and success criteria.
- `VERIFICATION_PLAN.md` invokes `python3 repo_preflight.py --repo . --profile
  public-export --paranoid` — a **bare script name and no `--config`**.
- `PUBLIC_SURFACE_WAIVERS.md` invokes the scanner via a full external path **with
  `--config public-profile-rule-pack.json`**. The two commands disagree (see §6/§12).
- `public-profile-rule-pack.json` allowlists exactly `caaren` and `caaren amirian`.
- `generate_banner.py` uses Pillow; verified locally with
  `python3 -m py_compile generate_banner.py` (passes). Installed Pillow is 12.x;
  `.devcontainer/Dockerfile` pins `Pillow==10.4.0` and installs `fonts-liberation2`.
- `.gitignore` ignores `HANDOFF.md` and `docs/OPERATING_STANDARD.md`; both are
  present locally but **untracked** (`git ls-files` returns nothing for them), so
  they are never published.
- Running the canonical public-export gate against the working tree currently
  reports **1 blocker + 1 warning**: blocker `private_publication_surface` on
  `HANDOFF.md` (a gitignored, untracked, local-only file), and warning
  `public_history_requires_audit` (26 commits). Evidence: scanner JSON output.

**ASSUMPTIONS**
- The HANDOFF.md blocker is a false positive for *publication* purposes because
  the file is gitignored and never reaches the public remote; the scanner reads
  the working tree, not git-tracked content.

**RECOMMENDATIONS**
- Document the scanner's working-tree behavior so the gate result is interpreted
  correctly, and reconcile the conflicting verification commands (§12 slice).
- Recheck external README links before any future publish.

---

## 3. Product Requirements

**FACTS** — target users: public visitors evaluating technical range; recruiters,
collaborators, design partners seeking public evidence; the owner and agents
maintaining the surface.

Primary workflows: update portfolio links/descriptions; regenerate the banner;
run the public-export gate; preserve waivers and security policy.

**RECOMMENDATIONS** — requirements:
- PR-1: Every listed project links to a public-safe repo or demo.
- PR-2: Every claim is descriptive, evidence-backed, or removed (no production,
  compliance, safety, employment, or customer assertions without public proof).
- PR-3: Public-sensitive-term waivers stay narrow and documented.
- PR-4: Generated assets regenerate with a documented command.
- PR-5: No private planning, employer/customer, secret, absolute-path, or
  machine-specific material appears.
- PR-6: Manual visual review of generated images before publish.
- PR-7: The verification command is *single-sourced* and internally consistent
  across all release docs.

Non-goals (FACT, from `SPEC.md`): private strategy, full resume vault, customer
pipeline, production/compliance claims for linked demos.

---

## 4. DORA AI Capability Alignment

**FACTS** — the repo describes agentic evidence/governable-autonomy *as portfolio
subject matter*; its own implementation surface is docs plus a banner generator.

**RECOMMENDATIONS**
- *Allowed AI use:* drafting public-safe summaries from already-public repos;
  checking link/claim consistency and public-surface risk; reviewing banner
  variations from non-sensitive prompts.
- *Restricted AI use:* summarizing private strategy or unreleased repos into
  public copy.
- *Prohibited AI use:* publishing contact details, private planning,
  employer/client references, credentials, or unsupported claims.
- *DORA alignment actions:* maintain a source register per public link; use only
  public sources; keep changes in small batches (one section/asset per change);
  make the banner regen and the public-export gate one documented command each;
  fix the missing-evidence gap that the verification command is not single-sourced.

---

## 5. Architecture Plan

**FACTS** — existing structure:
- `README.md` — public content and portfolio routing.
- `generate_banner.py` → `final_youtube_banner_master_2560.png` — asset workflow.
- `.devcontainer/` — reproducible render environment (Pillow + Liberation fonts).
- `SPEC.md`, `VERIFICATION_PLAN.md`, `PRE_RELEASE_CHECKLIST.md`,
  `PUBLIC_SURFACE_WAIVERS.md`, `SECURITY.md`, rule-pack — public-boundary controls.
- The public-export scanner is an **external tool** outside this repo.

**RECOMMENDATIONS** — proposed structure:
- Keep the repo documentation-first; do not add a duplicate in-repo checker (the
  external scanner already exists; AGENTS.md discourages inventing code).
- Single-source the canonical verification command; reference it from each
  release doc.
- Keep generated images at root only when intentionally public.

**ADR candidates:** whether to store external demo/link state in a machine-readable
manifest; whether banner source stays Python/Pillow or moves to a design workflow.

---

## 6. Feature Roadmap (milestones + acceptance criteria)

- **M1 — Verification command reconciliation.** Acceptance: `VERIFICATION_PLAN.md`,
  `PRE_RELEASE_CHECKLIST.md`, and `PUBLIC_SURFACE_WAIVERS.md` all reference one
  canonical public-export command (with `--config`), and the documented
  working-tree/gitignore caveat is captured. *(This is the §12 first slice.)*
- **M2 — Profile source register.** Acceptance: each README link has a source
  type, status, and verification date in a local table/manifest.
- **M3 — Banner workflow hardening.** Acceptance: Pillow version note and visual
  review criteria documented; dimensions checked after regeneration.
- **M4 — Claim-quality pass.** Acceptance: README descriptions avoid unsupported
  production/compliance/safety/employment/customer assertions.
- **M5 — Stale-plan cleanup.** Acceptance: root `MASTER_PLAN.md` is either
  refreshed or clearly marked superseded by this document.

---

## 7. Parallelization Plan

**RECOMMENDATIONS**
- Parallelizable: link/source register; public-copy claim review; banner docs;
  verification-doc reconciliation.
- Sequential: README publish waits on link + claim review; waiver expansion needs
  review before any new public identity term is allowed.
- Ownership: one owner for public text; one for verification docs; one for the
  visual asset workflow; one reviewer owns the final public-surface gate.

---

## 8. Task Backlog

Each item: *files affected · tests/verification · docs · done condition.*

- **T1 (slice):** Reconcile the canonical public-export command and document the
  gitignore/working-tree caveat. *Files:* `VERIFICATION_PLAN.md`,
  `PRE_RELEASE_CHECKLIST.md`. *Verify:* run the gate; confirm no *new* blocker is
  introduced; `py_compile` still passes. *Docs:* this plan, `CLAUDE.md`. *Done:*
  all release docs reference the same `--config` command and the HANDOFF.md/
  working-tree behavior is explained.
- **T2:** Build a public-link manifest/table for README links. *Files:* new
  `docs/` table. *Verify:* each URL intentionally public + reachable. *Done:*
  every README link has source type/status/date.
- **T3:** Banner dependency + visual-review notes. *Files:* `QUICKSTART.md`.
  *Verify:* `python3 -m py_compile generate_banner.py`; regen and check 2560x1440.
  *Done:* Pillow version and review criteria documented.
- **T4:** README claim-review checklist. *Files:* `PRE_RELEASE_CHECKLIST.md`.
  *Verify:* no unsupported claims. *Done:* checklist applied to current README.
- **T5:** Mark/refresh root `MASTER_PLAN.md`. *Files:* root `MASTER_PLAN.md`.
  *Done:* relationship to this canonical plan is explicit.

---

## 9. Testing & Verification Plan

**FACTS** — checks that exist today:
- `python3 -m py_compile generate_banner.py` (passes).
- `python3 generate_banner.py` (renders the banner).
- Public-export gate (canonical, with rule pack):
  ```bash
  python3 <path-to>/repo_preflight.py --repo . --profile public-export \
    --paranoid --config public-profile-rule-pack.json
  ```

**RECOMMENDATIONS** — planned checks: link reachability for README URLs; rule-pack
validation for public-sensitive terms; banner dimension/file-presence check;
manual review of claims, boundary terms, and link intent; `git diff` review
before publish. Interpret scanner findings against `git ls-files` (ignore
gitignored/untracked local files such as `HANDOFF.md`).

---

## 10. Release Criteria

**RECOMMENDATIONS** — ready to publish when:
- The public-export gate passes, or its only findings are known false positives on
  gitignored/untracked local files (documented), with no *new* blocker on tracked
  content.
- Manual review finds no private planning, secrets, customer/employer data,
  contact details, absolute local paths, or unsupported claims.
- All public links are intentional and reachable.
- The banner is visually reviewed after any regeneration.
- Waivers remain limited to `caaren` / `caaren amirian`.

Not ready: any link to private/missing/unreleased material; any production/
regulated/safety/customer/compliance claim without public evidence; any changed
asset not visually reviewed.

---

## 11. Risks & Open Questions

**Risks**
- High: stale or overbroad public claims directly affect trust (the README is the
  profile front page).
- High: accidental private-strategy or absolute-path leakage into a public push.
- Medium: external links rot or change content.
- Medium: banner render differs across machines (Pillow 12.x local vs. 10.4.0
  pinned; font availability).

**Open Questions**
- Should public link state live in a machine-readable manifest?
- Should profile copy be generated from public repo metadata to reduce drift?
- Should the root `MASTER_PLAN.md` be deleted, refreshed, or left as a superseded
  artifact?

---

## 12. Recommended First Implementation Slice

**Reconcile the canonical public-export verification command and document the
working-tree/gitignore caveat.**

**Why first:** It is the smallest genuinely-useful change, it is documentation
(matching AGENTS.md's "short, verifiable updates" and "not a planning workspace"),
and it fixes a real inconsistency: `VERIFICATION_PLAN.md` invokes the scanner with
a bare name and **no `--config`**, while `PUBLIC_SURFACE_WAIVERS.md` uses the rule
pack. Without `--config`, the identity-term allowlist is not applied, so the gate
can behave differently than the documented one. It does **not** invent code or
duplicate the existing external scanner.

**Changes:**
- `VERIFICATION_PLAN.md`: use the canonical command (with
  `--config public-profile-rule-pack.json`) and explain that the scanner reads the
  working tree, so gitignored/untracked local files (e.g. `HANDOFF.md`) may appear
  and should be judged against `git ls-files`.
- `PRE_RELEASE_CHECKLIST.md`: add a line tying the gate to the canonical command.

**Does not change:** no private strategy; no new portfolio claims; no publish
action; no touching the uncommitted README rewrite.

**Acceptance criteria:**
- All release docs reference one canonical public-export command with `--config`.
- The working-tree/gitignore caveat is documented.
- `python3 -m py_compile generate_banner.py` still passes.
- Running the gate introduces **no new blocker** on git-tracked content.
- README remains public-safe and untouched.
