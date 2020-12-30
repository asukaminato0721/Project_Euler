from diofant.ntheory.continued_fraction import continued_fraction_periodic
from diofant import sqrt


def main() -> int:
    return sum(
        (not sqrt(i).is_Integer)
        and bool(continued_fraction_periodic(p=0, q=1, d=i)[0] & 1)
        for i in range(1, 10000 + 1)
    )


assert main() == 1322
