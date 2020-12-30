from diofant import binomial


def main() -> int:
    return sum(1 for i in range(1, 101)
               for j in range(1, 101)
               if binomial(i, j) > 1000000)


assert main() == 4075
