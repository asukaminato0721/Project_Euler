from itertools import accumulate
from operator import add
from sympy.ntheory import divisor_count


for i in accumulate(range(10000000), add):
    if divisor_count(i) > 500:
        print(i)
        break
