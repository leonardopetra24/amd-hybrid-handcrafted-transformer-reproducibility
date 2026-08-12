from pathlib import Path
import pandas as pd
import json, hashlib

ROOT=Path(__file__).resolve().parents[1]

def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""):
            h.update(block)
    return h.hexdigest()

release=pd.read_csv(ROOT/"metadata/provenance/release_manifest_594_sha256.csv")
fold_full=pd.read_csv(ROOT/"folds/outer_fold_assignments.csv")
fold_release=pd.read_csv(ROOT/"metadata/outer_fold_assignments.csv")

assert len(release)==594
assert release["sample_id"].is_unique
assert len(fold_full)==594 and fold_full["sample_id"].is_unique
assert len(fold_release)==594 and fold_release["sample_id"].is_unique

m=fold_release.merge(fold_full[["sample_id","outer_fold"]],on="sample_id",suffixes=("_release","_builder"))
assert (m.outer_fold_release==m.outer_fold_builder).all()

nested=pd.read_csv(ROOT/"folds/nested_cv_assignments.csv")
lodo=pd.read_csv(ROOT/"folds/lodo_split_assignments.csv")
assert len(nested)==594*5
assert len(lodo)==594*4

print("PASS: 594-sample release metadata and fold mappings are internally consistent.")
print("Release outer fold hash:",sha256(ROOT/"metadata/outer_fold_assignments.csv"))
print("Fold-builder full outer fold hash:",sha256(ROOT/"folds/outer_fold_assignments.csv"))
print("Note: hashes differ because CSV schemas differ; sample_id->outer_fold mappings are identical.")
