from ctypes import CDLL, CFUNCTYPE, c_int

totatives = CDLL("./72.dll").totatives
totatives = CFUNCTYPE(c_int, c_int)(totatives)


def main() -> int:
    return sum(map(totatives, range(2, 1000_000 + 1)))


assert main() == 303963552391
