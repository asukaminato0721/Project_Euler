def main():
    return sum(pow(i, i, 10 ** 10) for i in range(1, 1001)) % 10 ** 10


assert main() == 9110846700
