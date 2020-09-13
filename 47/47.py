from sympy.ntheory import factorint as FactorInteger


def iff(n):
    return len(FactorInteger(n)) == 4


for i in range(1, 100_0000):
    if all(iff(i) for i in range(i, i+4)):
        print(i)
        break
