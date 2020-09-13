from sympy.ntheory import totient
import numpy as np
np.sum(np.frompyfunc(totient, 1, 1)(np.arange(2, 1000_000+1)))
