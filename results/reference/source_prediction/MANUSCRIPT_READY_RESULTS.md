# Manuscript-ready source-prediction diagnostic

## Methods
To assess whether the learned representations retained repository-specific information, repository identity (ADAM, FIVES, ODIR, or RFMID) was predicted using the immutable five outer folds. A fixed linear ridge probe was fitted after training-only standardization. Hybrid-PCA128 additionally fitted PCA within each outer-training partition. No synthetic oversampling was used. A disease-label-only probe quantified source predictability attributable solely to unequal class composition. Additional probes were trained separately within NORMAL, AMD_DRY, and AMD_WET, and a class-conditional permutation test shuffled source labels only within disease strata.

## Results
Repository identity was predictable from disease labels alone (balanced accuracy 41.15%), confirming a non-trivial source-composition baseline. Balanced accuracies from Handcrafted32, ViT768, Hybrid800, and Hybrid-PCA128 were 86.02%, 84.22%, 85.49%, and 91.32%, respectively.

## Conditional-permutation results
- HANDCRAFTED32: observed BA 86.02%; conditional-null mean 33.56%; Holm-adjusted p = 0.0199005.
- VIT768: observed BA 84.22%; conditional-null mean 26.81%; Holm-adjusted p = 0.0199005.
- HYBRID800: observed BA 85.49%; conditional-null mean 26.89%; Holm-adjusted p = 0.0199005.
- HYBRID_PCA128: observed BA 91.32%; conditional-null mean 31.82%; Holm-adjusted p = 0.0199005.

## Interpretation constraint
High repository-identity accuracy demonstrates decodable source information, but does not prove that the AMD classifier relied exclusively on source identity. Interpret this diagnostic jointly with LODO disease classification and source-specific error analyses.
