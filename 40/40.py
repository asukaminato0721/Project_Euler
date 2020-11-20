from math import prod

ChampernowneNumber = "".join(str(i) for i in range(10 ** 6 + 1))
print(prod(int(ChampernowneNumber[10 ** i]) for i in range(6)))
