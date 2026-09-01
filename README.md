# AMD Hybrid Handcrafted-Transformer Reproducibility Package

Reproducibility resources for:

**“A Hybrid Handcrafted-Transformer Framework for Multiclass AMD Classification with Efficient Downstream Recalibration”**

IJIES/INASS revision — **Paper ID 20264410**

---

## Canonical Study Registry

- Dataset release: `AMD_DATASET_594_PRODUCTION_v1`
- Total images: **594 unique color fundus photographs**
- Classes:
  - **287 NORMAL**
  - **139 AMD_DRY**
  - **168 AMD_WET**
- Source repositories:
  - ADAM
  - FIVES
  - ODIR
  - RFMiD
- Robustness seeds:
  - `42`
  - `123`
  - `2026`
  - `3407`
  - `7777`
- Immutable outer validation:
  - five **Source × Class stratified** folds
- Cross-repository evaluation:
  - four leave-one-dataset-out (**LODO**) holds

---

## Proposed Representation

The proposed framework uses the following pipeline:

1. **224 × 224 assisted macula-centered frozen ROI**
2. **Handcrafted32**
   - RGB color moments: 9D
   - uniform LBP: 18D
   - Mahotas Haralick first five descriptors: 5D
3. **Frozen ViT-B/16 representation**
   - 768-dimensional pre-head embedding
   - pretrained configuration:
     `timm/vit_base_patch16_224.augreg2_in21k_ft_in1k`
4. **Feature fusion**
   - Handcrafted32 + ViT768
   - total: **800 dimensions**
5. **Training-partition-only downstream processing**
   - `SMOTE → StandardScaler → optional PCA → RBF-SVM`

All training-dependent operations are fitted exclusively within the corresponding training partition. Outer-test samples are not used for preprocessing estimation, hyperparameter selection, or model fitting.

---

## Important ROI Provenance Statement
The historical macula-centered ROI placement was operator-assisted and guided by anatomical landmarks.
The final ROI identifiers and SHA-256 integrity records were retained. However, the historical per-image x/y crop-coordinate records used to create the original frozen ROI set were not retained.
Therefore:

**Exact pixel-level replay of the original raw-image-to-ROI placement is not claimed.**
Executable preprocessing and assisted-cropping utilities are included. Given access to the referenced frozen ROIs, the released resources support reproduction of the core frozen-feature pipeline and downstream analyses.

See:

`docs/DATA_AND_ROI_PROVENANCE.md`

for additional provenance information.

---

## What Is Included
The public reproducibility package includes:
- duplicate-controlled metadata for the final 594-image release;
- de-identified sample identifiers;
- repository-source identifiers;
- harmonized disease labels;
- duplicate-screening and provenance records;
- final ROI identifiers and SHA-256 integrity records;
- immutable outer-fold assignments;
- nested inner-fold assignments;
- LODO split assignments;
- five robustness seeds;
- executable preprocessing utilities;
- assisted ROI-cropping utilities;
- exact Handcrafted32 feature-extraction code;
- frozen ViT feature-extraction code;
- exact pretrained-model and checkpoint identifiers;
- locked configurations and hyperparameter search spaces;
- SMOTE, StandardScaler, PCA, and SVM configurations;
- software dependency specifications;
- hardware specifications;
- nested prediction and model-selection registries;
- source-prediction outputs;
- class-conditioned source-prediction outputs;
- matched handcrafted-contribution controls;
- feature-family ablation outputs;
- grouped-permutation outputs;
- PCA-loading diagnostics;
- PCA-sensitivity outputs;
- computational benchmark records;
- RETFound internal and LODO features, predictions, and audit records;
- HOG-CNN internal and LODO predictions and validation audits;
- corrected STARE dataset-shift outputs;
- statistical-analysis outputs;
- metric-regeneration scripts;
- integrity-audit scripts.

Sanitized notebooks document the nested cross-validation workflow, matched transformer comparisons, RETFound evaluation, contribution analyses, computational assessment, and corrected STARE dataset-shift analysis.

RETFound feature extraction requires the corresponding third-party checkpoint and locally reconstructed eligible ROI inputs.

---

## Supplementary Material

### Supplementary Table S1

[Supplementary Table S1](docs/Supplementary_Table_S1.md)

Supplementary Table S1 consolidates the detailed handcrafted-feature contribution diagnostics reported in the manuscript, including:

- LODO feature-family ablation results;
- grouped-permutation importance;
- PCA dimensional and loading shares; and
- LinearSVC surrogate coefficient-share diagnostics.

The supplementary material provides supporting detail for the contribution analyses summarized in Section 4.5 of the manuscript.

---

## What Is Not Redistributed

The following items are not redistributed through this repository:

- original source fundus photographs from ADAM, FIVES, ODIR, and RFMiD;
- historical per-image assisted ROI coordinates, because they were not retained;
- third-party gated or license-restricted pretrained checkpoints;
- the gated RETFound CFP checkpoint;
- large HOG-CNN feature caches in the normal Git history.

Where redistribution is restricted, the repository provides dataset identifiers, provenance records, acquisition references, and exact upstream model/checkpoint identifiers where available.

Large optional artifacts may be distributed separately through GitHub Release assets when permitted. See:

`release_assets_manifest.csv`

for the corresponding asset registry.

---

## Quick Start
Create and activate a Python virtual environment, then install the documented dependencies:

```bash
python -m venv .venv

# activate the environment, then:
pip install -r requirements.txt
python scripts/audit_integrity.py
python scripts/reproduce_nested_primary_metrics.py
python scripts/audit_public_package.py
```

See docs/NOTEBOOK_ORDER.md for the recommended experiment and notebook order.
---

## Computational Benchmark Scope
The synchronized computational benchmark uses a common boundary beginning from the frozen ROI.

The benchmark separately accounts for:

- cold-start model construction;
- one-time reusable feature generation;
- cached downstream fitting;
- complete multi-run time;
- direct ROI-to-prediction latency;
- batch throughput;
- memory use;
- storage requirements; and
- sampled-GPU-power-based energy estimates.

The principal engineering claim of the proposed framework is rapid downstream recalibration after reusable feature generation, not fastest direct online inference.

Energy values are sampled-GPU-power estimates and should not be interpreted as calibrated whole-system electricity measurements.

---

## Dataset-Shift Evaluation
STARE is used only as an exploratory rule-harmonized dataset-shift evaluation.

The final STARE evaluation set contains:
- 18 AMD_DRY images;
- 53 AMD_WET images; and
- 29 NORMAL images.

STARE labels were harmonized from diagnostic codes and text and were not established through blinded image-level regrading, adjudication, or inter-grader agreement.
The STARE experiment is therefore not presented as clinical external validation.

---

## Reproducibility Boundary
The package is intentionally explicit about historical reproducibility limitations. 

Given access to the referenced frozen ROIs, the released resources support reproduction of the core frozen-feature pipeline and downstream analyses.

Two comparator-specific exceptions apply: the original full-fine-tuning LODO runner and the HOG-CNN training source used for the reported comparator runs were not retained. For these two arms, archived predictions, metrics, configurations, fold assignments, and analysis outputs are provided instead of the original end-to-end training source.

Accordingly, complete byte-identical retraining of those historical comparator runs from their original training source is not claimed.

These limitations do not affect the availability of the archived comparator predictions, reported metrics, fold assignments, or analysis outputs provided in the package.

---

## Public Release
This repository is publicly available as the reproducibility package accompanying the IJIES revision.
Original source fundus images and third-party restricted checkpoints are not redistributed because repository licensing and access conditions differ.
The public repository is available at:
https://github.com/leonardopetra24/amd-hybrid-handcrafted-transformer-reproducibility

---

## Manuscript Scope

The accompanying study is a retrospective representation and engineering evaluation.

The proposed Hybrid framework is not claimed to:

- outperform full ViT fine-tuning predictively;
- provide the fastest direct online inference;
- constitute a clinically validated screening system;
- establish patient-level clinical benefit; or
- eliminate cross-repository dataset shift.

Its principal engineering contribution is a compact reusable frozen representation that enables rapid downstream PCA-SVM recalibration after one-time feature generation.

---

## Citation

When referring to this reproducibility package, please use the final manuscript title:

**A Hybrid Handcrafted-Transformer Framework for Multiclass AMD Classification with Efficient Downstream Recalibration**

Paper ID: **20264410**

International Journal of Intelligent Engineering and Systems (IJIES) / INASS revision.

---
