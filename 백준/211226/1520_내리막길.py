import sys

sys.setrecursionlimit(10 ** 6)  # 최대 재귀 깊이 변경

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visit = [[-1 for __ in range(m)] for _ in range(n)]


def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1

    if visit[x][y] != -1:
        return visit[x][y]

    visit[x][y] = 0

    for i in range(4):
        if (
            0 <= x + dx[i] < n
            and 0 <= y + dy[i] < m
            and graph[x][y] > graph[x + dx[i]][y + dy[i]]
        ):
            visit[x][y] += dfs(x + dx[i], y + dy[i])

    return visit[x][y]


print(dfs(0, 0))
