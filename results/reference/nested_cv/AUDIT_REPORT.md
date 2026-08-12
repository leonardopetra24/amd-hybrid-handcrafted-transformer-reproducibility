# Nested Cross-Validation and Multi-Seed Audit

## Purpose

This package addresses reviewer concerns about optimistic bias, incomplete
hyperparameter documentation, reliance on a single five-fold realization, and
lack of fold-level predictions.

## Design

- Five immutable outer folds from the frozen production release.
- Four-fold inner stratified cross-validation inside each outer-training set.
- Macro-F1 as the primary hyperparameter-selection criterion.
- Grid search over SVM C, gamma, class weighting, SMOTE neighbors, and PCA
  dimension where applicable.
- Five independent random seeds.
- Sample-level out-of-fold predictions for every scenario and seed.

## Leakage controls

- The outer validation fold is never used for hyperparameter selection.
- SMOTE is fitted inside the current training partition only.
- StandardScaler is fitted inside the current training partition only.
- PCA is fitted inside the current training partition only.
- Final outer-fold performance is evaluated once after configuration selection.

## Interpretation

The primary revised estimate should be based on the multi-seed nested-CV
summary rather than the earlier single-seed fixed-parameter result.
