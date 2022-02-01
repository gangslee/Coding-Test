n = int(input())
graph = [[] for _ in range(n+1)]
visit = [False for _ in range(n+1)]

start, end = map(int, input().split())
visit[start] = True

m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

result = n+1


def dfs(current, cnt):
    global result
    if current == end:
        result = min(result, cnt)
    for i in graph[current]:
        if not visit[i]:
            visit[i] = True
            dfs(i, cnt+1)
            visit[i] = False


dfs(start, 0)
if result == n+1:
    print(-1)
else:
    print(result)
