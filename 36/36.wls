Select[Range[1, 1000000 - 1, 2], (PalindromeQ@#) && (PalindromeQ@IntegerDigits[#, 2]) &] // Total
(*二进制下偶数不可能回文*)
