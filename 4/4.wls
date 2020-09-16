Select[Flatten@Table[i j , {i, 100, 999}, {j, i, 999}], PalindromeQ] // Max
