def iff(n):
    s = 0
    while n > 0:
        s += (n % 10)**5
        n //= 10
    return s

print(sum(i for i in range(2, 1000000) if iff(i) == i))


#---

import numpy as np


def iff(n):
    s = 0
    while n > 0:
        s += (n % 10)**5
        n //= 10
    return s


num = np.arange(2, 1000_0000)
ifff = np.frompyfunc(iff, 1, 1)
sum(num[ifff(num) == num])
