import sys

R, C = map(int, sys.stdin.readline().split())
graph = [list(map(lambda x:ord(x)-65, input())) for _ in range(R)]
visit = [False]*26
result = 1
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(x, y, cnt):
    global result
    result = max(result, cnt)

    for i in range(4):
        nx, ny = x+d[i][0], y+d[i][1]

        if 0 <= nx < R and 0 <= ny < C and not visit[graph[nx][ny]]:
            visit[graph[nx][ny]] = True
            dfs(nx, ny, cnt+1)
            visit[graph[nx][ny]] = False


visit[graph[0][0]] = True
dfs(0, 0, result)
print(result)
