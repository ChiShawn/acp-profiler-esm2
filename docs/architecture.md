# Architecture

## End-to-End Workflow

```mermaid
flowchart LR
    A[CancerPPD IC50 records] --> B[IC50 parsing and unit normalization]
    B --> C[Standard-time filtering: 12/24/36/48/72 h]
    C --> D[Context curation and leakage audit]
    D --> E[Leakage-aware source-row train/val/test split]

    F[PeptideAtlas peptides] --> G[Peptide-domain ESM2 MLM adaptation]
    G --> H[Frozen ESM2 peptide embeddings]

    I[Internal context features] --> J[Context representation]

    E --> L[Model-ready peptide-cell-line-time events]
    H --> L
    J --> L

    L --> M[Cross-attention fusion IC50 regressor]
    M --> N[Standard-time test evaluation]
    M --> O[Missing-time external diagnostic]
    M --> P[Web profiling utility]
```

## Model Inputs

```mermaid
flowchart TB
    S[Peptide sequence] --> ESM[ESM2 mean embedding]
    S --> DESC[37 peptide descriptors + metadata]
    CTX[Assay and cell-line context] --> ASSAY[time, assay, cancer type, cell-line category]
    DEP[Experimental context] --> CTX[context token]

    ESM --> T1[64-d peptide token]
    DESC --> T2[64-d descriptor token]
    ASSAY --> T3[64-d assay/context token]
    CTX --> T4[context representation token]

    T1 --> F[model token set]
    T2 --> F
    T3 --> F
    T4 --> F

    F --> XATTN[context-aware fusion]
    XATTN --> HEAD[wide regression head]
    HEAD --> Y[-log10 IC50_uM]
```

## Evaluation Design

```mermaid
flowchart LR
    A[Train split] --> B[Model fitting]
    C[Validation split] --> D[Model selection]
    B --> D
    D --> E[Lock selected model]
    E --> F[Standard-time test set]
    E --> G[Raw ESM2 RidgeCV comparator]
    E --> H[No-token-fusion regression comparator]
    E --> I[xDeep-AcPEP public baseline comparison]
    E --> J[Missing-time diagnostic]
```

## Portfolio Scope

This diagram intentionally abstracts internal feature engineering details. The public version is meant to show the research design without exposing the full internal training recipe.
