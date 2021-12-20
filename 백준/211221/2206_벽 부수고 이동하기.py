from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]


def bfs(graph, visit):
    q = deque([(0, 0, 0)])
    visit[0][0][0] = 1

    while q:
        cx, cy, cc = q.popleft()

        if cx == n - 1 and cy == m - 1:
            return visit[cx][cy][cc]

        for d in direction:
            dx, dy = cx + d[0], cy + d[1]

            if dx <= -1 or dx >= n or dy <= -1 or dy >= m:
                continue

            if graph[dx][dy] == 0 and visit[dx][dy][cc] == 0:
                q.append((dx, dy, cc))
                visit[dx][dy][cc] = visit[cx][cy][cc] + 1

            if graph[dx][dy] == 1 and cc == 0:
                q.append((dx, dy, cc + 1))
                visit[dx][dy][cc + 1] = visit[cx][cy][cc] + 1

    return -1


print(bfs(graph, visit))
