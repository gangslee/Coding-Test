import sys
from collections import deque

t = int(sys.stdin.readline())

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def bfs(s1, s2, g):
    bfsQue = deque([(s1, s2)])
    while bfsQue:
        current = bfsQue.popleft()
        for d in directions:
            plusX, plusY = current[0]+d[0], current[1]+d[1]
            if 0 <= plusX < n and 0 <= plusY < m and not visit[plusX][plusY] and g[plusX][plusY] == 1:
                bfsQue.append((plusX, plusY))
                visit[plusX][plusY] = True


for i in range(t):
    n, m, k = map(int, sys.stdin.readline().split())
    graph = [[0 for __ in range(m)] for _ in range(n)]
    visit = [[False for __ in range(m)] for _ in range(n)]

    for j in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = 1

    result = 0

    for c in range(n):
        for r in range(m):
            if not visit[c][r] and graph[c][r] == 1:
                visit[c][r] = True
                bfs(c, r, graph)
                result += 1

    print(result)
