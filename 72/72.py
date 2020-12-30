from diofant.ntheory import totient


def main() -> int:
    return sum(map(totient, range(2, 1000_000 + 1)))


assert main() == 303963552391
