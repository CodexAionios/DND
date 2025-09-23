from __future__ import annotations
from dataclasses import dataclass
import math

@dataclass
class RSUWeights:
    w_lux: float = 0.25         # luminance contribution
    w_fix: float = 0.20         # fixation duration contribution
    w_blink: float = 0.25       # blink suppression contribution
    w_pupil: float = 0.20       # pupil size deviation contribution
    w_sacc: float = 0.10        # microsaccade density contribution

def clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))

def normalize(value: float, ref: float, max_ratio: float = 3.0) -> float:
    """Normalize by reference with saturation to avoid runaway scores."""
    ratio = value / (ref + 1e-9)
    return clamp(ratio / max_ratio, 0.0, 1.0)

def rsu_score(
    luminance_cd_m2: float,
    fixation_seconds: float,
    blink_rate_per_min: float,
    baseline_blink_per_min: float = 18.0,
    pupil_mm: float = 3.5,
    baseline_pupil_mm: float = 3.5,
    microsaccades_per_min: float = 25.0,
    baseline_microsaccades_per_min: float = 25.0,
    weights: RSUWeights = RSUWeights(),
) -> float:
    """Compute a unitless RSU in [0,1] as an operational stress index.

    This is a parametric placeholder meant for pilot studies.
    """
    lux_n = clamp(luminance_cd_m2 / 300.0, 0.0, 1.0)  # saturate ~300 cd/m^2
    fix_n = clamp(fixation_seconds / 5.0, 0.0, 1.0)   # saturate ~5s continuous fixation
    blink_suppr = clamp((baseline_blink_per_min - blink_rate_per_min) / baseline_blink_per_min, 0.0, 1.0)
    pupil_dev = clamp(abs(pupil_mm - baseline_pupil_mm) / max(1.0, baseline_pupil_mm), 0.0, 1.0)
    sacc_n = normalize(microsaccades_per_min, baseline_microsaccades_per_min)

    return (
        weights.w_lux * lux_n +
        weights.w_fix * fix_n +
        weights.w_blink * blink_suppr +
        weights.w_pupil * pupil_dev +
        weights.w_sacc * sacc_n
    )

if __name__ == "__main__":
    demo = rsu_score(
        luminance_cd_m2=250,
        fixation_seconds=4.0,
        blink_rate_per_min=6.0,
        pupil_mm=3.0,
        microsaccades_per_min=30.0,
    )
    print(f"Demo RSU={demo:.3f}")
