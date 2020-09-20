from diofant.ntheory import totient

print(max(range(1, 1000_000+1), key=lambda x: x/totient(x)))
