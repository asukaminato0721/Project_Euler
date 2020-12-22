from diofant.ntheory import isprime

left = right = {2, 3, 5, 7}
range10 = {'', '1', '2', '3', '4', '5', '6', '7', '8', '9'}


for _ in range(5):
    left = {int(f'{i}{j}') for i in left for j in range10
            if isprime(int(f'{i}{j}'))}
    right = {int(f'{j}{i}') for i in right for j in range10
             if isprime(int(f'{j}{i}'))}


def main() -> int:
    return sum(left & right - {2, 3, 5, 7})


assert main() == 748317
