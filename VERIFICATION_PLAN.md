# Verification Plan

## Checks

Run the public-export gate before publishing changes:

```bash
python3 repo_preflight.py --repo . --profile public-export --paranoid
```

Manual review:

- Confirm no personal contact details, private planning notes, employer references, or machine-specific details are present.
- Confirm external links are intentional public links.
- Confirm descriptions point to public-safe repositories only.

## Release Decision

Release only when automated checks and manual boundary review pass.
