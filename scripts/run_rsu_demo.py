#!/usr/bin/env python
from rsu import rsu_score
import random

def main():
    samples = []
    for _ in range(12):
        s = rsu_score(
            luminance_cd_m2=random.uniform(120, 320),
            fixation_seconds=random.uniform(1.5, 6.0),
            blink_rate_per_min=random.uniform(3.0, 18.0),
            pupil_mm=random.uniform(2.5, 4.5),
            microsaccades_per_min=random.uniform(15, 40),
        )
        samples.append(s)
    mean = sum(samples)/len(samples)
    print(f"Synthetic RSU demo — mean={mean:.3f}; min={min(samples):.3f}; max={max(samples):.3f}")

if __name__ == "__main__":
    main()
