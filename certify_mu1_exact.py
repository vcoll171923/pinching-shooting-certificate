#!/usr/bin/env python3
"""Exact-rational certificate for the shooting bounds in the pinching paper.

This script uses only Python's standard library. It evaluates the power-series
recurrence and the geometric tail estimate at the rational endpoints
mu_- = 584259/100000 and mu_+ = 584260/100000 with N = 30.
"""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction
from typing import List, Tuple

N = 30
MU_MINUS = Fraction(584259, 100000)
MU_PLUS = Fraction(584260, 100000)


def coefficients(mu: Fraction, last_index: int) -> List[Fraction]:
    """Return c_0,...,c_last_index from the exact recurrence."""
    c = [Fraction(1, 1)]
    for n in range(last_index):
        numerator = Fraction((2 * n + 1) * (2 * n + 4), 1) - mu
        denominator = Fraction((2 * n + 2) * (2 * n + 3), 1)
        c.append(c[-1] * numerator / denominator)
    return c


def shooting_bounds(mu: Fraction, n_cutoff: int = N) -> Tuple[Fraction, Fraction]:
    """Return the exact lower and upper bounds for S(mu)."""
    c = coefficients(mu, n_cutoff + 1)
    s_n = sum(
        Fraction((2 * n + 1), 2**n) * c[n]
        for n in range(n_cutoff + 1)
    )
    a_next = -Fraction(2 * (n_cutoff + 1) + 1, 2 ** (n_cutoff + 1)) * c[n_cutoff + 1]
    q_n = Fraction(1, 2) + Fraction(1, 2 * n_cutoff + 4)
    lower = s_n - a_next / (1 - q_n)
    upper = s_n
    return lower, upper


def decimal_string(value: Fraction, places: int = 24) -> str:
    getcontext().prec = places + 20
    d = Decimal(value.numerator) / Decimal(value.denominator)
    return f"{d:.{places}E}"


def main() -> None:
    lower_minus, upper_minus = shooting_bounds(MU_MINUS)
    lower_plus, upper_plus = shooting_bounds(MU_PLUS)

    # Exact comparisons corresponding to the outward-rounded decimal bounds
    # printed in the manuscript.
    assert lower_minus > Fraction(20068004693, 10**16)
    assert upper_minus < Fraction(20125400647, 10**16)
    assert lower_plus > -Fraction(28444241513, 10**16)
    assert upper_plus < -Fraction(28386845347, 10**16)

    # In particular, the shooting function changes sign across the interval.
    assert lower_minus > 0
    assert upper_plus < 0

    print(f"N = {N}")
    print(f"mu_- = {MU_MINUS}")
    print(f"lower bound for S(mu_-) = {lower_minus}")
    print(f"upper bound for S(mu_-) = {upper_minus}")
    print(f"decimal lower = {decimal_string(lower_minus)}")
    print(f"decimal upper = {decimal_string(upper_minus)}")
    print()
    print(f"mu_+ = {MU_PLUS}")
    print(f"lower bound for S(mu_+) = {lower_plus}")
    print(f"upper bound for S(mu_+) = {upper_plus}")
    print(f"decimal lower = {decimal_string(lower_plus)}")
    print(f"decimal upper = {decimal_string(upper_plus)}")
    print()
    print("All exact rational assertions passed.")


if __name__ == "__main__":
    main()
