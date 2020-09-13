from itertools import count


def iff(n):
    same = sorted(str(n))
    return all(sorted(str(i)) == same for i in range(n, 7*n, n))


for i in count(1):
    if iff(i):
        print(i)
        break
