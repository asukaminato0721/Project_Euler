poly3 = set(i * (i + 1) // 2 for i in range(1, 1000000))
poly5 = set(i * (3 * i - 1) // 2 for i in range(1, 1000000))
poly6 = set(i * (2 * i - 1) for i in range(1, 1000000))
print(poly3 & poly5 & poly6)
