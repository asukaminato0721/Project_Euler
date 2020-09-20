from diofant import binomial
print(sum(1 for i in range(1, 101)
          for j in range(1, 101)
          if binomial(i, j) > 1000000))
