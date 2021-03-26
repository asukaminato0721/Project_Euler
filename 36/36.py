def foo(x: int) -> str:
    return bin(x)[2:]


def main() -> int:
    return sum(
        i
        for i in range(1, 100_0000 + 1)
        if str(i)[::-1] == str(i) and foo(i) == foo(i)[::-1]
    )


assert main() == 872187
