# Usage and Release Policy

This repository is an inference-oriented portfolio release. It is designed to
show the ACP-Profiler model interface, architecture, and public summary
performance without releasing the internal training pipeline.

## Public Usage

The public entry points are:

```bash
python scripts/acp_profiler_cli.py \
  --input examples/toy_input.csv \
  --output outputs/toy_predictions.csv
```

```bash
python scripts/show_public_results.py
```

The CLI validates the public input schema and writes the expected inference
output schema. Prediction values are intentionally blank in this portfolio
release because the trained model bundle and private feature pipeline are not
published. The public results script prints the released summary tables.

The expected input columns are:

- `sequence`
- `cell_line`
- `time_hours`
- `assay`

## Not Released

The public repository intentionally does not include:

- training scripts
- comparator evaluation scripts
- row-level CancerPPD-derived tables
- processed feature matrices
- internal feature schemas
- pretraining or fine-tuning recipes
- a hosted backend service

If a model bundle is released later, it should be added as an inference artifact
with a minimal loader and versioned model card. It should not require exposing
the private training workflow.
