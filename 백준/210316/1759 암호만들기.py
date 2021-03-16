import sys
from itertools import combinations

l, c = map(int, sys.stdin.readline().split())
a = list(sys.stdin.readline().split())

moeum = ['a', 'e', 'i', 'o', 'u']

a = sorted(a, key=lambda x: x)

for c in combinations(a, l):
    mcnt = 0

    for m in moeum:
        if m in c:
            mcnt += 1
    if mcnt > 0 and l-mcnt > 1:
        for i in c:
            print(i, end='')
        print()
