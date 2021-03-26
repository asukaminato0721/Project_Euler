def main() -> int:
    return max(
        i * j
        for i in range(100, 1000)
        for j in range(i, 999)
        if (k := str(i * j))[::-1] == k
    )


assert main() == 906609
