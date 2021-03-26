def rever(num: int) -> int:
    return int("".join(str(num)[::-1]))


def iff(n: int) -> int:
    cnt = 0
    while True:
        n += rever(n)
        cnt += 1
        if n == rever(n):
            return 0
        if cnt > 50:
            return 1


def main() -> int:
    return sum(iff(i) for i in range(1, 10000 + 1))


assert main() == 249
