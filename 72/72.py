from numba import njit


def main() -> int:
    @njit
    def totatives(n):
        phi = int(n > 1 and n)
        for p in range(2, int(n ** 0.5) + 1):
            if not n % p:
                phi -= phi // p
                while not n % p:
                    n //= p
        # if n is > 1 it means it is prime
        if n > 1:
            phi -= phi // n
        return phi

    return sum(map(totatives, range(2, 1000_000 + 1)))


assert main() == 303963552391
