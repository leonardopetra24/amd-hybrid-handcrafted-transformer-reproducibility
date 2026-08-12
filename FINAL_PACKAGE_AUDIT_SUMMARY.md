# Final package audit summary

**Status: READY FOR PRIVATE GITHUB UPLOAD**

The assembled public-repository folder passed the integrity and size audits. It contains no normal Git file larger than 25 MiB.

- Canonical dataset: 594 unique samples (287 NORMAL, 139 AMD_DRY, 168 AMD_WET).
- Nested prediction registry: 14,850 rows.
- RETFound internal prediction registry: 2,970 rows.
- STARE v8 validation report: complete and valid.
- Handcrafted32 equivalence gate: passed for 594/594 canonical samples.
- Resolved proposed frozen ViT identifier: `timm/vit_base_patch16_224.augreg2_in21k_ft_in1k`.
- Historical ROI coordinates: not retained; exact pixel-level replay of the historical manual crop is not claimed.

## Remaining actions before PUBLIC visibility
1. Authors select a code license.
2. Upload repository as Private and inspect the GitHub-rendered content.
3. Optionally upload the large HOG-CNN package as a GitHub Release asset.
4. Change visibility to Public.
5. Insert the public repository URL into the manuscript and Reviewer 1 Comment 10 response.

## Disclosed historical comparator limitations
The source artifact set did not contain the original full-fine-tuning LODO runner or the original HOG-CNN training source. This does not affect the executable proposed frozen-feature pipeline, metadata/folds, or included audited prediction registries, but those two comparator runs are not represented as byte-identical end-to-end source reproductions.
