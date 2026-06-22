# GitHub Release Checklist

Before making this repository public:

- [ ] Confirm no `.docx`, `.pdf`, `.pt`, `.npz`, `.npy`, `.tar.gz`, or raw data files are present.
- [ ] Confirm `git status --short` only shows intended public files.
- [ ] Review scripts for absolute local paths and replace them with config arguments where practical.
- [ ] Decide whether research scripts expose too much internal know-how; if yes, replace with simplified portfolio scripts before public release.
- [ ] Decide on license. Use a permissive code license only if you are comfortable releasing the code publicly.
- [ ] Keep third-party raw data and model weights out of GitHub.
- [ ] Keep complete row-level CancerPPD-derived CSV files out of GitHub.
- [ ] Add a short repository description and topics on GitHub:
  - `bioinformatics`
  - `anticancer-peptides`
  - `protein-language-models`
  - `esm2`
  - `xdeep-acpep`
  - `drug-discovery`
- [ ] Add screenshots or rendered Mermaid diagrams if GitHub rendering is not enough.
- [ ] Optionally create a private repo first and inspect it as a reviewer before making it public.
