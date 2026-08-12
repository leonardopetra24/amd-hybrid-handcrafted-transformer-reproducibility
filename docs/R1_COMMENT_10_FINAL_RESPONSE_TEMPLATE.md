# Reviewer 1 - Comment 10: final response template

**Response:** We thank the reviewer for emphasizing reproducibility. We have prepared a public reproducibility repository containing executable preprocessing and assisted ROI-cropping code, exact pretrained-model identifiers, the anonymized 594-image manifest, source identifiers, harmonized labels, duplicate-screening records, final ROI provenance and SHA-256 records, immutable image-level outer and inner fold assignments, random seeds, exact feature definitions, model configurations and search spaces, software dependencies, hardware specifications, sample-level predictions, statistical analyses, and scripts/notebooks for regenerating the reported analyses.

The original macula-centered ROIs were generated using an operator-assisted fixed 224 x 224 cropping interface guided by anatomical landmarks and were visually inspected. Historical per-image crop coordinates were not retained; therefore, the repository does not claim exact pixel-level replay of the original manual crop from raw photographs. Instead, final ROI identifiers and integrity hashes are provided, and the downstream proposed-method experiments are reproducible from the frozen-ROI stage onward. Original fundus photographs are not redistributed where restricted by source-repository licenses; source identifiers and acquisition information are provided instead. Third-party gated weights, including RETFound, are referenced by exact upstream identifiers rather than redistributed.

The repository is available at: **[PUBLIC_GITHUB_URL]**

**Location in revised manuscript:** Sections 3.2 and 3.10, Table 3, and the Code and Data Availability section.
