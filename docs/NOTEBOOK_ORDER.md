# Recommended notebook order

1. `00_portable_preprocessing_assisted_roi.ipynb` — optional preprocessing/assisted ROI demonstration.
2. `01_freeze_dataset_594.ipynb` — canonical dataset freeze/integrity logic.
3. `02_build_immutable_folds.ipynb` — Source x Class folds, nested assignments, and LODO assignments.
4. `03_nested_cv_multiseed.ipynb` — proposed/frozen-feature ablations with five-seed nested CV.
5. `04_transformer_same_condition_comparison.ipynb` — partial/full ViT fine-tuning on the same frozen ROIs.
6. `05_retfound_frozen_pca128_svm.ipynb` — RETFound feature extraction/evaluation.
7. `06_retfound_internal_validation_paired.ipynb` — RETFound audit/paired comparisons.
8. `07_stare_v8_exploratory_shift.ipynb` — corrected exploratory STARE v8 analysis.

The historical manual preprocessing notebook is retained under `notebooks/legacy/` for provenance only.
