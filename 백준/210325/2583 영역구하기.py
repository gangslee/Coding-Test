import sys
from collections import deque

M, N, K = map(int, sys.stdin.readline().split())

graph = [[0 for __ in range(M)] for _ in range(N)]
visit = [[False for __ in range(M)] for _ in range(N)]
direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
rect, result = [], []

for _ in range(K):
    rect.append(list(map(int, sys.stdin.readline().split())))

for i in range(K):
    for j in range(rect[i][0], rect[i][2]):
        for k in range(rect[i][1], rect[i][3]):
            graph[j][k] = 1


def bfs(x, y):
    cnt = 0
    q = deque([(x, y)])

    while q:
        current = q.popleft()
        cnt += 1

        for d in direction:
            nx, ny = current[0]+d[0], current[1]+d[1]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0 and not visit[nx][ny]:
                q.append((current[0]+d[0], current[1]+d[1]))
                graph[current[0]+d[0]][current[1]+d[1]] = 1
                visit[current[0]+d[0]][current[1]+d[1]] = True

    return cnt


for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and not visit[i][j]:
            visit[i][j] = True
            graph[i][j] = 1
            result.append(bfs(i, j))

result.sort()

print(len(result))
print(*result)
