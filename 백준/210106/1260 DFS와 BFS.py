import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())

edges = [[0 for __ in range(n+1)] for _ in range(n+1)]

# 2차원 리스트를 통해 모든 간선의 연관 관계를 정의
for _ in range(m):
    first, second = map(int, (sys.stdin.readline().split()))
    edges[first][second] = 1
    edges[second][first] = 1


dfsVisit, bfsVisit = [False]*(n+1), [False]*(n+1)


def dfs(start):
    if dfsVisit[start]:
        return
    dfsVisit[start] = True
    print(start, end=' ')

    for i in range(n):
        if edges[start][i+1] == 1:
            dfs(i+1)


def bfs(idx):
    bfsQue = deque([idx])
    bfsVisit[idx] = True
    while bfsQue:
        start = bfsQue.popleft()
        print(start, end=' ')

        for i in range(n):
            if edges[start][i+1] == 1 and not bfsVisit[i+1]:
                bfsQue.append(i+1)
                bfsVisit[i+1] = True


dfs(v)
print()
bfs(v)
