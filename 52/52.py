from itertools import count


def iff(n: int) -> bool:
    return all(sorted(str(i)) == sorted(str(n)) for i in range(n, 7 * n, n))


def main() -> int:
    return (next(i for i in count(1) if iff(i)))


assert main() == 142857
