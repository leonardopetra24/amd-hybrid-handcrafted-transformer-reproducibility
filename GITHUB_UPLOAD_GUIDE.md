# GitHub upload guide for a first-time user

## 1. Create a GitHub account
1. Open GitHub in a browser and choose **Sign up**.
2. Register a professional username and verify your email.
3. Enable two-factor authentication.

## 2. Install GitHub Desktop
Download and install GitHub Desktop, then sign in with the new account. This avoids command-line Git for the initial publication.

## 3. Unzip this package
Unzip `AMD_HYBRID_REPRODUCIBILITY_GITHUB_READY_v1.zip`. The unzipped folder itself will become the repository root. Do not nest the repository inside another copy of the same folder.

## 4. Add the local folder to GitHub Desktop
In GitHub Desktop: **File > Add local repository > Choose** and select the unzipped folder. If prompted, create/initialize a Git repository there.

## 5. First commit
Review the file list, use a message such as `Initial reproducibility package`, and commit to the default branch.

## 6. Publish as PRIVATE first
Choose **Publish repository**. Recommended repository name:
`amd-hybrid-handcrafted-transformer-reproducibility`

Recommended description:
`Reproducibility package for A Hybrid Handcrafted-Transformer Framework for Efficient Multiclass AMD Classification (IJIES Paper ID 20264410).`

Keep the repository **Private** during the first audit.

## 7. Audit online
Confirm that README renders correctly, no raw fundus images are present, no tokens/passwords are present, notebooks do not show personal local-path outputs, and no file is unexpectedly large.

Run locally from the repository root:
```bash
python scripts/audit_integrity.py
python scripts/reproduce_nested_primary_metrics.py
python scripts/audit_public_package.py
```

## 8. Optional large files
Create a GitHub Release and upload `hogcnn_pytorch_internal.zip` as a Release asset if you want to distribute the large HOG-CNN feature caches. Use `release_assets_manifest.csv` to verify SHA-256. Do not add this 100+ MiB ZIP to normal Git history.

## 9. Select a code license
The package intentionally does not choose a new code license on the authors' behalf. Review `LICENSE_SELECTION_REQUIRED.md`, choose an appropriate license for original code, and verify compatibility with third-party resources before public release.

## 10. Make the repository PUBLIC
After the audit and license review, change repository visibility from Private to Public. Copy the final public URL.

## 11. Update the manuscript and response letter
Replace `[PUBLIC_GITHUB_URL]` in the supplied templates with the actual public URL and change Reviewer 1 Comment 10 status to **Addressed**.
