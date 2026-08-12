# Public release status

**Status:** PRIVATE GitHub upload completed; final public-release preflight required.

The repository has been assembled from the supplied canonical metadata, folds, nested-CV artifacts, RETFound files, final STARE v8 package, transformer comparison notebook, HOG-CNN audits/predictions, source-prediction diagnostics, contribution analyses, PCA sensitivity, and computational benchmark.

Before changing visibility to PUBLIC:
1. Run the three audit commands in `GITHUB_UPLOAD_GUIDE.md`.
2. Decide whether to add an explicit code license; no license is asserted by the packaging step.
3. Verify the repository contains no source fundus images or credentials.
4. Optionally upload the large HOG-CNN ZIP as a GitHub Release asset.
5. Insert the final public URL into the manuscript and Reviewer 1 Comment 10 response.

Known non-blocking historical limitation: manual ROI coordinate CSVs were not retained. Exact raw-image-to-historical-ROI replay is therefore not claimed.


Privacy cleanup: author-specific absolute local paths were removed/replaced by `<LOCAL_PROJECT_ROOT>` before public release.
