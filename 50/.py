from diofant import primerange, isprime
from collections import defaultdict
from itertools import accumulate
from operator import add

num = defaultdict(int)


def foo(start=1):
    for i, j in enumerate(accumulate(primerange(start, 100_0000), add)):
        if j > 100_0000:
            break
        if isprime(j):
            num[i] = j


for k in range(1, 100):
    foo(k)

print(max(num.items(), key=lambda x: x[0]))
