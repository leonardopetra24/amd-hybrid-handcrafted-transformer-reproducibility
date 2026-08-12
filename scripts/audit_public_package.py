from pathlib import Path
import hashlib, json, pandas as pd

ROOT=Path(__file__).resolve().parents[1]
issues=[]

def check(cond,msg):
    if not cond: issues.append(msg)

# Key files
required=[
 'README.md','configs/pretrained_weights.json','metadata/provenance/release_manifest_594_sha256.csv',
 'folds/outer_fold_assignments.csv','folds/nested_cv_assignments.csv','folds/lodo_split_assignments.csv',
 'results/reference/nested_cv/nested_sample_level_predictions.csv',
 'results/reference/retfound/retfound_internal_sample_predictions.csv',
 'results/reference/stare_v8/VALIDATION_REPORT.json',
]
for rel in required: check((ROOT/rel).exists(),f'missing: {rel}')

# Dataset counts
m=pd.read_csv(ROOT/'metadata/provenance/release_manifest_594_sha256.csv',dtype={'sample_id':str})
check(len(m)==594,'release manifest must have 594 rows')
check(m['sample_id'].nunique()==594,'release sample IDs must be unique')

# Fold consistency
f=pd.read_csv(ROOT/'folds/outer_fold_assignments.csv',dtype={'sample_id':str})
check(len(f)==594,'outer fold assignments must have 594 rows')
check(f['sample_id'].nunique()==594,'outer fold sample IDs must be unique')

# Nested predictions
n=pd.read_csv(ROOT/'results/reference/nested_cv/nested_sample_level_predictions.csv',dtype={'sample_id':str})
check(n['sample_id'].nunique()==594,'nested predictions must cover 594 unique samples')

# RETFound
r=pd.read_csv(ROOT/'results/reference/retfound/retfound_internal_sample_predictions.csv',dtype={'sample_id':str})
check(len(r)==2970,'RETFound internal predictions expected 2970 rows')
check(r['sample_id'].nunique()==594,'RETFound must cover 594 samples')

# STARE validation
s=json.load(open(ROOT/'results/reference/stare_v8/VALIDATION_REPORT.json',encoding='utf-8'))
check(bool(s.get('complete_and_valid')),'STARE validation report not valid')
check(bool(s.get('handcrafted_equivalence_passed')),'STARE handcrafted equivalence gate did not pass')

# No normal Git file over 25 MiB in prepared public repository
oversized=[]
for p in ROOT.rglob('*'):
    if p.is_file() and p.stat().st_size>25*1024*1024:
        oversized.append((str(p.relative_to(ROOT)),p.stat().st_size))
check(not oversized,f'files over 25 MiB found: {oversized}')

report={'status':'PASS' if not issues else 'FAIL','issues':issues,'manifest_rows':len(m),'nested_prediction_rows':len(n),'retfound_rows':len(r),'oversized_files':oversized}
print(json.dumps(report,indent=2))
if issues: raise SystemExit(1)
