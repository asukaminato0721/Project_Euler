from itertools import count


def main():
    a, b = 0, 1
    for i in count():
        if len(str(a)) >= 1000:
            return i
        a, b = b, a + b


assert main() == 4782
