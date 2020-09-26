def foo(a, b, c):
    return sorted(set((*str(a), *str(b), *str(c)))) == [str(i) for i in range(1, 10)]


print(sum(set(i*j for i in range(1, 100)
              for j in range(100, 10000) if foo(i, j, i*j) if i*j <= 9999)))
