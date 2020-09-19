from sympy import primerange
from itertools import combinations
for i, j, k in combinations(primerange(1000, 10000), 3):
    if sorted(str(i)) == sorted(str(j)) == sorted(str(k)) and i+k == 2*j:
        print(i, j, k)
