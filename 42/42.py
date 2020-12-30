import httpx


def main() -> int:
    tri = {n * (n + 1) // 2 for n in range(1, 1000)}

    text = (
        httpx.get("https://projecteuler.net/project/resources/p042_words.txt")
        .text.replace('"', "")
        .split(",")
    )

    def num(a: str) -> int:
        return ord(a) - ord("A") + 1

    return sum((sum(num(i) for i in j) in tri) for j in text)


assert main() == 162
