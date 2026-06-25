# CLAUDE.md

Guidance for Claude Code and other agents working in this repository.

## What this repository is

This is the **public GitHub profile and portfolio repository** for the `camirian`
identity (a `username/username` profile repo whose `README.md` renders on the
GitHub profile page). It is a *sanitized publication surface*, not a planning
workspace or product codebase.

Evidence: `README.md`, `SPEC.md` ("Maintain a public GitHub profile README..."),
`AGENTS.md` ("This is a public profile and portfolio surface. Treat it as a
sanitized publication repo, not a planning workspace.").

## Contents (facts)

- `README.md` — the rendered profile: a short positioning statement plus a
  "Selected public work" table linking to public case studies and demo videos.
- `generate_banner.py` — a standalone Pillow script that renders
  `final_youtube_banner_master_2560.png` (a 2560x1440 YouTube banner). It depends
  on the Liberation Sans Bold TrueType font and falls back to a default font.
- `final_youtube_banner_master_2560.png` — the generated banner asset.
- `SPEC.md` — goal, non-goals, public boundary, and success criteria.
- `VERIFICATION_PLAN.md`, `PRE_RELEASE_CHECKLIST.md` — release controls.
- `PUBLIC_SURFACE_WAIVERS.md` — narrow allowlist of public identity terms and the
  canonical public-export scan command.
- `public-profile-rule-pack.json` — rule-pack config (identity-term allowlist)
  consumed by the public-export scanner.
- `SECURITY.md` — security/disclosure policy for the public surface.
- `LICENSE` — all rights reserved; profile/portfolio content, no reuse license.
- `MASTER_PLAN.md` (root) — an earlier plan. The canonical plan is
  `docs/MASTER_PLAN.md`; see that file for the relationship.
- `.devcontainer/` — a Python 3.10 dev container that installs `fonts-liberation2`
  and `Pillow==10.4.0` so the banner renders reproducibly.
- `docs/OPERATING_STANDARD.md` and `HANDOFF.md` exist locally but are **gitignored**
  (see `.gitignore`) and are not part of the public published repo.

There is no application code, test suite, or build pipeline beyond the banner
generator and the documentation set.

## How to work here

Follow `AGENTS.md` first. In short:

- Keep every change **public-safe and evidence-bounded**. Do not add private
  planning, private/unreleased repo names, customer or employer material,
  personal contact details, secrets/credentials, absolute local paths, or
  machine-specific artifacts.
- Prefer **short, verifiable doc/portfolio updates** over broad positioning
  rewrites or new code. This repo is documentation-first.
- Only the identity terms `caaren` and `caaren amirian` are allowlisted as
  intentionally public (`public-profile-rule-pack.json`,
  `PUBLIC_SURFACE_WAIVERS.md`).
- Make the smallest change that satisfies the need, verify with the narrowest
  useful check, and update docs if the workflow changed
  (`docs/OPERATING_STANDARD.md`).

## Common commands (facts)

Regenerate the banner (writes `final_youtube_banner_master_2560.png`):

```bash
python3 generate_banner.py
```

Syntax-check the generator:

```bash
python3 -m py_compile generate_banner.py
```

Run the public-export gate before publishing changes (the canonical command,
with the profile rule pack — see `VERIFICATION_PLAN.md`):

```bash
python3 <path-to>/repo_preflight.py \
  --repo . \
  --profile public-export \
  --paranoid \
  --config public-profile-rule-pack.json
```

The scanner is an **external tool** that lives outside this repository. Note that
it reads the working tree, so locally-present but gitignored files (e.g.
`HANDOFF.md`) can surface in results even though they are never published; review
findings against what git actually tracks (`git ls-files`).

## Definition of done (from AGENTS.md)

- The public narrative remains coherent from `README.md`.
- Linked projects are public-safe and still relevant.
- No private planning, unreleased implementation detail, or credential material
  was added.

## Safety

- This is a public repository. Never commit secrets, `.env`, private network
  details, or local workspace artifacts.
- Report suspected security issues privately per `SECURITY.md`; do not open
  public issues containing sensitive material.
