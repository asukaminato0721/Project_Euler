from diofant.ntheory import totient


def main() -> int:
    return max(range(1, 1000_000 + 1), key=lambda x: x / totient(x))


assert main() == 510510
