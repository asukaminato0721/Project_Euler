def foo(n):
    return sorted(str(n) + str(2*n)) == [str(i) for i in range(1, 10)]


print(max(int(str(n) + str(2*n)) for n in range(9000, 10000) if foo(n)))
