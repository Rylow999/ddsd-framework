# DDSD Framework: Structural Dissipation in Discrete Dynamical Systems

[![arXiv](https://img.shields.io/badge/arXiv-2406.XXXXX-b31b1b.svg)](https://arxiv.org/abs/2406.XXXXX)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Abstract

We introduce the DDSD (Dissipative Dynamical System with Decoupling) framework as a computational characterization of dissipative behavior in discrete dynamical systems. Four measurable axioms are proposed: (A1) resolution-dependent decorrelation, (A2) intrafiber output dispersion, (A3) scale-dependent negative macroscopic drift, and (A4) pathwise recurrence. Verification on the Collatz 3x+1 map, the divergent 5x+1 map, a parametric family ax+1, and other systems shows that **A3 is the discriminant axiom**: Collatz exhibits significant negative drift (Bonferroni-corrected p < 10⁻¹⁰); 5x+1 shows drift ≈ 0. The exact 2-adic drift is proven to be Φ(a) = log₂(a) - 2, placing Collatz as the last odd dissipative map before the inaccessible boundary at a=4. A genetic algorithm discovers maps with 2.5× stronger dissipation than Collatz. 

**This paper does not prove Collatz boundedness.** Rather, it provides a taxonomic framework for dissipative systems and localizes Collatz within a precise phase diagram.

## Key Results

- ✅ **A3 Discriminates**: Collatz (Φ = -0.415) vs 5x+1 (Φ ≈ 0)
- ✅ **Exact Theory**: Φ(a) = log₂(a) - 2 for maps Rₐ(n) = (an+1)/2^ν₂(aₙ+₁)
- ✅ **Phase Boundary**: Collatz is the last dissipative odd map before a=4
- ✅ **Optimality**: GA discovers map with drift -0.23 (2.5× Collatz)
- ✅ **Cryptographic Link**: Toy hash exhibits drift -1.29 with perfect decorrelation

## Reproducibility

All code, data, and figures are provided for independent verification.

```bash
# Install dependencies
pip install -r requirements.txt

# Regenerate all results and figures
python src/master_simulation.py

# Verify data consistency
python src/verify_submission.py
```

**Seed:** 42 (all simulations)
**Runtime:** ~5-10 minutes
**Output:** 14 figures, verification tables, console report

## File Structure

```
.
├── README.md                    # Quick start guide
├── README_ARXIV.md              # This file
├── LICENSE                      # MIT
├── requirements.txt             # Python dependencies
├── src/
│   ├── master_simulation.py     # Complete reproduction suite
│   └── verify_submission.py     # Data integrity checks
├── data/
│   ├── verification_results.json
│   ├── collatz_ksweep.csv
│   ├── fivexone_ksweep.csv
│   └── ax1_family.csv
├── figures/                     # 14 PNG figures
└── paper/
    ├── ddsd_paper.tex           # LaTeX (publication-ready)
    ├── ddsd_paper.md            # Markdown (GitHub-ready)
    └── [references to figures]
```

## Main Claims and Verification

| Claim | Evidence | Table/Figure |
|-------|----------|--------------|
| A3 discriminates Collatz/5x+1 | Bonferroni p-values | Table 2-3 |
| Φ(a) = log₂(a) - 2 | Theoretical proof | Theorem 5.1 |
| Collatz is boundary | a=3 < a=4 (inaccessible) | Corollary 5.2 |
| GA optimizes dissipation | Drift -0.23 > -0.415 | Section 6 |
| Toy hash: hyper-dissipative | Drift -1.29 | Table 6 |

All claims are verified in Section 3 (Computational Verification) with independent code.

## Requirements

- Python 3.12+
- NumPy 1.24+
- SciPy 1.11+
- scikit-learn 1.3+
- Matplotlib 3.7+ (for figure generation)

For LaTeX compilation:
- TeX Live 2020+ or MiKTeX 2020+
- All standard packages included in full distributions

## Citation

```bibtex
@article{Nieto2026DDSD,
  title={Structural Dissipation in Discrete Dynamical Systems: 
         A Computational Characterization},
  author={Nieto, Luciano Benjamín},
  journal={arXiv preprint arXiv:2406.XXXXX},
  year={2026}
}
```

## Related Work

- **Tao (2019):** Almost all Collatz orbits attain almost bounded values (arXiv:1909.03562)
- **Lagarias (1985):** The 3x+1 problem and its generalizations (AMM)
- **Conway (1972):** On numbers and games (BAMS)

## Open Questions

1. **Invariant measure:** Does a unique T-invariant measure exist for Collatz?
2. **Axiom independence:** Which axioms imply others?
3. **Continuous extension:** How do A1-A4 generalize to ODEs/PDEs?
4. **Cryptography connection:** What is the mechanistic link between A1-A3 and cryptographic security?
5. **Higher dimensions:** Does the framework extend to multidimensional maps?

## Contact

**Luciano Benjamín Nieto**  
Independent Researcher, General Alvear, Mendoza, Argentina  

GitHub: [@delorien](https://github.com/delorien)

## License

This work is licensed under the MIT License (see LICENSE file).

## Acknowledgments

Thanks to Lautaro Luconi for collaborations on the broader NOUS/DSCN-G framework and conceptual discussions that informed this work.

---

**Submitted to:** arXiv  
**Date:** June 18, 2026  
**Framework version:** DDSD 2.0  
**Code version:** v1.0.0
