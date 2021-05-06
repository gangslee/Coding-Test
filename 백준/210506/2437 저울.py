import sys
from itertools import combinations

N = int(sys.stdin.readline())

choo = list(map(int, sys.stdin.readline().split()))
choo.sort()

current = 1

for c in choo:
    if c > current:
        break
    current += c

print(current)
