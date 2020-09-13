from collections import defaultdict

rows_by_num = defaultdict(list)


def key(n):
    return ''.join(sorted(str(n)))


for i in (i**3 for i in range(10000+1)):
    rows_by_num[key(i)].append(i)
min(min(i for i in rows_by_num.values() if len(i) == 5))
