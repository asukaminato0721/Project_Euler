from diofant.ntheory import primerange, isprime


def foo1(a):
    tmp = len(str(a))
    return ((str(a)*2)[i: i + tmp] for i in range(tmp))


def foo2(a):
    return (int(i) for i in foo1(a))


def foo3(a):
    return all(isprime(j) for j in foo2(a))


print(sum(1 for i in primerange(1, 100_0000) if foo3(i)))
