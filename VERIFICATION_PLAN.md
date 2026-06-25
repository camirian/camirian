# Verification Plan

## Checks

Run the public-export gate before publishing changes. This is the canonical
command and must match `PUBLIC_SURFACE_WAIVERS.md`: it passes the profile rule
pack with `--config` so the public identity-term allowlist is applied.

```bash
python3 <path-to>/repo_preflight.py \
  --repo . \
  --profile public-export \
  --paranoid \
  --config public-profile-rule-pack.json
```

The scanner is an external tool that lives outside this repository, and it scans
the **working tree** rather than git-tracked content. Files that are present
locally but gitignored and untracked (for example `HANDOFF.md` and
`docs/OPERATING_STANDARD.md`, both listed in `.gitignore`) can therefore appear in
results even though they are never published. Judge any finding against what git
actually tracks (`git ls-files`); a finding on a gitignored, untracked file is not
a publication blocker.

Manual review:

- Confirm no personal contact details, private planning notes, employer references, or machine-specific details are present.
- Confirm external links are intentional public links.
- Confirm descriptions point to public-safe repositories only.

## Release Decision

Release only when automated checks and manual boundary review pass.
