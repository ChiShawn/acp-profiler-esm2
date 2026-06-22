# ACP-Profiler: ESM2-Based IC50 Profiling for Anticancer Peptides

ACP-Profiler is a research portfolio project for context-aware anticancer peptide activity modeling using CancerPPD-derived IC50 records. Instead of predicting a peptide-only ACP/non-ACP label, this project models a quantitative peptide-cell-line-time IC50 event:

```text
peptide sequence + peptide descriptors + experimental context
-> -log10(IC50_uM)
```

This repository is intentionally a **portfolio version**, not the full internal research release. It shows the problem framing, model interface, architecture, and selected summary results while keeping internal feature engineering details, processed datasets, training code, comparator evaluation code, and model weights private.

## Why This Project Matters

Most ACP prediction tools are sequence-only classifiers or cancer-type/tissue-level predictors. Experimental IC50, however, is measured under a specific cell-line, assay, and exposure-time condition. This project reframes ACP activity prediction as a context-resolved regression task and shows the bioinformatics workflow: CancerPPD curation, leakage-aware splitting, protein language model representation, baseline comparison, and deployment-style profiling.

## Research Highlights

- Curated CancerPPD IC50 records into peptide-cell-line-time regression events.
- Used peptide-domain ESM2 representations and peptide physicochemical descriptors.
- Built context-aware neural regression models for quantitative IC50 prediction.
- Evaluated against peptide-embedding and non-fusion regression baselines.
- Compared against xDeep-AcPEP as a public CancerPPD-based ACP baseline.
- Built a lightweight inference-style webapp prototype for peptide context profiling and candidate ranking.

## Model Summary

| Setting | Value |
|---|---|
| Peptide representation | ESM2-derived embedding |
| Additional inputs | peptide descriptors and experimental context |
| Objective | transformed IC50 regression |
| Evaluation | held-out IC50 test events |
| Portfolio release | inference/demo interface and summary metrics only |

## Key Results

Held-out IC50 regression summary:

| Method | RMSE | MAE | R2 | PCC |
|---|---:|---:|---:|---:|
| ACP-Profiler context-aware model | 0.3201 | 0.2107 | 0.6995 | 0.8419 |
| Raw ESM2 RidgeCV | 0.3981 | 0.2828 | 0.5352 | 0.7404 |
| Raw regression without token fusion | 0.3312 | 0.2137 | 0.6784 | 0.8289 |

Public xDeep-AcPEP comparison on the shared held-out IC50 subset:

| Method | N | RMSE | MAE | R2 | PCC | Output resolution |
|---|---:|---:|---:|---:|---:|---|
| ACP-Profiler context-aware model | 58 | 0.3135 | 0.2155 | 0.6440 | 0.8069 | cell-line and time-resolved IC50 |
| xDeep-AcPEP | 58 | 0.6030 | 0.4665 | -0.3173 | 0.4197 | cancer-type/tissue-level activity model |

The key distinction is not only accuracy. xDeep-AcPEP provides cancer-type/tissue-level activity modeling, whereas ACP-Profiler models cell-line- and time-resolved IC50 events.

The public repository reports summary metrics only. Full row-level datasets and internal training artifacts are not included.

## Repository Layout

```text
ACP_research/
  README.md
  configs/                  # Abstract portfolio config examples
  docs/                     # Markdown-only research documentation and architecture diagrams
  examples/                 # Toy inputs only, no third-party raw data
  results/                  # Small summary tables only
  scripts/                  # Inference/demo and public result utilities
```

## What Is Not Included

This repository intentionally does not include:

- CancerPPD raw data or derived row-level tables
- processed `.npz` feature matrices
- model checkpoints or ESM2 weights
- full row-level train/validation/test CSV files
- training, pretraining, or comparator evaluation scripts
- PDFs or Word documents

These files are excluded because of size, third-party redistribution constraints, and GitHub portfolio hygiene. The repository is intended to show the scientific design and implementation, not to redistribute external datasets.

## Documentation

- [Architecture](docs/architecture.md)
- [Data governance and release policy](docs/data_governance.md)
- [Model card](docs/model_card.md)
- [Usage and release policy](docs/usage.md)

## Status

This is a cleaned research/portfolio version prepared from the active ACP project. It is suitable for review before deciding whether to publish to GitHub. A future publication-ready release can be rebuilt from a separate branch or merged into a new `main` after the manuscript and data-release policy are finalized.
