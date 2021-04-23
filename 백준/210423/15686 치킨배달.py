import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

home, chicken = [], []

for i in range(N):
    street = list(map(int, sys.stdin.readline().split()))

    for j in range(len(street)):
        if street[j] == 1:
            home.append((i, j))
        elif street[j] == 2:
            chicken.append((i, j))

distance = list(combinations(chicken, M))
result = [0]*len(distance)

for h in home:
    for j in range(len(distance)):
        street = 100
        for i in distance[j]:
            temp = abs(h[0]-i[0])+abs(h[1]-i[1])
            street = min(street, temp)
        result[j] += street

print(min(result))
