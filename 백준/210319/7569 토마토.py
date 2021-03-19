import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
tomato = [[] for _ in range(H)]
visit = [[[False for ___ in range(M)] for __ in range(N)] for _ in range(H)]
direction = [(-1, 0, 0), (1, 0, 0), (0, -1, 0),
             (0, 1, 0), (0, 0, -1), (0, 0, 1)]
q = deque([])
result = 0

for i in range(H):
    for j in range(N):
        tomato[i].append(list(map(int, sys.stdin.readline().split())))

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                q.append((i, j, k))


def bfs():
    while q:
        x, y, z = q.popleft()
        visit[x][y][z] = True

        for d in direction:
            nx, ny, nz = x+d[0], y+d[1], z+d[2]

            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and tomato[nx][ny][nz] == 0 and not visit[nx][ny][nz]:
                q.append((nx, ny, nz))
                tomato[nx][ny][nz] = tomato[x][y][z]+1
                visit[nx][ny][nz] = True


bfs()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 0:
                print(-1)
                exit()
            result = max(result, tomato[i][j][k])

print(result-1)
