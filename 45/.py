poly3 = set(i*(i+1)//2 for i in range(1, 1000000))
poly5 = set(i*(3*i-1)//2 for i in range(1, 1000000))
poly6 = set(i*(2*i-1) for i in range(1, 1000000))
set.intersection(poly3, poly6, poly5)
