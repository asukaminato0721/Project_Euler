from cffi import FFI

ffi = FFI()
ffi.cdef("int totatives(int n);")
lib = ffi.dlopen("./72.dll")


def main() -> int:
    return sum(map(lib.totatives, range(2, 1000_000 + 1)))


assert main() == 303963552391
