from sympy.ntheory.continued_fraction import continued_fraction
from sympy import sqrt
import numpy as np


def iff(i):
    return (not sqrt(i).is_Integer) and len(continued_fraction(sqrt(i))[-1]) % 2 == 1


iss = np.frompyfunc(iff, 1, 1)

print(np.sum(np.where(iss(np.arange(1, 10001)), 1, 0)))
