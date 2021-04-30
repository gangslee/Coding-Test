import sys

V = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]

for _ in range(V):
    info = list(map(int, sys.stdin.readline().split()))

    for i in range(1, len(info)//2):
        graph[info[0]].append((info[2*i-1], info[2*i]))

result = [0]*(V+1)


def dfs(start, result):
    for node, value in graph[start]:
        if result[node] == 0:
            result[node] = result[start]+value
            dfs(node, result)


dfs(1, result)
startNode = result.index(max(result))

result = [0]*(V+1)

dfs(startNode, result)
result[startNode] = 0

print(max(result))
