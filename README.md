# AMD Hybrid Handcrafted-Transformer Reproducibility Package

Reproducibility resources for **“A Hybrid Handcrafted-Transformer Framework for Efficient Multiclass AMD Classification”** (IJIES/INASS revision, Paper ID 20264410).

## Canonical study registry
- Dataset release: `AMD_DATASET_594_PRODUCTION_v1`
- 594 unique color fundus photographs
- Classes: 287 NORMAL, 139 AMD_DRY, 168 AMD_WET
- Sources: ADAM, FIVES, ODIR, RFMiD
- Robustness seeds: 42, 123, 2026, 3407, 7777
- Immutable outer folds: five Source x Class stratified folds
- Cross-repository evaluation: four leave-one-dataset-out holds

## Proposed representation
1. 224 x 224 assisted macula-centered frozen ROI.
2. Handcrafted32 = RGB moments 9D + uniform LBP 18D + Mahotas Haralick first five 5D.
3. Frozen ViT-B/16 768D representation. Runtime audit resolves the pretrained configuration to `timm/vit_base_patch16_224.augreg2_in21k_ft_in1k`.
4. Concatenate to 800D.
5. Training-partition-only scaling, SMOTE, PCA/model selection, and RBF-SVM classification.

## Important ROI provenance statement
The historical assisted crop was operator-guided. The final ROI files/identifiers and SHA-256 provenance were retained, but the historical per-image x/y crop-coordinate CSVs were not. **Exact pixel-level replay of the original manual ROI from raw images is not claimed.** Automatic preprocessing and the assisted-crop interface are executable, and all downstream proposed-method analyses are reproducible from the frozen-ROI stage when those ROIs are available. See `docs/DATA_AND_ROI_PROVENANCE.md`.

## What is included
- duplicate-controlled 594-sample metadata and provenance;
- immutable outer, nested-inner, and LODO split assignments;
- portable preprocessing, assisted ROI, Handcrafted32, and frozen-ViT modules;
- sanitized notebooks documenting nested CV, same-condition transformer comparison, RETFound, and corrected STARE v8; RETFound feature extraction additionally requires the gated checkpoint and a locally reconstructed ROI set;
- complete nested prediction/grid registries;
- source-prediction, feature-family, matched-control, PCA-sensitivity, and computational result registries;
- RETFound internal/LODO features, predictions, computational records, and audit;
- HOG-CNN internal/LODO predictions and validation audits;
- lightweight STARE v8 final outputs and the 594/594 handcrafted equivalence gate;
- exact pretrained-model identifiers;
- integrity and metric-regeneration scripts.

## What is not redistributed
- Original source fundus images.
- Historical per-image manual ROI coordinates (not retained).
- Gated RETFound CFP checkpoint (~3.68 GiB); exact upstream identifiers are provided.
- Large HOG-CNN feature caches in normal Git history; use the optional GitHub Release asset listed in `release_assets_manifest.csv`.

## Quick start
```bash
python -m venv .venv
# activate the environment, then:
pip install -r requirements.txt
python scripts/audit_integrity.py
python scripts/reproduce_nested_primary_metrics.py
python scripts/audit_public_package.py
```

See `docs/NOTEBOOK_ORDER.md` for the experiment order and `GITHUB_UPLOAD_GUIDE.md` for first-time GitHub publication instructions.

## Reproducibility boundary
The package is intentionally explicit about historical limitations. The proposed frozen-feature pipeline, dataset/fold provenance, predictions, and reported analyses are strongly auditable. Some historical comparator source artifacts were not retained (notably the original full-fine-tuning LODO runner and original HOG-CNN training source), so those specific comparator runs are not described as byte-identical end-to-end reproductions. Their audited predictions/metrics are included where available.

## Public release
Before making the repository public, verify third-party terms, decide whether to add an explicit code license, run the included audits, and replace `[PUBLIC_GITHUB_URL]` in the manuscript/response templates. Public files have been sanitized to remove author-specific absolute local paths; historical path fields are represented by `<LOCAL_PROJECT_ROOT>` where needed for provenance.
