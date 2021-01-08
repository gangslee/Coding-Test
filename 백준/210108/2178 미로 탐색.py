import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

miro, result, visit = [], [[n*m+1 for __ in range(m)] for _ in range(n)], [
    [False for __ in range(m)] for _ in range(n)]

for _ in range(n):
    miro.append(sys.stdin.readline())

bfsQue = deque([(0, 0)])

result[0][0] = 1
visit[0][0] = True
diretion = [(-1, 0), (0, -1), (1, 0), (0, 1)]

while bfsQue:
    current = bfsQue.popleft()

    for d in diretion:
        if current[0]+d[0] < 0:
            continue
        if current[0]+d[0] >= n:
            continue
        if current[1]+d[1] < 0:
            continue
        if current[1]+d[1] >= m:
            continue
        if visit[current[0]+d[0]][current[1]+d[1]]:
            continue
        if miro[current[0]+d[0]][current[1]+d[1]] == '0':
            continue

        visit[current[0]+d[0]][current[1]+d[1]] = True
        result[current[0]+d[0]][current[1]+d[1]] = min(
            result[current[0]+d[0]][current[1]+d[1]], result[current[0]][current[1]]+1)
        bfsQue.append((current[0]+d[0], current[1]+d[1]))

print(result[-1][-1])
