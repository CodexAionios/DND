from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
import json, time
from rsu import rsu_score

@dataclass
class SessionConfig:
    target_rsu: float = 0.45
    block_seconds: int = 90
    rest_seconds: int = 30
    max_blocks: int = 10

class AVARSUSession:
    def __init__(self, cfg: SessionConfig):
        self.cfg = cfg
        self.blocks = []

    def log_block(self, luminance, fixation, blink_rate, pupil, microsaccades):
        score = rsu_score(luminance, fixation, blink_rate, pupil_mm=pupil, microsaccades_per_min=microsaccades)
        self.blocks.append({"rsu": score, "l": luminance, "fix": fixation, "blink": blink_rate, "pupil": pupil, "sacc": microsaccades})
        return score

    def summary(self):
        if not self.blocks:
            return {"n": 0, "mean_rsu": None}
        mean_rsu = sum(b["rsu"] for b in self.blocks)/len(self.blocks)
        return {"n": len(self.blocks), "mean_rsu": mean_rsu}
