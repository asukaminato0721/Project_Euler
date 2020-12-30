from diofant.ntheory import factorint
from itertools import count


def main() -> int:
    return next(
        i
        for i in count(1)
        if all(len(factorint(n)) == 4 for n in range(i, i + 4))
    )


assert main() == 134043
