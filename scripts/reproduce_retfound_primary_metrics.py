from pathlib import Path
import pandas as pd, numpy as np
from sklearn.metrics import accuracy_score, f1_score, balanced_accuracy_score
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'results/reference/retfound/retfound_internal_sample_predictions.csv'
df=pd.read_csv(p)
rows=[]
for seed,g in df.groupby('seed'):
    rows.append({'seed':int(seed),'accuracy':accuracy_score(g.true_label,g.predicted_label),'macro_f1':f1_score(g.true_label,g.predicted_label,average='macro'),'balanced_accuracy':balanced_accuracy_score(g.true_label,g.predicted_label)})
out=pd.DataFrame(rows)
print(out.to_string(index=False))
for c in ['accuracy','macro_f1','balanced_accuracy']:
    print(c, out[c].mean(), out[c].std(ddof=1))
