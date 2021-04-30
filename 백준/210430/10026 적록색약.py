import sys
from collections import deque

N = int(sys.stdin.readline())
graph = []
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
result = [0, 0]
visit = [[False for __ in range(N)] for _ in range(N)]

for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))


def bfs(r, c, color):
    q = deque([(r, c)])
    visit[r][c] = True

    while q:
        x, y = q.popleft()

        for d in directions:
            dx, dy = x+d[0], y+d[1]

            if -1 < dx < N and -1 < dy < N and not visit[dx][dy] and graph[dx][dy] == color:
                visit[dx][dy] = True
                q.append((dx, dy))


for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            bfs(i, j, graph[i][j])
            result[0] += 1

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visit = [[False for __ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            bfs(i, j, graph[i][j])
            result[1] += 1

print(*result)
