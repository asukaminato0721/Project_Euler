from sympy.ntheory import totient

max(range(1, 1000_000+1), key=lambda x: x/totient(x))
