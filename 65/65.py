from sympy.ntheory.continued_fraction import continued_fraction_convergents, continued_fraction_iterator
from sympy.ntheory.digits import digits
from sympy import E

for i, j in zip(range(1, 101), continued_fraction_convergents(continued_fraction_iterator(E))):
    if i == 100:
        print(sum(digits(j.numerator())[1:]))
