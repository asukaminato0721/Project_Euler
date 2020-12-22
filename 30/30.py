def iff(n: int) -> bool:
    return sum(int(i)**5 for i in str(n)) == n


def main() -> int:
    return sum(i for i in range(2, 1000000) if iff(i))


assert main() == 443839
