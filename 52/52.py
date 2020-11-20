from itertools import count


def iff(n):
    return all(sorted(str(i)) == sorted(str(n)) for i in range(n, 7 * n, n))


print(next(i for i in count(1) if iff(i)))
