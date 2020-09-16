def main():
    for c in range(333, 1000):
        for b in range(1, c):
            for a in range(1, b):
                if a+b+c == 1000 and a**2+b**2 == c**2:
                    print(a*b*c)
                    return 0


main()
