from diofant.ntheory.partitions_ import npartitions


def main() -> int:
    return npartitions(100) - 1


assert main() == 190569291
