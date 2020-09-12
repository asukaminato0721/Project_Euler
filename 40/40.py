from functools import reduce
from operator import mul
ChampernowneNumber = ''.join(str(i) for i in range(10**6+1))
reduce(mul,  (int(ChampernowneNumber[10**i]) for i in range(6)), 1)
