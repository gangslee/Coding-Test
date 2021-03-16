import sys
from itertools import combinations

n, s = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

result = 0

for i in range(1, n+1):
    for c in combinations(l, i):
        if sum(c) == s:
            result += 1

print(result)

# 부분순열은 연결된 애들이 아니여도 됨
