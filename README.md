# DDSD Framework: Structural Characterization of Discrete Dynamical Systems

**Author:** Luciano Benjamín Nieto  
**Affiliation:** Independent Researcher, General Alvear, Mendoza, Argentina    
**Series:** DDSD Part 1

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

Computational verification suite for the DDSD framework applied to Collatz, 5x+1,
perturbed families, critical maps, 2-adic variable fields, toy cryptographic hashes,
and evolved maps via genetic algorithm.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run complete reproduction suite (takes ~5-10 minutes)
python src/master_simulation.py

# Verify data integrity against paper claims
python src/verify_submission.py
```

## Structure

```
.
├── README.md                    # This file
├── LICENSE                      # MIT License
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore rules
├── src/
│   ├── master_simulation.py     # Complete reproduction suite (all experiments)
│   └── verify_submission.py     # Automated verification script
├── data/
│   ├── verification_results.json    # Axiom verification results
│   ├── invariant_measure_ml.json    # ML fit metrics
│   ├── collatz_ksweep.csv           # Collatz K-sweep data
│   ├── fivexone_ksweep.csv          # 5x+1 K-sweep data
│   └── ax1_family.csv               # ax+1 family phase diagram
├── figures/
│   ├── fig01_a1_correlation_decay.png
│   ├── fig02_ksweep_collatz.png
│   ├── fig03_ksweep_5x1.png
│   ├── fig04_invariant_measure.png
│   ├── fig05_scale_dependence.png
│   ├── fig06_a2_entropy.png
│   ├── fig07_phase_transition.png
│   ├── fig08_critical_map.png
│   ├── fig09_phase_diagram_exact.png
│   ├── fig10_2adic_and_tree.png
│   ├── fig11_percolation_and_primes.png
│   ├── fig12_variable_field.png
│   ├── fig13_toyhash_vs_collatz.png
│   └── fig14_evolution.png
└── paper/
    ├── ddsd_paper.md            # Markdown version (GitHub-ready)
    └── ddsd_paper.tex           # LaTeX version (arXiv-ready)
```

## Reproducibility

All simulations use fixed random seed `42` for full reproducibility.
The complete suite regenerates all data, figures, and verification reports.

**Expected outputs:**
- `data/*.json` and `data/*.csv` — Verification data
- `figures/*.png` — All 14 figures
- Console report with all metrics

## Key Results

- **Collatz**: 952 trajectories up to 2^40. A1-A3 verified structurally.
- **5x+1**: 200 trajectories. A3 fails under Bonferroni correction.
- **A4**: Does not discriminate between maps (shared property).
- **ML**: LOO-CV R²=0.96, exploratory evidence for smooth measure.
- **Phase diagram**: Exact drift in Z_2 is log₂(a) - 2. Collatz (a=3) is the last odd dissipative map.
- **Critical map 7/16**: Bimodal behavior (23% collapse, 77% explode). No macro-clusters.
- **Variable field**: Mixing dissipative and expansive zones yields ~60% termination.
- **Toy hash**: Hyper-dissipative (drift -1.29) with perfect decorrelation.
- **Evolved map**: Genetic algorithm discovers map with drift -0.23 (2.5× stronger than Collatz).
- **Primes**: No structural enrichment in inverse tree (statistical artifact).

## Verification

Before submission to any venue, run:

```bash
python src/verify_submission.py
```

This checks that all data files match the paper's claims. If it prints
"VERIFICATION PASSED", the submission is internally consistent.

## Citation

```bibtex
@article{Nieto2026DDSD,
  title={Structural Dissipation in Discrete Dynamical Systems: A Computational Characterization},
  author={Nieto, Luciano Benjamín},
  year={2026},
  note={arXiv preprint}
}
```

## Contact

For questions or issues, please open a GitHub issue or contact the authors.

---

*Per Aspera, Ad Astra.*
*Framework: DDSD v2.0*
*Seed: 42*
