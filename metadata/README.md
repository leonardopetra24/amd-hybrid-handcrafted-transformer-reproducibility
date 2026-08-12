# AMD Dataset 594 — Production v1

## Release status

**FROZEN**

This directory is the immutable production release reconstructed and validated
from the 597-sample master collection. Three exact duplicate images were
excluded, leaving 594 retained unique samples.

## Contents

- `RAW_594/`: raw images renamed by immutable `sample_id`
- `PREPROCESSED_594/`: validated preprocessed images
- `ROI_594/`: validated ROI images
- `outer_fold_assignments.csv`: outer-fold assignment for all 594 samples
- `provenance/release_manifest_594_sha256.csv`: sample-level paths and SHA-256
- `RELEASE_FILE_CHECKSUMS_SHA256.csv`: checksum inventory for the release
- `RELEASE_METADATA.json`: release summary and version metadata
- `provenance/`: original V3 manifests, audit records, and validation reports

## Validation summary

- Final retained samples: 594
- NORMAL mappings: 287
- Automatically confirmed NORMAL mappings: 243
- Manually visually verified NORMAL mappings: 44
- Unresolved NORMAL mappings: 0
- Missing preprocessed paths: 0
- Missing ROI paths: 0
- Duplicate preprocessed assignments: 0
- Duplicate ROI assignments: 0
- Missing outer-fold assignments: 0
- Blocking failures: 0

## Immutability rule

Do not rename, replace, edit, add, or delete files inside this directory.

Any future correction, transformation, or experiment-specific derivative must
be created under a new version, for example:

`AMD_DATASET_594_PRODUCTION_v2`

The `sample_id` values and the original outer-fold assignments must remain
unchanged unless a formally documented correction requires a new release.
