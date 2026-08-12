# Public-release preflight

Before changing repository visibility from PRIVATE to PUBLIC:

- [ ] `README.md` renders correctly.
- [ ] No raw fundus images are tracked.
- [ ] No `.pth`, `.pt`, `.ckpt`, or oversized ZIP files are tracked.
- [ ] No API keys, Hugging Face tokens, passwords, or credentials are present.
- [ ] No author-specific absolute local paths remain; provenance placeholders use `<LOCAL_PROJECT_ROOT>`.
- [ ] Dataset manifest contains 594 unique samples and final class/source labels.
- [ ] Immutable outer/nested/LODO fold files are present.
- [ ] ROI provenance limitation is stated explicitly.
- [ ] `python scripts/audit_integrity.py` passes.
- [ ] `python scripts/reproduce_nested_primary_metrics.py` reproduces the canonical nested metrics.
- [ ] `python scripts/audit_public_package.py` passes.
- [ ] Third-party dataset/model terms have been checked.
- [ ] Authors have decided whether an explicit code license will be added.
- [ ] Public GitHub URL will be inserted in the manuscript and response letter only after visibility is PUBLIC.
