from math import lcm


def main() -> int:
    return lcm(*range(1, 21))


assert main() == 232792560
