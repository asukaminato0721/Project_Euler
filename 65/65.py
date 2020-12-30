from diofant.ntheory.continued_fraction import (
    continued_fraction_convergents,
    continued_fraction_iterator,
)
from diofant import E
from itertools import count


def main():
    for i, j in zip(
        count(1), continued_fraction_convergents(continued_fraction_iterator(E))
    ):
        if i == 100:
            return sum(map(int, str(j.numerator)))


assert main() == 272
