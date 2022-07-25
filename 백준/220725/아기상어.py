from collections import deque

N = int(input())
shark = [2, 0]
graph = []
start = []
result = [[0 for __ in range(N)] for _ in range(N)]
visit = [[False for __ in range(N)] for _ in range(N)]
direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

for i in range(N):
    row = list(map(int, input().split()))

    if 9 in row:
        start = [i, row.index(9)]

    graph.append(row)


def bfs(start):
    q = deque([start])
    visit[start[0]][start[1]] = True

    while q:
        current = q.popleft()

        for d in direction:
            if graph[current[0]+d[0]][current[1]+d[1]] <= shark[0] and not visit[current[0]+d[0]][current[1]+d[1]]:
                if 0 < graph[current[0]+d[0]][current[1]+d[1]] < shark[0]:
                    shark[1] += 1

                    if shark[0] == shark[1]:
                        shark[0] += 1
                        shark[1] = 0

                visit[current[0]+d[0]][current[1]+d[1]] = True
                q.append([current[0]+d[0], current[1]+d[1]])
                result[current[0]+d[0]][current[1]+d[1]
                                        ] = result[current[0]][current[1]] + 1


bfs(start)


# print(graph)
