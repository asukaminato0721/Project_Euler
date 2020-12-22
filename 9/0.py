def main() -> int:
    return next(a * b * c for c in range(333, 1000) for b in range(1, c)
                for a in range(1, b) if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2)


assert main() == 31875000
