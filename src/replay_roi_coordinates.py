from pathlib import Path
import pandas as pd
import cv2

def replay_coordinates(preprocessed_root, coordinates_csv, output_root):
    preprocessed_root = Path(preprocessed_root)
    output_root = Path(output_root)
    output_root.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(coordinates_csv)
    required = {"filename","x","y","w","h"}
    cols = {c.lower():c for c in df.columns}
    if not required.issubset(cols):
        raise ValueError(f"Coordinate CSV must include {sorted(required)}; found {list(df.columns)}")
    for _, row in df.iterrows():
        fn = str(row[cols["filename"]])
        img = cv2.imread(str(preprocessed_root/fn))
        if img is None:
            raise ValueError(f"Missing image: {fn}")
        x=int(row[cols["x"]]); y=int(row[cols["y"]])
        w=int(row[cols["w"]]); h=int(row[cols["h"]])
        crop=img[y:y+h,x:x+w]
        if crop.shape[:2] != (h,w):
            raise ValueError(f"Crop out of bounds: {fn}")
        cv2.imwrite(str(output_root/fn), crop)
