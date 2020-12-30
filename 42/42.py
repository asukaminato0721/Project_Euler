import requests

tri = {n*(n+1)//2 for n in range(1, 1000)}

text = requests.get(
    "https://projecteuler.net/project/resources/p042_words.txt"
).text.replace('\"', "").split(',')


def num(a: str) -> int:
    return ord(a)-ord('A')+1


print(sum(1 for j in text if (sum(num(i) for i in j) in tri)))
