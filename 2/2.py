def main() -> int:
    def fib():
        a, b = 0, 1
        while a < 400_0000:
            if a % 2 == 0:
                yield a
            a, b = b, a + b

    return sum(fib())


assert main() == 4613732
