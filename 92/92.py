solu89 = set((89,))
solu1 = set((1,))


def sqrsum(i):
    s = 0
    while i > 0:
        s += (i % 10)**2
        i //= 10
    return s


def sol(i):
    temp = [i]
    while True:
        if i in solu89:
            solu89.update(temp)
            break
        elif i in solu1:
            solu1.update(temp)
            break
        else:
            temp.append(i)
        i = sqrsum(i)


for i in range(1, 1000_0000):
    sol(i)
len(solu89)
