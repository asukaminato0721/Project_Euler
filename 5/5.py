from math import gcd
from functools import reduce
reduce(lambda x, y: x*y//gcd(x, y), range(1, 21), 1)
