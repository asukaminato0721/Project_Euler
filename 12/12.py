from itertools import accumulate
from operator import add
from diofant.ntheory import divisor_count
from itertools import count


def main() -> int:
    return next(i for i in accumulate(count(1), add) if divisor_count(i) > 500)


assert main() == 76576500
