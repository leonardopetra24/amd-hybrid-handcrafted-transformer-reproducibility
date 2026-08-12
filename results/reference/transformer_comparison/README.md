# Transformer same-condition comparison

The executable same-condition partial/full ViT fine-tuning source is provided in `notebooks/04_transformer_same_condition_comparison.ipynb`. The historical output directory itself was not included in the uploaded artifact set used to assemble this public package. Running the notebook on the frozen 594 ROI set regenerates checkpoint, epoch-history, sample-prediction, fold-metric, and summary artifacts.

Model identifier used by the notebook: `vit_base_patch16_224.augreg_in21k_ft_in1k`.

The manuscript's full-fine-tuning LODO analysis was generated in a separate experiment whose original executable source was not present in the supplied artifact set. The package therefore does not claim byte-identical end-to-end regeneration of that specific historical LODO full-fine-tuning run. Reported results remain auditable in the manuscript/handoff, but this limitation is disclosed here rather than hidden.
