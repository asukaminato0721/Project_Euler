def sumdig(num: int) -> int:
    return sum(map(int, str(num)))


def main() -> int:
    return max(sumdig(i**j) for i in range(1, 100) for j in range(1, 100))


assert main() == 972
