def foo(x):
    return bin(x)[2:]


print(sum(i for i in range(1, 100_0000+1) if str(i)
          [::-1] == str(i) and foo(i) == foo(i)[::-1]))
