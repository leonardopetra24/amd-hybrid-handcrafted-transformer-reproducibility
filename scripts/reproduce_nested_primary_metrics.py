from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, f1_score, balanced_accuracy_score

ROOT=Path(__file__).resolve().parents[1]
p=ROOT/"results/reference/nested_cv/nested_sample_level_predictions.csv"
df=pd.read_csv(p)

def col(*names):
    for n in names:
        if n in df.columns: return n
    raise KeyError(names)

seed=col("seed")
scenario=col("scenario","scenario_id","method")
yt=col("y_true","true_label","class_label")
yp=col("y_pred","predicted_label","prediction")

rows=[]
for (s,m),g in df.groupby([seed,scenario]):
    rows.append({
        "seed":s,"scenario":m,"n":len(g),
        "accuracy":accuracy_score(g[yt],g[yp]),
        "macro_f1":f1_score(g[yt],g[yp],average="macro"),
        "balanced_accuracy":balanced_accuracy_score(g[yt],g[yp])
    })
seed_metrics=pd.DataFrame(rows)
summary=seed_metrics.groupby("scenario")[["accuracy","macro_f1","balanced_accuracy"]].agg(["mean","std"])
print(summary)
