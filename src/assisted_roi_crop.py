from __future__ import annotations
"""
Generalized assisted 224x224 ROI GUI reconstructed from the legacy notebook.
The operator positions the fixed-size crop using X/Y trackbars and presses:
  c = accept crop, s = skip, ESC = stop.

The exact anatomical decision remains human-assisted. For deterministic replay
of historical ROI choices, use `replay_roi_coordinates.py` with archived
coordinates if those records are available.
"""
from pathlib import Path
import csv
import cv2

IMG_EXTS = {".jpg",".jpeg",".png",".bmp",".tif",".tiff"}

def crop_folder(input_folder, output_folder, csv_output, crop_size=(224,224)):
    input_folder, output_folder = Path(input_folder), Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)
    with open(csv_output, "w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["filename","x","y","w","h"])
        for img_path in sorted(input_folder.iterdir()):
            if not img_path.is_file() or img_path.suffix.lower() not in IMG_EXTS:
                continue
            image = cv2.imread(str(img_path))
            if image is None:
                continue
            clone = image.copy()
            h_img, w_img = image.shape[:2]
            cw, ch = crop_size
            if w_img < cw or h_img < ch:
                raise ValueError(f"Image smaller than crop: {img_path}")
            win_name = f"Move box for macula ROI: {img_path.name}"
            cv2.namedWindow(win_name)
            x0 = w_img//2-cw//2; y0 = h_img//2-ch//2
            cv2.createTrackbar("X", win_name, x0, w_img-cw, lambda v: None)
            cv2.createTrackbar("Y", win_name, y0, h_img-ch, lambda v: None)
            while True:
                x = cv2.getTrackbarPos("X", win_name)
                y = cv2.getTrackbarPos("Y", win_name)
                temp = clone.copy()
                cv2.rectangle(temp, (x,y), (x+cw,y+ch), (0,255,0), 2)
                cv2.imshow(win_name, temp)
                key = cv2.waitKey(1) & 0xFF
                if key == ord("c"):
                    crop = clone[y:y+ch, x:x+cw]
                    cv2.imwrite(str(output_folder/img_path.name), crop)
                    writer.writerow([img_path.name,x,y,cw,ch])
                    break
                if key == ord("s"):
                    break
                if key == 27:
                    cv2.destroyAllWindows()
                    return
            cv2.destroyAllWindows()
