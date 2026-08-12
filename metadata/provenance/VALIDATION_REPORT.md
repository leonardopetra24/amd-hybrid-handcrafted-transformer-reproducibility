# Dataset Provenance Validation Report

## Scope

This report documents the internal validation of correspondence among raw,
preprocessed, and ROI images. It is an audit record and is not intended to
replace the scientific methods description.

## NORMAL provenance reconstruction

- Total NORMAL samples: 287
- Automatic high-confidence assignments: 243
- Assignments requiring visual verification: 44
- Visually verified as correct: 44
- Incorrect assignments after review: 0
- Unresolved assignments: 0
- Final validated NORMAL mappings: 287/287

## Final retained dataset

- Retained samples: 594
- Accepted mapping statuses:
  - AUTO_CONFIRMED
  - MANUALLY_VERIFIED
  - CONFIRMED (deterministic non-NORMAL filename correspondence)
- Blocking failures: 0

## Interpretation

The automatic matcher produced the candidate assignments. High-confidence
NORMAL assignments retain the status `AUTO_CONFIRMED`. Assignments originally
flagged because of conservative confidence or margin criteria retain a distinct
audit trail and are recorded as `MANUALLY_VERIFIED` after visual confirmation.
They are not relabeled as automatic confirmations.

All final statuses preserve how each correspondence was validated.
