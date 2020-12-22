from fractions import Fraction


def frac():
    n = Fraction(1, 2)
    while True:
        yield n+1
        n = 1/(2+n)


def main() -> int:
    return sum(1 for i, j in zip(range(1000), frac())
               if len(str(j.numerator)) > len(str(j.denominator)))


assert main() == 153
