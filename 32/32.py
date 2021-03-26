def foo(a: int, b: int, c: int) -> bool:
    return sorted(set(f"{a}{b}{c}")) == [str(i) for i in range(1, 10)]


def main() -> int:
    return sum(
        set(
            i * j
            for i in range(1, 100)
            for j in range(100, 10000)
            if foo(i, j, i * j)
            if i * j <= 9999
        )
    )


assert main() == 45228
