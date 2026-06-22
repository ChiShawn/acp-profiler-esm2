#!/usr/bin/env python3
"""Print the public ACP-Profiler performance summary."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SUMMARY = ROOT / "results" / "model_performance_summary.csv"


def main() -> None:
    df = pd.read_csv(SUMMARY)
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()
