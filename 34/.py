from math import factorial, floor


def foo(a: int) -> bool:
    return sum(factorial(int(i)) for i in str(a)) == a

# First[n /. NSolve[{10^n == 9! n, n > 1}, n]] == 6.36346


def main() -> int:
    return sum(set(i for i in range(3, floor(10**6.36346)) if foo(i)))


assert main() == 40730
