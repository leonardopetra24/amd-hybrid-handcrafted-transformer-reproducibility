from __future__ import annotations
"""
Reconstructed executable wrapper for the legacy preprocessing logic in
`preprocessing_crop_manual_code.ipynb`.

This wrapper preserves the original algorithm while making paths/classes
parameter-driven. It is a clean-room organizational reconstruction of the
legacy notebook, not a claim that the historical code was originally stored
in this form.
"""
from pathlib import Path
import cv2
import numpy as np

IMG_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"}

def apply_clahe_bgr(img_bgr, clip_limit: float = 2.0, tile_grid=(8, 8)):
    lab = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2LAB)
    L, A, B = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid)
    L2 = clahe.apply(L)
    return cv2.cvtColor(cv2.merge([L2, A, B]), cv2.COLOR_LAB2BGR)

def apply_gamma(img_bgr, gamma: float = 1.1):
    # Exact legacy convention: LUT exponent = 1/gamma.
    if gamma <= 0:
        return img_bgr
    inv = 1.0 / gamma
    table = (np.arange(256) / 255.0) ** inv
    table = np.clip(table * 255.0, 0, 255).astype(np.uint8)
    return cv2.LUT(img_bgr, table)

def largest_circle_mask(img_bgr):
    hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    V = hsv[:, :, 2]
    V_blur = cv2.GaussianBlur(V, (5, 5), 0)
    _, th = cv2.threshold(V_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    if np.sum(th == 255) < 0.2 * th.size:
        th = cv2.bitwise_not(th)
    kernel = np.ones((7, 7), np.uint8)
    th = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel, iterations=2)
    th = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel, iterations=1)
    contours, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        h, w = th.shape
        r = int(min(h, w) * 0.48)
        cy, cx = h // 2, w // 2
        mask = np.zeros_like(th)
        cv2.circle(mask, (cx, cy), r, 255, -1)
        return mask, (cx, cy, r)
    cnt = max(contours, key=cv2.contourArea)
    (cx, cy), r = cv2.minEnclosingCircle(cnt)
    cx, cy, r = int(cx), int(cy), int(r)
    mask = np.zeros_like(th)
    cv2.circle(mask, (cx, cy), r, 255, -1)
    return mask, (cx, cy, r)

def crop_to_circle(img_bgr, mask, circle):
    h, w = mask.shape
    cx, cy, r = circle
    x1 = max(cx-r, 0); y1 = max(cy-r, 0)
    x2 = min(cx+r, w-1); y2 = min(cy+r, h-1)
    img_masked = cv2.bitwise_and(img_bgr, img_bgr, mask=mask)
    crop = img_masked[y1:y2, x1:x2]
    return img_masked if crop.size == 0 else crop

def process_image(path_in, path_out, gamma: float = 1.1, target_size=(512, 512)):
    img = cv2.imread(str(path_in))
    if img is None:
        raise ValueError(f"OpenCV could not read {path_in}")
    img = apply_clahe_bgr(img, clip_limit=2.0, tile_grid=(8, 8))
    img = apply_gamma(img, gamma=gamma)
    mask, circle = largest_circle_mask(img)
    crop = crop_to_circle(img, mask, circle)
    out = cv2.resize(crop, target_size, interpolation=cv2.INTER_AREA)
    path_out = Path(path_out)
    path_out.parent.mkdir(parents=True, exist_ok=True)
    if not cv2.imwrite(str(path_out), out):
        raise IOError(f"Failed to write {path_out}")
    return path_out

def process_tree(input_root, output_root, gamma=1.1, target_size=(512,512)):
    input_root, output_root = Path(input_root), Path(output_root)
    total = 0
    for p in sorted(input_root.rglob("*")):
        if not p.is_file() or p.suffix.lower() not in IMG_EXTS:
            continue
        rel = p.relative_to(input_root)
        process_image(p, output_root/rel, gamma=gamma, target_size=target_size)
        total += 1
    return total
