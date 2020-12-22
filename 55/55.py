def rever(num: int) -> int:
    return int(''.join(str(num)[::-1]))


def iff(n: int) -> bool:
    cnt = 0
    while True:
        n += rever(n)
        cnt += 1
        if n == rever(n):
            return False
        if cnt > 50:
            return True


def main() -> int:
    return sum(1 for i in range(1, 10000+1) if iff(i))


assert main() == 249
