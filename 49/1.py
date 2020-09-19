from sympy import primerange, isprime
from itertools import combinations
prime = set(primerange(1000, 10000))
for i, k in combinations(prime, 2):
    if sorted(str(i)) == sorted(str(m := ((i+k)//2))) == sorted(str(k)) and isprime(m):
        print(*sorted((i, k, m)), sep='')
