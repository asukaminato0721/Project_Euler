def rever(num):
    return int(''.join(reversed(str(num))))


def iff(n):
    cnt = 0
    while True:
        n += rever(n)
        cnt += 1
        if n == rever(n):
            return False
        if cnt > 50:
            return True


sum(1 for i in range(1, 10000+1) if iff(i))
