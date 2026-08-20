from __future__ import annotations
from pathlib import Path
import numpy as np
import tifffile
from skimage.measure import regionprops
from linking import ObjectState


def load_states(mask_path: Path, image_path: Path, frame: int) -> list[ObjectState]:
    mask=tifffile.imread(mask_path)
    image=tifffile.imread(image_path)
    states=[]
    for r in regionprops(mask.astype(np.int32), intensity_image=image.astype(float)):
        y,x=r.centroid
        states.append(ObjectState(frame=frame,label=int(r.label),y=float(y),x=float(x),area=float(r.area),mean_intensity=float(r.mean_intensity)))
    return states


def discover_sequence(root: Path, seq: str):
    image_dir=root/seq
    err_dir=root/f"{seq}_ERR_SEG"
    if not image_dir.exists() or not err_dir.exists():
        raise FileNotFoundError(f"Expected {image_dir} and {err_dir}. Check CTC archive layout.")
    image_files=sorted(image_dir.glob("t*.tif"))
    mask_files=sorted(err_dir.glob("mask*.tif"))
    if not image_files or not mask_files:
        raise FileNotFoundError("No image/mask TIFF files discovered.")
    n=min(len(image_files),len(mask_files))
    return list(zip(image_files[:n],mask_files[:n]))
