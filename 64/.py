from diofant.ntheory.continued_fraction import continued_fraction_periodic
from diofant import sqrt

print(sum(1 for i in range(1, 10000+1) if (not sqrt(i).is_Integer)
          and continued_fraction_periodic(p=0, q=1, d=i)[0] % 2 == 1))
