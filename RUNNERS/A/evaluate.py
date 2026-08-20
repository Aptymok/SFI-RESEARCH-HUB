from __future__ import annotations
from pathlib import Path
import numpy as np
import tifffile


def majority_gt_id(pred_mask: np.ndarray, gt_mask: np.ndarray, pred_label: int) -> int | None:
    pixels=gt_mask[pred_mask==pred_label]
    pixels=pixels[pixels>0]
    if pixels.size==0:
        return None
    ids,counts=np.unique(pixels,return_counts=True)
    return int(ids[np.argmax(counts)])


def evaluate_links(err_prev: Path, err_cur: Path, gt_prev: Path, gt_cur: Path, links: list[tuple[int,int,float]]) -> dict:
    """GT is loaded only here, after link predictions exist.
    A predicted one-to-one continuation is counted correct when both imperfect segments map by majority overlap to the same GT track id.
    Division events are retained separately and are not treated as ordinary continuation wins.
    """
    ep=tifffile.imread(err_prev); ec=tifffile.imread(err_cur)
    gp=tifffile.imread(gt_prev); gc=tifffile.imread(gt_cur)
    correct=0; evaluable=0; unmapped=0
    for p,c,_ in links:
        pgt=majority_gt_id(ep,gp,p); cgt=majority_gt_id(ec,gc,c)
        if pgt is None or cgt is None:
            unmapped+=1; continue
        evaluable+=1
        if pgt==cgt:
            correct+=1
    return {
        "links":len(links),
        "evaluable":evaluable,
        "correct":correct,
        "accuracy":correct/evaluable if evaluable else None,
        "unmapped":unmapped,
    }


def discover_gt(root: Path, seq: str):
    gt_dir=root/f"{seq}_GT"/"TRA"
    if not gt_dir.exists():
        raise FileNotFoundError(f"Gold tracking directory not found: {gt_dir}")
    files=sorted(gt_dir.glob("man_track*.tif"))
    if not files:
        raise FileNotFoundError(f"No gold tracking masks found under {gt_dir}")
    return files
