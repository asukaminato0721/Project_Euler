from math import gcd
from functools import reduce


def main() -> int:
    return reduce(lambda x, y: x*y//gcd(x, y), range(1, 21), 1)


assert main() == 232792560
