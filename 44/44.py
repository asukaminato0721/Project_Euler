from itertools import combinations


def main() -> int:
    poly = set(i * (3 * i - 1) // 2 for i in range(1, 10000))
    for i, j in combinations(poly, 2):
        if (k := abs(j - i)) in poly and j + i in poly:
            return k


assert main() == 5482660
