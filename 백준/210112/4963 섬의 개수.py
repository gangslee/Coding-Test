import sys
from collections import deque

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
              (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]


def bfs(x, y):
    q = deque([(x, y)])

    while q:
        current = q.popleft()

        for d in directions:
            r, c = current[0]+d[0], current[1]+d[1]
            if 0 <= r < h and 0 <= c < w and not visit[r][c] and graph[r][c] == 1:
                visit[r][c] = True
                q.append((r, c))


while True:
    w, h = map(int, sys.stdin.readline().split())

    if w == 0 and h == 0:
        break

    graph, visit = [], [[False for __ in range(w)] for _ in range(h)]
    result = 0

    for i in range(h):
        graph.append(list(map(int, sys.stdin.readline().split())))

    for i in range(h):
        for j in range(w):
            if not visit[i][j] and graph[i][j] == 1:
                visit[i][j] = True
                result += 1
                bfs(i, j)
    print(result)
