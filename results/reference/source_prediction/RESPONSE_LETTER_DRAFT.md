# Draft response to Reviewer 2, Comment 1

**Response:** We thank the reviewer for identifying repository identity as a potential class proxy. We added a direct repository-identity diagnostic using the same immutable five outer folds. Repository identity was predicted using a fixed linear ridge probe from Handcrafted32, ViT768, Hybrid800, and Hybrid-PCA128. Standardization and PCA were fitted exclusively on each outer-training partition, and no synthetic oversampling was used.

A disease-label-only baseline quantified predictability caused solely by unequal source-by-class composition and achieved balanced accuracy 41.15%. Handcrafted32, ViT768, Hybrid800, and Hybrid-PCA128 achieved 86.02%, 84.22%, 85.49%, and 91.32%, respectively. We additionally repeated source prediction within NORMAL, AMD_DRY, and AMD_WET and performed class-conditional permutation testing.

Patient-level grouped cross-validation could not be performed because verifiable patient identifiers were not consistently available across the four repositories. We did not infer patient identity from filenames or eye laterality. This limitation is now stated explicitly.
