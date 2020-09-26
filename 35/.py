from diofant.ntheory import primerange, isprime
from itertools import cycle, islice


def foo1(a):
    return (islice(cycle(str(a)), i, i + len(str(a))) for i in range(len(str(a))))


def tonum(a):
    return int(''.join(a))


def foo2(a):
    return (tonum(i) for i in foo1(a))


def foo3(a):
    return all(isprime(j) for j in foo2(a))


print(sum(1 for i in primerange(1, 100_0000) if foo3(i)))
