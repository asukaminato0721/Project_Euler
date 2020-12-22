from diofant.ntheory import primerange, isprime


def foo1(a: int):
    tmp = len(str(a))
    return (f'{a}{a}'[i: i + tmp] for i in range(tmp))


def foo2(a: int):
    return (int(i) for i in foo1(a))


def foo3(a: int) -> bool:
    return all(map(isprime, foo2(a)))


def main() -> int:
    return sum(1 for i in primerange(1, 100_0000) if foo3(i))


assert main() == 55
