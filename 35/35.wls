rot[x_] := With[{li = IntegerDigits[x]}, NestList[RotateLeft, li, Length@li - 1]] // Map[FromDigits]
pri = Prime@Range@PrimePi@1000000;
Select[pri, AllTrue[rot[#], PrimeQ] &] // Length
