from diofant.ntheory import factorint as FactorInteger
from itertools import count
for i in count(1):
    if all(len(FactorInteger(n)) == 4 for n in range(i, i+4)):
        print(i)
        break
