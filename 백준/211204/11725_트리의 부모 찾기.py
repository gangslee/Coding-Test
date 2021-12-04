import sys

sys.setrecursionlimit(10**6)  # 최대 재귀 깊이 변경

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
result = [10000]*(N+1)


def dfs(start):
    visit[start] = True

    for node in graph[start]:
        if not visit[node]:
            result[node] = start
            dfs(node)


for _ in range(N-1):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visit = [False]*(N+1)
dfs(1)


for i in range(2, N+1):
    print(result[i])
