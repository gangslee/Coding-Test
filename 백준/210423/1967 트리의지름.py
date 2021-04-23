# root로 부터 최대 거리 노드를 구하고 해당 노드에서 가장 먼 노드까지의 거리값을 구함

import sys
sys.setrecursionlimit(10**9)    # 재귀 깊이 증가

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    x, y, z = map(int, sys.stdin.readline().split())
    graph[x].append((y, z))
    graph[y].append((x, z))

result = [0]*(n+1)


def dfs(start, result):
    for node, value in graph[start]:
        if result[node] == 0:
            result[node] = result[start]+value
            dfs(node, result)


dfs(1, result)

result[1] = 0
maxIdx = result.index(max(result))

result = [0]*(n+1)
dfs(maxIdx, result)
result[maxIdx] = 0
print(max(result))
