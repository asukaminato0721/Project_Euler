from itertools import accumulate
from operator import add
from diofant.ntheory import divisor_count
from itertools import count

for i in accumulate(count(1), add):
    if divisor_count(i) > 500:
        print(i)
        break
