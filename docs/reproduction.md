# Reproduction Notes

This cleaned repository intentionally omits raw data, processed matrices, model weights, and internal feature-schema details.

## High-Level Steps

1. Download CancerPPD activity records from the official provider according to its terms.
2. Parse activity rows and retain numeric IC50 records.
3. Normalize IC50 units to uM and compute `-log10(IC50_uM)`.
4. Curate experimental context fields and perform leakage-aware splitting.
5. Extract or load peptide-domain ESM2 mean embeddings.
6. Train a context-aware IC50 regression model.
7. Evaluate held-out test rows and comparator baselines.
8. Optionally run auxiliary diagnostics and the webapp prototype.

## Example Commands

The exact paths depend on where the third-party data and model weights are stored.

```bash
python scripts/train_context_aware_ic50_model.py \
  --config configs/portfolio_model_example.yaml
```

```bash
python scripts/evaluate_standard_time_comparators.py \
  --checkpoint /path/to/checkpoint.pt \
  --feature_matrix /path/to/model_ready_features
```

```bash
python scripts/context_aware_ic50_webapp.py \
  --checkpoint /path/to/checkpoint.pt \
  --feature_matrix /path/to/model_ready_features
```

## Portfolio Note

The scripts in this folder are kept close to the research version to show the actual modeling workflow. Some paths may need to be adapted before reuse in a new environment.
