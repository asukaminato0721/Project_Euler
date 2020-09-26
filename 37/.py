from diofant.ntheory import isprime

left, right = {2, 3, 5, 7}, {2, 3, 5, 7}
range10 = {'', '1', '2', '3', '4', '5', '6', '7', '8', '9'}


for _ in range(5):
    left = {int(str(i)+j) for i in left for j in range10
            if isprime(int(str(i) + j))}
    right = {int(j+str(i)) for i in right for j in range10
             if isprime(int(j + str(i)))}
print(sum(left & right - {2, 3, 5, 7}))
