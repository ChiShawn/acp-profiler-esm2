# Data Governance and Release Policy

This repository is designed as a public-readable research portfolio, not as a redistribution package for third-party biological datasets.

## Data Sources Used in the Research Project

- CancerPPD: anticancer peptide activity records and IC50-like labels
- Protein language model resources used for peptide representation
- Private context features used for model development

## Files Excluded From GitHub

The following files should not be committed:

- Raw third-party data files
- Full processed row-level datasets
- Train/validation/test split CSVs containing CancerPPD-derived rows
- `.npz` feature matrices
- `.pt` model checkpoints
- downloaded PDFs
- Word documents
- local environment files and credentials

## What Is Safe to Include

- Source code
- Configuration files
- Small summary tables
- Architecture diagrams
- Documentation of curation rules and model design
- Toy examples with synthetic or minimal non-sensitive inputs

## Reproducibility Position

External datasets should be downloaded by users from their official sources according to each provider's terms. This portfolio repository intentionally avoids exposing the full internal feature schema or model-ready data matrices.
