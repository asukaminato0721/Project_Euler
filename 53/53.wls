Table[Binomial[i, j], {i, 1, 100}, {j, 1, 100}] // Flatten // Count[u_ /; u > 1*^6]
