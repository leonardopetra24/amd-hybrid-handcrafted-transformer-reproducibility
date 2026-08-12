from __future__ import annotations
from pathlib import Path
import numpy as np
import torch
import timm
from PIL import Image
from torchvision import transforms as T

MODEL_ID="vit_base_patch16_224"
INPUT_SIZE=224

def create_frozen_vit(device=None):
    device=device or torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model=timm.create_model(MODEL_ID,pretrained=True,num_classes=0).to(device).eval()
    cfg=dict(getattr(model,"pretrained_cfg",{}) or {})
    return model,device,cfg

def transform():
    return T.Compose([
        T.Resize((224,224)),
        T.ToTensor(),
        T.Normalize(mean=(0.5,0.5,0.5),std=(0.5,0.5,0.5)),
    ])

def extract(paths,batch_size=16,device=None):
    model,device,cfg=create_frozen_vit(device)
    tfm=transform()
    parts=[]
    with torch.no_grad():
        for start in range(0,len(paths),batch_size):
            batch=[]
            for p in paths[start:start+batch_size]:
                with Image.open(p) as im:
                    batch.append(tfm(im.convert("RGB")))
            x=torch.stack(batch).to(device)
            parts.append(model(x).detach().cpu().numpy().astype(np.float32))
    feat=np.vstack(parts)
    if feat.shape[1]!=768:
        raise ValueError(feat.shape)
    return feat,cfg
