# Optional large GitHub Release assets

Do not commit the large HOG-CNN cache ZIP to normal Git history. The file is larger than the normal GitHub 100 MiB per-file limit. Upload it as a GitHub **Release asset** instead.

The repository includes `release_assets_manifest.csv` with exact SHA-256 hashes for the optional large assets. The full STARE v8 ZIP is also listed as an optional Release asset because its lightweight final outputs are already extracted into the repository.

The RETFound CFP checkpoint is **not** redistributed. It is a gated upstream model and must be obtained from `YukunZhou/RETFound_mae_natureCFP` after accepting the provider's access conditions. Exact code commit and observed checkpoint snapshot identifiers are recorded in `configs/pretrained_weights.json`.
