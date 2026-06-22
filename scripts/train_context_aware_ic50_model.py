#!/usr/bin/env python3
"""Portfolio skeleton for ACP-Profiler training.

The production research code is intentionally not included in this public
portfolio folder. This script documents the modeling stages without exposing
internal feature schemas or model-ready data paths.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TrainingPlan:
    activity_database: str = "CancerPPD"
    target: str = "-log10(IC50_uM)"
    peptide_representation: str = "protein language model embedding"
    model_family: str = "context-aware neural IC50 regressor"
    evaluation: str = "held-out IC50 regression"


def main() -> None:
    plan = TrainingPlan()
    print("ACP-Profiler training plan")
    for key, value in plan.__dict__.items():
        print(f"- {key}: {value}")
    print("\nProduction training code and model-ready feature schemas are kept private.")


if __name__ == "__main__":
    main()
