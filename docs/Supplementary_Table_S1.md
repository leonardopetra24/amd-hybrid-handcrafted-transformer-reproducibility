# Supplementary Table S1

## Consolidated diagnostics of handcrafted-feature contribution

This supplementary table consolidates the detailed diagnostic analyses used to assess whether the Handcrafted32 branch contributes information beyond the frozen ViT representation. The analyses include feature-family ablation under leave-one-dataset-out evaluation, grouped permutation importance, PCA loading-share analysis, and a standardized LinearSVC surrogate.

The results should be interpreted as supporting diagnostics rather than as independent evidence of causal or clinically specific feature importance.

---

### Table S1a. Feature-family contribution under leave-one-dataset-out evaluation

| Feature-family diagnostic | Accuracy change (percentage points) | Macro-F1 change (percentage points) | Additional observation |
|---|---:|---:|---|
| Color9 unique contribution | +1.45 | +1.25 | Positive accuracy effect in 5/5 seeds |
| LBP18 added to Frozen ViT | +1.41 | +1.45 | Standalone complementarity relative to Frozen ViT |
| LBP18 unique contribution after other handcrafted families | +0.27 | — | Limited unique incremental accuracy after other handcrafted families were present |
| Haralick5 removal | +0.61 | +0.50 | Small numerical gain after removal; does not establish that Haralick features are universally harmful |

**Difference definition for Haralick5 removal.** Values are the five-seed mean of seed-level pooled LODO metrics for the model without Haralick minus the corresponding full-model metrics. Positive values indicate improved performance after removal.

**Interpretation.** Color moments showed the clearest unique numerical contribution. LBP produced a larger gain when added directly to the frozen ViT representation, but its unique contribution became substantially smaller after the other handcrafted families were present. Removing Haralick produced small numerical gains of 0.61 percentage points in accuracy and 0.50 percentage points in macro-F1. These gains do not establish that Haralick descriptors are universally harmful.

---

### Table S1b. Grouped permutation importance

| Permuted feature group | Macro-F1 decrease (percentage points), mean ± SD | Positive decreases | Interpretation |
|---|---:|---:|---|
| Color9 | 0.25 ± 0.46 | 17/25 | Small contribution |
| LBP18 | 0.55 ± 0.98 | 18/25 | Largest disruption among handcrafted families |
| Haralick5 | 0.13 ± 0.33 | 13/25 | Limited contribution |
| All Handcrafted32 | 0.80 ± 0.81 | 23/25 | Detectable aggregate handcrafted contribution |
| ViT768 | 57.11 ± 3.65 | 25/25 | Dominant discriminative contribution |

**Interpretation.** Permuting all handcrafted features reduced macro-F1 by 0.80 percentage point on average, whereas permutation of the ViT representation caused a substantially larger decrease. These results are consistent with the frozen ViT representation carrying the dominant share of predictive information.

---

### Table S1c. PCA dimensional share and loading share

| Representation / feature family | Dimensional share (%) | PCA loading share (%) |
|---|---:|---:|
| Color9 | 1.125 | 1.136 |
| LBP18 | 2.250 | 2.371 |
| Haralick5 | 0.625 | 0.631 |
| All Handcrafted32 | 4.000 | 4.138 |
| ViT768 | 96.000 | 95.862 |

**Interpretation.** The complete Handcrafted32 block represented 4.000% of the original 800-dimensional fused representation and accounted for 4.138% of the PCA loading share. The ViT representation accounted for 96.000% of the original dimensions and 95.862% of the loading share. Thus, PCA did not disproportionately amplify the handcrafted component.

---

### Table S1d. Standardized LinearSVC surrogate coefficient share

| Disease class | Handcrafted32 coefficient share (%) |
|---|---:|
| AMD_DRY | 4.04 |
| AMD_WET | 2.99 |
| NORMAL | 4.12 |

**Interpretation.** Across the three disease classes, the Handcrafted32 block accounted for approximately 2.99%-4.12% of the absolute L1 coefficient mass in the standardized LinearSVC surrogate. Because the primary classifier is a nonlinear RBF-SVM, these coefficients are reported only as a supplementary linear diagnostic and should not be interpreted as coefficients of the final classifier.

---

## Overall interpretation

Across the complementary diagnostic analyses, the Handcrafted32 branch showed a small and feature-family-dependent contribution. Color moments provided the clearest unique numerical benefit, while LBP produced the largest handcrafted-family permutation disruption. However, the aggregate handcrafted contribution remained modest relative to the ViT representation.

These results are consistent with the conclusion reported in the manuscript that the handcrafted block contributes detectable information but is not uniquely distinguishable from dimensionality-matched or generic-statistic controls and does not dominate the fused representation.

---

## Relationship to the main manuscript

The summarized interpretation is reported in Section 4.5, "Evidence for and limits of handcrafted contribution," and the matched-dimensionality controls are reported in Table 9 of the main manuscript.

The present supplementary table provides the detailed family-ablation, grouped-permutation, PCA-loading, and linear-surrogate diagnostics referenced from Section 4.5.