# R2.7 Interpretation Rules

## What this experiment can establish

- whether exact Handcrafted32 performs differently from ViT-PCA128 when all
  compared outputs are fixed at 128 dimensions;
- whether exact Handcrafted32 exceeds deterministic Random32 and the predefined
  Generic32 histogram control;
- whether held-out performance changes after grouped permutation of Color,
  LBP, Haralick, all handcrafted features, or ViT;
- whether handcrafted families receive more or less PCA loading share than
  expected from their dimension counts;
- which standardized coefficients appear in a linear surrogate.

## What this experiment cannot establish

- clinical lesion causality;
- ophthalmologist-confirmed relevance;
- direct RBF-SVM input coefficients;
- universal superiority of handcrafted fusion;
- preregistered confirmatory evidence.

## Required wording

Use:
- reviewer-requested post hoc diagnostic;
- matched PCA-128 control;
- grouped permutation importance;
- variance-weighted PCA loading share;
- standardized linear-SVM surrogate.

Do not use:
- standardized coefficients of the RBF-SVM;
- clinically proven feature importance;
- PCA proves discriminative importance;
- random control proves lesion specificity by itself.
