def main() -> int:
    return len(set(i ** j for i in range(2, 101) for j in range(2, 101)))


assert main() == 9183
