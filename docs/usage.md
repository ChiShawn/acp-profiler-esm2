# Usage and Release Policy

This repository is an inference-oriented portfolio release. It is designed to
show the ACP-Profiler model interface, architecture, and public summary
performance without releasing the internal training pipeline.

## Public Usage

The public entry points are:

```bash
python scripts/context_aware_ic50_webapp.py
```

```bash
python scripts/show_public_results.py
```

The webapp is a lightweight demonstration of the intended model interaction:
submit a peptide sequence and inspect context-aware IC50 profiling output. The
public results script prints the released summary tables.

## Not Released

The public repository intentionally does not include:

- training scripts
- comparator evaluation scripts
- row-level CancerPPD-derived tables
- processed feature matrices
- internal feature schemas
- pretraining or fine-tuning recipes

If a model bundle is released later, it should be added as an inference artifact
with a minimal loader and versioned model card. It should not require exposing
the private training workflow.
