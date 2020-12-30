from math import prod


def main() -> int:
    ChampernowneNumber = "".join(str(i) for i in range(10 ** 6 + 1))
    return prod(int(ChampernowneNumber[10 ** i]) for i in range(6))


assert main() == 210
