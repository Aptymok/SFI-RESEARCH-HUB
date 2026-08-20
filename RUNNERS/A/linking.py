from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from scipy.optimize import linear_sum_assignment

@dataclass(frozen=True)
class ObjectState:
    frame: int
    label: int
    y: float
    x: float
    area: float
    mean_intensity: float


def _scale(values: list[float], floor: float = 1e-6) -> float:
    if not values:
        return 1.0
    s = float(np.median(np.abs(values)))
    return max(s, floor)


def _pair_cost(prev: ObjectState, cur: ObjectState, spatial_scale: float, area_scale: float) -> float:
    d = math.hypot(cur.x - prev.x, cur.y - prev.y) / spatial_scale
    a = abs(cur.area - prev.area) / area_scale
    return d + 0.35 * a


def instantaneous_links(previous: list[ObjectState], current: list[ObjectState]) -> list[tuple[int, int, float]]:
    """One-to-one nearest state matching using only t-1 and t."""
    if not previous or not current:
        return []
    spatial = _scale([math.hypot(a.x-b.x, a.y-b.y) for a in previous for b in current])
    area = _scale([o.area for o in previous] + [o.area for o in current])
    cost = np.array([[_pair_cost(p,c,spatial,area) for c in current] for p in previous], dtype=float)
    rows, cols = linear_sum_assignment(cost)
    return [(previous[r].label, current[c].label, float(cost[r,c])) for r,c in zip(rows,cols)]


def persistence_links(history2: list[ObjectState], previous: list[ObjectState], current: list[ObjectState], prior_links: dict[int,int]) -> list[tuple[int, int, float]]:
    """History-aware linker. Uses t-2 -> t-1 velocity where a prior identity link exists."""
    if not previous or not current:
        return []
    hist_by_label = {o.label:o for o in history2}
    spatial = _scale([math.hypot(a.x-b.x, a.y-b.y) for a in previous for b in current])
    area = _scale([o.area for o in previous] + [o.area for o in current])
    matrix=[]
    for p in previous:
        ancestor_label = next((k for k,v in prior_links.items() if v==p.label), None)
        h = hist_by_label.get(ancestor_label) if ancestor_label is not None else None
        row=[]
        for c in current:
            base=_pair_cost(p,c,spatial,area)
            if h is not None:
                pred_x = p.x + (p.x-h.x)
                pred_y = p.y + (p.y-h.y)
                motion = math.hypot(c.x-pred_x,c.y-pred_y)/spatial
                persistence = abs((p.area-h.area) - (c.area-p.area))/area
                base = 0.45*base + 0.45*motion + 0.10*persistence
            row.append(base)
        matrix.append(row)
    cost=np.array(matrix,dtype=float)
    rows,cols=linear_sum_assignment(cost)
    return [(previous[r].label,current[c].label,float(cost[r,c])) for r,c in zip(rows,cols)]
