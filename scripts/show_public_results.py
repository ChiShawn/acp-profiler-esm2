#!/usr/bin/env python3
"""Print the public ACP-Profiler result summaries."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RESULTS = [
    ROOT / "results" / "model_performance_summary.csv",
    ROOT / "results" / "xdeep_acpep_comparison_summary.csv",
]


def main() -> None:
    for path in RESULTS:
        print(f"\n{path.name}")
        print(pd.read_csv(path).to_string(index=False))


if __name__ == "__main__":
    main()
