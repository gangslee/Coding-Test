from collections import deque
from re import T

N = int(input())
x, y, size = -1, -1, 2
graph = []
start = []
direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

for i in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            x = i
            y = j


def bfs(x, y, size):
    q = deque()
    q.append((x, y))

    result = [[0 for __ in range(N)] for _ in range(N)]
    visit = [[False for __ in range(N)] for _ in range(N)]
    visit[x][y] = True
    temp = []

    while q:
        current = q.popleft()

        for d in direction:
            dx, dy = current[0]+d[0], current[1]+d[1]

            if 0 <= dx < N and 0 <= dy < N and not visit[dx][dy]:
                if graph[dx][dy] <= size:
                    q.append((dx, dy))
                    visit[dx][dy] = True
                    result[dx][dy] = result[current[0]][current[1]] + 1

                    if 0 < graph[dx][dy] < size:
                        temp.append((dx, dy, result[dx][dy]))

    return sorted(temp, key=lambda x: (-x[2], -x[0], -x[1]))


cnt = 0
result = 0

while True:
    shark = bfs(x, y, size)

    if len(shark) == 0:
        break

    nx, ny, dist = shark.pop()

    result += dist
    graph[x][y], graph[nx][ny] = 0, 0

    x, y = nx, ny
    cnt += 1

    if cnt == size:
        size += 1
        cnt = 0

print(result)
