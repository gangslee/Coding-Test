import sys

T = int(sys.stdin.readline())
result = []


def dfs(idx, stack):
    if idx == graph[idx]:
        if len(stack) == 0:
            matched[idx] = True
        return

    stack.append(idx)

    if graph[idx] in stack:
        if graph[idx] == stack[0]:
            for s in stack:
                matched[s] = True
        return

    else:
        if not matched[graph[idx]] and graph[idx] not in unmatched:
            dfs(graph[idx], stack)


for _ in range(T):
    n = int(sys.stdin.readline())
    graph = [0]+list(map(int, sys.stdin.readline().split()))
    matched = [False]*(n+1)
    unmatched = []

    for i in range(1, n+1):
        if not matched[i]:
            dfs(i, [])
            if not matched[i]:
                unmatched.append(i)

    result.append(matched.count(False)-1)

for r in result:
    print(r)
