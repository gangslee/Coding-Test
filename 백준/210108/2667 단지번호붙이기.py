import sys
from collections import deque

danji = []

n = int(sys.stdin.readline())

jido, visit = [], [[False for __ in range(n)] for _ in range(n)]

direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

for _ in range(n):
    jido.append(sys.stdin.readline())


def bfs(start, end):
    bfsQue = deque([(start, end)])

    while bfsQue:
        current = bfsQue.popleft()

        for d in direction:
            if current[0]+d[0] < 0 or current[1]+d[1] < 0 or current[0]+d[0] >= n or current[1]+d[1] >= n or jido[current[0]+d[0]][current[1]+d[1]] == '0' or visit[current[0]+d[0]][current[1]+d[1]]:
                continue
            danji[-1] += 1
            visit[current[0]+d[0]][current[1]+d[1]] = True
            bfsQue.append((current[0]+d[0], current[1]+d[1]))


for i in range(n):
    for j in range(n):
        if visit[i][j] or jido[i][j] == '0':
            continue
        danji.append(1)
        visit[i][j] = True
        bfs(i, j)

print(len(danji))
danji.sort()
for i in danji:
    print(i)
