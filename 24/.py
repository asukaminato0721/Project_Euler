from itertools import permutations
for i, j in enumerate(permutations(range(10))):
    if i == 100_0000-1:
        print(j)
        break
