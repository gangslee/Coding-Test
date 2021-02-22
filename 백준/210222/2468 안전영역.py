import sys
from collections import deque

n = int(sys.stdin.readline())

graph, directions = list(), [(0, -1), (-1, 0), (0, 1), (1, 0)]
maxHeight = 1

for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    maxHeight = max(maxHeight, max(temp))
    graph.append(temp)

result = [1]*(maxHeight+1)


def getResult(idx):
    cnt = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j] > idx and not visit[i][j]:
                visit[i][j] = True
                bfs(i, j, idx)
                cnt += 1

    return cnt


def bfs(c, r, idx):
    q = deque([(c, r)])

    while q:
        current = q.popleft()
        for d in directions:
            if -1 < current[0]+d[0] < n and -1 < current[1]+d[1] < n and graph[current[0]+d[0]][current[1]+d[1]] > idx and not visit[current[0]+d[0]][current[1]+d[1]]:
                q.append((current[0]+d[0], current[1]+d[1]))
                visit[current[0]+d[0]][current[1]+d[1]] = True


for i in range(1, maxHeight):
    visit = [[False for __ in range(n)] for _ in range(n)]
    result[i] = getResult(i)

print(max(result))
