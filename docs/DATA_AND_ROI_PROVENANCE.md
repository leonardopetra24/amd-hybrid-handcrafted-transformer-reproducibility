# Data and ROI provenance

## Final dataset
The canonical release contains 594 unique color fundus photographs: 287 NORMAL, 139 AMD_DRY, and 168 AMD_WET, drawn from ADAM, FIVES, ODIR, and RFMiD. Exact-duplicate screening was completed before immutable fold construction.

## Image redistribution
Original fundus images are not redistributed in this repository because source-dataset licenses differ. `metadata/provenance/release_manifest_594_sha256.csv` provides sample identifiers, source labels, class labels, paths used during the historical run, and SHA-256 records for raw, preprocessed, and frozen ROI stages. Users should acquire source images from their original repositories.

## Assisted ROI limitation
The 224x224 macula-centered ROIs were historically selected using an operator-assisted OpenCV interface guided by anatomical landmarks and then visually checked. Historical per-image x/y crop-coordinate CSV files were not retained. Therefore this repository **does not claim exact pixel-level replay of the original manual crop from raw photographs**.

What is preserved instead:
- executable automatic preprocessing and assisted-crop interface;
- fixed ROI size and protocol;
- final ROI identifiers and SHA-256 provenance records;
- exact downstream feature definitions;
- immutable folds, predictions, metrics, and analysis artifacts.

All reported downstream machine-learning analyses are reproducible from the frozen-ROI stage when the corresponding frozen ROIs are available.
