# Architecture

## End-to-End Workflow

```mermaid
flowchart LR
    A[User CSV: peptide + assay context] --> B[Input validation]
    B --> C[Peptide representation]
    B --> D[Context representation]
    C --> E[ACP-Profiler inference model]
    D --> E
    E --> F[Predicted IC50 profile]
    F --> G[Ranked peptide-context candidates]

    H[Public result tables] --> I[Performance summary]
    J[Model card] --> I
```

The public workflow is inference-oriented. It documents the expected user input
and output contract without exposing the internal training, feature-generation,
or model-selection pipeline.

## Model Inputs

```mermaid
flowchart TB
    S[Peptide sequence] --> ESM[ESM2 mean embedding]
    S --> DESC[Peptide descriptors]
    CTX[Assay context] --> ASSAY[time, assay, cell-line label]

    ESM --> T1[peptide token]
    DESC --> T2[descriptor token]
    ASSAY --> T3[context token]

    T1 --> F[model token set]
    T2 --> F
    T3 --> F

    F --> XATTN[context-aware fusion]
    XATTN --> HEAD[regression head]
    HEAD --> Y[-log10 IC50_uM]
```

## Evaluation Design

```mermaid
flowchart LR
    A[Held-out IC50 events] --> B[ACP-Profiler summary metrics]
    C[Peptide representation baseline] --> D[Baseline summary metrics]
    E[Non-fusion regression baseline] --> D
    F[xDeep-AcPEP public baseline] --> G[Cross-model comparison]
    B --> H[Public performance tables]
    D --> H
    G --> H
```

Evaluation details are reported at summary level only. The public repository
keeps row-level datasets, split files, comparator scripts, and training code out
of scope while still documenting the benchmark logic and final metrics.

## Portfolio Scope

These diagrams intentionally abstract internal feature engineering details. The
public version is meant to show the model interface, architectural reasoning,
and evaluation logic without exposing the full internal training recipe.
