import sys

n, m = map(int, sys.stdin.readline().split())
graph, visit = [[] for _ in range(n+1)], [False]*(n+1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

result = 0


def dfs(idx):
    visit[idx] = True

    for g in graph[idx]:
        if not visit[g]:
            dfs(g)


for i in range(1, n+1):
    if not visit[i]:
        result += 1
        dfs(i)

print(result)

# pypy3로 돌렸을 때는 정답
