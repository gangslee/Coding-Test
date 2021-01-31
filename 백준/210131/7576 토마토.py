import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())

tomato, visit = list(), [[False for __ in range(m)] for _ in range(n)]
direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]
noZero, result = True, 0

for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    tomato.append(row)

    if noZero and 0 in row:
        noZero = False


def bfs(q):

    global result

    while q:
        result += 1
        temp = list()
        for current in q:
            if visit[current[0]][current[1]]:
                continue

            visit[current[0]][current[1]] = True

            for d in direction:
                r, c = current[0]+d[0], current[1]+d[1]

                if -1 < r < n and -1 < c < m and tomato[r][c] == 0 and not visit[r][c]:
                    temp.append((r, c))
                    tomato[r][c] = 1
        q = deque(temp)
        print(tomato)


if noZero:
    print(result)

else:
    result = 0
    q = deque([])
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 1 and not visit[i][j]:
                q.append((i, j))

    bfs(q)

    for l in tomato:
        if 0 in l:
            print(-1)
            exit()

    print(result-1)
