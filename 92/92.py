solu89 = {89}
solu1 = {1}


def sqrsum(i: int) -> int:
    return sum(int(i) ** 2 for i in str(i))


def sol(i: int):
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

assert len(solu89) == 8581146
