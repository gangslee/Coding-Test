import sys
from collections import deque


graph, start, goal = [], [], []
direction = [[-2, -1], [-1, -2], [1, -2],
             [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1]]

n = int(sys.stdin.readline())


def bfs(s, g, l):
    q = deque([[s[0], s[1]]])

    while q:
        current = q.popleft()
        if current == g:
            print(graph[current[0]][current[1]])
            return
        for d in direction:
            dx, dy = current[0]+d[0], current[1]+d[1]

            if (0 <= dx < l) and (0 <= dy < l) and graph[dx][dy] == 0:
                graph[dx][dy] = graph[current[0]][current[1]]+1
                q.append([dx, dy])


for _ in range(n):
    length = int(sys.stdin.readline())
    graph = [[0 for ___ in range(length)]for __ in range(length)]
    start = list(map(int, sys.stdin.readline().split()))
    goal = list(map(int, sys.stdin.readline().split()))
    bfs(start, goal, length)
