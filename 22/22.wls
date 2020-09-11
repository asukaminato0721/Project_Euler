data = Import[ "https://projecteuler.net/project/resources/p022_names.txt"] // StringReplace["\"" -> ""] // StringSplit[#, ","] & // Sort;
MapIndexed[#1*First@#2 &, data // Map[ToCharacterCode[#, "UTF8"] & /* (# - 64 &) /* Total]] // Total
