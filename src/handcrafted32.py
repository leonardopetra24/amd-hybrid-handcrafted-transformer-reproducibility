from __future__ import annotations
from pathlib import Path
import cv2
import mahotas
import numpy as np
from scipy.stats import skew
from skimage.feature import local_binary_pattern

LBP_P=16
LBP_R=2

def extract_handcrafted_32d(image_path: str | Path) -> np.ndarray:
    """Exact production-equivalent 32D extractor verified against 594/594 cache."""
    img_bgr=cv2.imread(str(image_path))
    if img_bgr is None:
        raise ValueError(f"OpenCV could not read: {image_path}")
    img_rgb=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
    img_gray=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY)
    features=[]
    for channel_index in range(3):
        channel=img_rgb[:,:,channel_index]
        features.extend([float(np.mean(channel)),float(np.std(channel)),float(skew(channel.flatten()))])
    lbp=local_binary_pattern(img_gray,LBP_P,LBP_R,method="uniform")
    n_bins=LBP_P+2
    hist,_=np.histogram(lbp.ravel(),bins=n_bins,range=(0,n_bins),density=True)
    features.extend(hist.astype(float).tolist())
    har=mahotas.features.haralick(img_gray,distance=1).mean(axis=0)
    features.extend(har[:5].astype(float).tolist())
    arr=np.asarray(features,dtype=np.float32)
    if arr.shape!=(32,):
        raise ValueError(arr.shape)
    return np.nan_to_num(arr,nan=0.0,posinf=0.0,neginf=0.0)
