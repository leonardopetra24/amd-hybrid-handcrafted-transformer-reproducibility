# Reproducibility scope

| Level | Scope | Status |
|---|---|---|
| A | Dataset registry, duplicate audit, provenance, immutable folds | Fully supported from included non-image metadata |
| B | Automatic preprocessing | Executable and deterministic |
| C | Assisted 224x224 ROI placement | Interface reproducible; exact historical coordinates unavailable |
| D | Handcrafted32 extraction | Exact recovered function; 594/594 equivalence previously verified |
| E | Frozen ViT feature extraction | Executable; exact timm pretrained configuration recorded |
| F | Nested Hybrid PCA-SVM evaluation | Executable notebook + complete prediction/grid registries |
| G | Source prediction / contribution / PCA / computational analyses | Audited reference outputs included; original source notebooks were not all retained |
| H | Same-condition partial/full ViT fine-tuning | Executable internal-comparison notebook included |
| I | RETFound baseline | Executable notebooks + internal/LODO features/predictions; upstream gated checkpoint not redistributed |
| J | HOG-CNN adapted baseline | Internal/LODO predictions and audits included; large feature caches are optional release assets; original training source was not retained in supplied artifacts |
| K | STARE v8 exploratory shift analysis | Self-contained executable notebook + lightweight final outputs included |

The package is designed to make the provenance and limitations explicit rather than imply a stronger level of replay than the historical records support.
