from cffi import FFI

ffi = FFI()
ffi.cdef("double key(int n);")
lib = ffi.dlopen("./69.dll")


def main() -> int:
    return max(range(3, 1000_000 + 1), key=lib.key)


assert main() == 510510
