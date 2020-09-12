Table[Boole[ (IntegerDigits[i] // Factorial // Total) == i]*i, {i, 3, 1000000}] // Total
