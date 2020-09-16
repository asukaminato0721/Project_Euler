max(i*j for i in range(100, 1000) for j in range(i, 999) if int(''.join(reversed(str(i*j)))) == i*j)
