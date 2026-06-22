#!/usr/bin/env python3
"""Public ACP-Profiler inference interface.

This portfolio release exposes the expected command-line input/output contract.
The trained model bundle and private feature pipeline are not included.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = ["sequence", "cell_line", "time_hours", "assay"]
OUTPUT_COLUMNS = [
    "sequence",
    "cell_line",
    "time_hours",
    "assay",
    "prediction_status",
    "predicted_neg_log10_ic50_um",
    "predicted_ic50_um",
    "rank",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate ACP-Profiler inputs and write the public inference output schema."
    )
    parser.add_argument("-i", "--input", required=True, help="Input CSV file.")
    parser.add_argument("-o", "--output", required=True, help="Output CSV file.")
    parser.add_argument(
        "--model-bundle",
        help=(
            "Optional path reserved for a future released inference bundle. "
            "The portfolio repository does not include this artifact."
        ),
    )
    return parser.parse_args()


def normalize_sequence(value: object) -> str:
    return "".join(ch for ch in str(value).upper() if ch.isalpha())


def load_input(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    missing = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing:
        joined = ", ".join(missing)
        raise SystemExit(f"Input CSV is missing required column(s): {joined}")

    df = df[REQUIRED_COLUMNS].copy()
    df["sequence"] = df["sequence"].map(normalize_sequence)
    if df["sequence"].eq("").any():
        raise SystemExit("Input CSV contains empty peptide sequences after normalization.")
    return df


def build_public_output(df: pd.DataFrame, model_bundle: str | None) -> pd.DataFrame:
    if model_bundle:
        status = "model_bundle_not_released_in_public_repo"
    else:
        status = "validated_input_no_public_model_bundle"

    output = df.copy()
    output["prediction_status"] = status
    output["predicted_neg_log10_ic50_um"] = pd.NA
    output["predicted_ic50_um"] = pd.NA
    output["rank"] = pd.NA
    return output[OUTPUT_COLUMNS]


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)

    df = load_input(input_path)
    output = build_public_output(df, args.model_bundle)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output.to_csv(output_path, index=False)
    print(f"Wrote {len(output)} row(s) to {output_path}")


if __name__ == "__main__":
    main()
