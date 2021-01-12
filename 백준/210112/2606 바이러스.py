import sys

n = int(sys.stdin.readline())

m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]

visit, result = [False]*(n+1), [False]*(n+1)

for _ in range(m):
    c1, c2 = map(int, sys.stdin.readline().split())
    graph[c1].append(c2)
    graph[c2].append(c1)


def dfs(idx):
    if visit[idx]:
        return

    visit[idx], result[idx] = True, True

    for i in graph[idx]:
        dfs(i)


dfs(1)
print(result.count(True)-1)
