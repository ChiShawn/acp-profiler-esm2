# Model Card

## Model Name

ACP-Profiler context-aware IC50 model

## Intended Use

The model estimates anticancer peptide potency as a peptide-cell-line-time IC50 regression event. It is intended for research prioritization and hypothesis generation, not for clinical decision making.

## Prediction Target

```text
label = -log10(IC50_uM)
```

Lower predicted IC50 corresponds to stronger predicted activity.

## Inputs

- Peptide-domain ESM2 mean embedding
- Peptide physicochemical descriptors and metadata
- Assay and cell-line categorical/numeric context
- Experimental context features curated from the activity records

## Model Architecture

- Protein language model peptide representation
- Peptide descriptor branch
- Experimental context branch
- Neural fusion and regression head

## Performance Summary

Standard-time source-row test set, N = 155:

| Method | RMSE | MAE | R2 | PCC |
|---|---:|---:|---:|---:|
| ACP-Profiler context-aware model | 0.3201 | 0.2107 | 0.6995 | 0.8419 |
| Raw ESM2 RidgeCV | 0.3981 | 0.2828 | 0.5352 | 0.7404 |
| Raw regression without token fusion | 0.3312 | 0.2137 | 0.6784 | 0.8289 |

Shared held-out IC50 subset for public xDeep-AcPEP comparison:

| Method | N | RMSE | MAE | R2 | PCC | Output resolution |
|---|---:|---:|---:|---:|---:|---|
| ACP-Profiler context-aware model | 58 | 0.3135 | 0.2155 | 0.6440 | 0.8069 | cell-line and time-resolved IC50 |
| xDeep-AcPEP | 58 | 0.6030 | 0.4665 | -0.3173 | 0.4197 | cancer-type/tissue-level activity model |

## Limitations

- The benchmark evaluates curated CancerPPD-derived IC50 events, not unrestricted de novo peptide discovery.
- xDeep-AcPEP is not an identical-output model: it is included as a public CancerPPD-based baseline, while ACP-Profiler is designed for cell-line/time IC50 profiling.
- The same peptide can appear under different contexts; event-level leakage was audited, but this is not a cold-peptide-only benchmark.
- Missing-time records lack measured assay time and should be interpreted as auxiliary diagnostics.
- Predicted all-context IC50 ranges are prioritization hypotheses, not experimentally verified fold changes.

## Ethical and Safety Notes

This model is for computational research prioritization. Experimental validation is required before biological or therapeutic claims.
