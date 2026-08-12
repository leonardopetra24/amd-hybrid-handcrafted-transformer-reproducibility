from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
for rel in [
    'results/reference/hogcnn_internal/hogcnn_internal_seed_level_pooled_metrics.csv',
    'results/reference/hogcnn/hogcnn_lodo_seed_level_pooled_metrics.csv',
]:
    p=ROOT/rel
    print('\n'+rel)
    if not p.exists():
        print('missing')
        continue
    df=pd.read_csv(p)
    print(df.to_string(index=False))
    numeric=[c for c in df.columns if c.lower() in {'accuracy','macro_f1','balanced_accuracy','pooled_accuracy','pooled_macro_f1','pooled_balanced_accuracy'}]
    for c in numeric:
        print(f'{c}: mean={df[c].mean():.6f}, sample_sd={df[c].std(ddof=1):.6f}')
