import os
from ctypes import CFUNCTYPE, c_double, c_int
from pytcc import TCC

PATH = os.path.dirname(os.path.abspath(__file__))
comp = TCC()
comp.add_library_path("./")
comp.add_file(os.path.join(PATH, "69.c"))
comp.relocate()
key = comp.get_symbol("key")
key = CFUNCTYPE(c_double, c_int)(key)


def main() -> int:
    return max(range(3, 1000_000 + 1), key=key)


assert main() == 510510
