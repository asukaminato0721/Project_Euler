is[n_Integer] := 
    With[{t = DivisorSum[n, # &] - n}, 
        DivisorSum[t, # &] - t == n && t != n]
Select[Range[2, 9999], is] // Total
