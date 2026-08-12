from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
for rel in ['results/reference/stare_v8/table_1_stare_five_seed_summary.csv','results/reference/stare_v8/table_2_primary_seed42_metrics.csv','results/reference/stare_v8/table_3_consensus_metrics.csv']:
    p=ROOT/rel
    print('\n'+rel)
    print(pd.read_csv(p).to_string(index=False))
