[README(1).md](https://github.com/user-attachments/files/30960945/README.1.md)
# Exact-Rational Shooting Certificate

This repository contains the computer-assisted shooting calculation used in the paper on the pinching theorem by Vincent E. Coll, Jr. and Lee B. Whitt.

## Purpose

The script

```text
certify_mu1_exact.py
```

provides an exact-rational certificate for the numerical estimate

\[
5.84259 < \mu_1 < 5.84260,
\]

where \(\mu_1\) is the spectral quantity arising in the shooting argument used in the proof of the pinching theorem.

The computation is intended to make the numerical component of the proof independently reproducible.

## Requirements

Only standard Python 3 is required.

No third-party Python packages are needed.

## Running the certificate

From the repository directory, run

```bash
python certify_mu1_exact.py
```

On some systems the command may instead be

```bash
python3 certify_mu1_exact.py
```

## Expected output

A successful run ends with

```text
All exact rational assertions passed.
```

This confirms the exact-rational inequalities used to certify the stated interval for \(\mu_1\).

## Arithmetic

The certification step uses exact rational arithmetic rather than floating-point comparisons. The cutoff used in the certificate is

\[
N=30.
\]

Thus the final verification of the interval is not dependent on machine floating-point roundoff.

## Reproducibility

The purpose of this repository is to provide a short, independently executable verification of the computer-assisted portion of the argument.

The mathematical derivation of the shooting problem and its connection with the geometric pinching theorem are given in the accompanying paper.

## Authors

Vincent E. Coll, Jr.  
Lee B. Whitt
