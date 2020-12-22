from diofant import primerange, isprime
from collections import defaultdict
from itertools import accumulate
from operator import add, itemgetter

num = defaultdict(int)


def foo(start: int = 1) -> None:
    for i, j in enumerate(accumulate(primerange(start, 100_0000), add)):
        if j > 100_0000:
            break
        if isprime(j):
            num[i] = j


[foo(k) for k in range(1, 100)]


def main() -> int:
    return max(num.items(), key=itemgetter(0))[-1]


assert main() == 997651
