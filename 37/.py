from diofant.ntheory import isprime
from itertools import chain

solleft = set((2, 3, 5, 7))
solright = set((2, 3, 5, 7))


def conj(num, num1):
    return int(str(num)+str(num1))


def fooleft(n):
    return set(conj(i, n)for i in range(1, 10) if isprime(conj(i, n)))


def fooright(n):
    return set(conj(n, i)for i in range(1, 10) if isprime(conj(n, i)))


for _ in range(5):
    solleft = set(chain.from_iterable(fooleft(i)
                                      for i in solleft)) | solleft
    solright = set(chain.from_iterable(fooright(i)
                                       for i in solright)) | solright
print(sum(solleft & solright - set((2, 3, 5, 7))))
