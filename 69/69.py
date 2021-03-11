from ctypes import CDLL, CFUNCTYPE, c_double, c_int

key = CDLL("./69.dll").key
key = CFUNCTYPE(c_double, c_int)(key)


def main() -> int:
    return max(range(3, 1000_000 + 1), key=key)


assert main() == 510510
