from collections import deque

n, m = map(int, input().split())
graph = []
visit = []
direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
check = False

for _ in range(n):
    graph.append(list(map(int, input().split())))


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        current = q.popleft()
        visit[x][y] = True

        for d in direction:
            dx, dy = current[0]+d[0], current[1]+d[1]

            if 0 <= dx < n and 0 <= dy < m:
                if not visit[dx][dy] and graph[dx][dy] > 0:
                    visit[dx][dy] = True
                    q.append((dx, dy))
                elif graph[dx][dy] == 0:
                    temp[current[0]][current[1]] += 1

    return 1


result = 0
year = 0

while True:

    temp = [[0]*m for _ in range(n)]

    visit = [[False] * m for _ in range(n)]

    result = []

    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and visit[i][j] == False:
                result.append(bfs(i, j))

    for i in range(n):
        for j in range(m):
            graph[i][j] -= temp[i][j]

            if graph[i][j] < 0:
                graph[i][j] = 0

    if len(result) == 0:
        break
    if len(result) >= 2:
        check = True
        break
    year += 1

if check:
    print(year)
else:
    print(0)
