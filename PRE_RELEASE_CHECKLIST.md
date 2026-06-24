# Pre-Release Checklist

- [x] Profile uses public-safe identity boundaries.
- [x] Public repository links are intentional.
- [x] No personal contact details or private planning notes are included.
- [x] Claims avoid employment, client, production, compliance, and certification assertions.
- [x] Public-export gate has been run before release using the canonical command in `VERIFICATION_PLAN.md` (with `--config public-profile-rule-pack.json`); any findings on gitignored, untracked local files were judged against `git ls-files` and are not publication blockers.
