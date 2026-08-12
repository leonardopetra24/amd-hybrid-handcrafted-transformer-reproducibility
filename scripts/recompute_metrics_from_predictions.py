from __future__ import annotations
import argparse
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, balanced_accuracy_score

def find_col(df,candidates):
    for c in candidates:
        if c in df.columns: return c
    raise KeyError(f"None of {candidates} found; columns={list(df.columns)}")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--group",nargs="*",default=[])
    args=ap.parse_args()
    df=pd.read_csv(args.csv)
    y=find_col(df,["y_true","true_label","class_label","true_class"])
    p=find_col(df,["y_pred","predicted_label","pred_label","prediction"])
    groups=args.group
    if not groups:
        groups=[None]
    out=[]
    if groups==[None]:
        iterable=[("ALL",df)]
    else:
        iterable=df.groupby(groups,dropna=False)
    for key,g in iterable:
        out.append({
            "group":str(key),
            "n":len(g),
            "accuracy":accuracy_score(g[y],g[p]),
            "macro_f1":f1_score(g[y],g[p],average="macro"),
            "balanced_accuracy":balanced_accuracy_score(g[y],g[p]),
        })
    print(pd.DataFrame(out).to_string(index=False))
if __name__=="__main__": main()
