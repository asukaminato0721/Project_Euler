from functools import reduce
from operator import add


def foo(num):
    while num > 0:
        yield num % 10
        num //= 10


reduce(add, foo(2**1000), 0)
