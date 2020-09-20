from diofant.ntheory.continued_fraction import continued_fraction_convergents, continued_fraction_iterator
from diofant import E
from itertools import count

for i, j in zip(count(1), continued_fraction_convergents(continued_fraction_iterator(E))):
    if i == 100:
        print(sum(int(k) for k in str(j.numerator)))
        break
