#!/usr/bin/env python3
"""
================================================================================
DDSD Framework - Automated Verification Script
================================================================================
Verifies that all data files match the paper's claims.
Run this before submission to arXiv or any journal.

Usage:
    python verify_submission.py
================================================================================
"""

import csv
import json
import sys

def verify():
    errors = []

    # Load data
    with open('data/collatz_ksweep.csv', 'r') as f:
        collatz_ksweep = list(csv.DictReader(f))
    with open('data/fivexone_ksweep.csv', 'r') as f:
        fivexone_ksweep = list(csv.DictReader(f))
    with open('data/verification_results.json', 'r') as f:
        verif = json.load(f)

    # 1. Trajectory counts
    if verif['metadata']['collatz_traj'] != 952:
        errors.append(f"Collatz trajectories: expected 952, got {verif['metadata']['collatz_traj']}")
    if verif['metadata']['fivexone_traj'] != 200:
        errors.append(f"5x+1 trajectories: expected 200, got {verif['metadata']['fivexone_traj']}")

    # 2. A1 k=6
    a1_cor = verif['collatz']['A1']['correlation']
    if abs(a1_cor - 0.182) > 0.01:
        errors.append(f"A1 k=6 correlation: expected ~0.182, got {a1_cor:.4f}")

    # 3. A3 Collatz K=8
    for row in collatz_ksweep:
        if int(row['K']) == 8:
            phi = float(row['phi'])
            if abs(phi - (-0.081)) > 0.005:
                errors.append(f"A3 Collatz K=8: expected ~-0.081, got {phi:.5f}")
            if row['bonferroni_verified'] != 'True':
                errors.append("A3 Collatz K=8: expected Bonferroni verified=True")
            break

    # 4. A3 5x+1 K=8
    for row in fivexone_ksweep:
        if int(row['K']) == 8:
            phi = float(row['phi'])
            if abs(phi - 0.0001) > 0.001:
                errors.append(f"A3 5x+1 K=8: expected ~0.0001, got {phi:.5f}")
            if row['bonferroni_verified'] != 'False':
                errors.append("A3 5x+1 K=8: expected Bonferroni verified=False")
            break

    # 5. A4
    a4_c = verif['collatz']['A4_e2']['mean_frequency']
    if abs(a4_c - 0.522) > 0.01:
        errors.append(f"A4 Collatz: expected ~0.522, got {a4_c:.3f}")

    # Report
    if errors:
        print("VERIFICATION FAILED:")
        for e in errors:
            print(f"  ✗ {e}")
        sys.exit(1)
    else:
        print("VERIFICATION PASSED: All data matches paper claims.")
        sys.exit(0)

if __name__ == '__main__':
    verify()
