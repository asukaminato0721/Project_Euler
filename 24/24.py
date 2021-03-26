from itertools import permutations


def main() -> tuple:
    return next(
        j for i, j in enumerate(permutations(range(10))) if i == 100_0000 - 1
    )


assert "".join(map(str, main())) == 2783915460
