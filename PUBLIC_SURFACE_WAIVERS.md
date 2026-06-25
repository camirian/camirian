# Public Surface Waivers

This repository is the public GitHub profile repository for `camirian`.

## Public Identity Terms

The terms `caaren` and `caaren amirian` are intentionally public in this repository because they identify the public profile owner and public channel links.

These waivers are limited to public-sensitive-term scanning for this profile repository. They do not waive checks for secrets, tokens, private keys, personal contact details, private planning notes, customer data, employer/client material, or unsupported production, safety, compliance, or certification claims.

Use the profile rule pack when running public-export checks:

```bash
python3 <path-to>/repo_preflight.py \
  --repo . \
  --profile public-export \
  --paranoid \
  --config public-profile-rule-pack.json
```
