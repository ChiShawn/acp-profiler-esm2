# Interview Talking Points

## One-Minute Summary

I built ACP-Profiler, a context-aware anticancer peptide IC50 regression workflow. Instead of predicting whether a peptide is ACP-positive from sequence alone, the model predicts peptide-cell-line-time IC50 events by combining peptide-domain ESM2 representations, peptide physicochemical descriptors, and curated experimental context.

## What This Demonstrates

- Biological problem framing: ACP activity depends on cell line, assay, and exposure time.
- Data curation: CancerPPD IC50 parsing, unit normalization, sequence filtering, and context cleaning.
- Representation learning: ESM2-based peptide representation and frozen embedding extraction.
- Leakage awareness: split design with peptide-cell-line-time event audit.
- Model design: peptide representation, context-aware fusion, and regression head comparison.
- Evaluation discipline: peptide-embedding baseline, non-fusion regression baseline, xDeep-AcPEP public comparison, and held-out IC50 summary metrics.
- Deployment thinking: command-line inference interface for context-ranked IC50 profiles.

## Important Design Decision

The public portfolio version does not expose the full internal feature schema. It focuses on the scientific framing: IC50 is context dependent, so the model should treat activity as a peptide-cell-line-time regression event rather than a peptide-only class label.

## Main Result to Mention

On the held-out IC50 test set:

- ACP-Profiler context-aware model: RMSE 0.3201, PCC 0.8419
- Raw ESM2 RidgeCV: RMSE 0.3981, PCC 0.7404
- Raw regression without token fusion: RMSE 0.3312, PCC 0.8289

On the shared held-out subset used for xDeep-AcPEP comparison:

- ACP-Profiler: RMSE 0.3135, PCC 0.8069
- xDeep-AcPEP: RMSE 0.6030, PCC 0.4197

The key methodological difference is that xDeep-AcPEP is cancer-type/tissue-level, while ACP-Profiler models cell-line- and time-resolved IC50 events.

## Limitation to State Clearly

This is not a claim of universal de novo ACP discovery. It is a context-aware IC50 profiling model built from curated CancerPPD-derived records. Experimental validation is required for generated variants or ranked assay conditions.

## If Asked Why GitHub Does Not Include Data or Weights

The repo excludes raw data, processed matrices, and checkpoints because the project uses third-party biological datasets with redistribution constraints. I include code, configs, documentation, architecture diagrams, and summary metrics so the design and implementation are reviewable without redistributing external data.
