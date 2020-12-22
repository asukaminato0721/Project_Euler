from math import factorial


def main() -> int:
    return sum(map(int, str(factorial(100))))


assert main() == 648
