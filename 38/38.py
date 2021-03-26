def foo(n: int) -> bool:
    return sorted(f"{n}{2*n}") == [str(i) for i in range(1, 10)]


def main() -> int:
    return max(int(f"{n}{2*n}") for n in range(9000, 10000) if foo(n))


assert main() == 932718654
