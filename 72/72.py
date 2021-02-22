import os
from ctypes import CFUNCTYPE, c_int
from pytcc import TCC

PATH = os.path.dirname(os.path.abspath(__file__))
comp = TCC()
comp.add_library_path("./")
comp.add_file(os.path.join(PATH, "72.c"))
comp.relocate()
totatives = comp.get_symbol("totatives")
totatives = CFUNCTYPE(c_int, c_int)(totatives)


def main() -> int:
    return sum(map(totatives, range(2, 1000_000 + 1)))


assert main() == 303963552391
