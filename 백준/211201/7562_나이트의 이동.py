import sys
from collections import deque

n = int(sys.stdin.readline())
graph, start, goal = [], [], []
direction = [[-2, -1], [-1, -2], [1, -2],
             [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1]]

for _ in range(n):
    length = int(sys.stdin.readline())
    graph.append([[0 for ___ in range(length)]for __ in range(length)])
    start.append(list(map(int, sys.stdin.readline().split())))
    goal.append(list(map(int, sys.stdin.readline().split())))


def bfs(s, g, v):
    q = deque([[s[0], s[1]]])

    while q:
        current = q.popleft()

        for d in direction:
            dx, dy = current[0]+d[0], current[1]+d[1]

            if (0 <= dx < len(v)) and (0 <= dy < len(v)) and (not visit[dx][dy]) and graph[i][dx][dy] == 0:
                v[dx][dy] = True
                graph[i][dx][dy] = graph[i][current[0]][current[1]]+1
                q.append([dx, dy])


for i in range(n):
    visit = [[False for __ in range(len(graph[i]))]
             for _ in range(len(graph[i]))]
    if start[i] == goal[i]:
        print(0)
    else:
        graph[i][start[i][0]][start[i][1]] = 0
        bfs(start[i], goal[i], visit)
        print(graph[i][goal[i][0]][goal[i][1]])
