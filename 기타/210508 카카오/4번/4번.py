def dfs(start, result, graph, end, traps, visited):
    if start == end:
        return

    visited[start] += 1

    if start in traps:
        for i in range(1, len(graph)):
            graph[start][i], graph[i][start] = graph[i][start], graph[start][i]

    if graph[start][end] != 0:
        result[end] = result[start]+graph[start][end]
        return

    for i in range(1, len(graph)):
        if graph[start][i] != 0 and visited[start] < 2:
            # print(start, i)
            # input()
            result[i] = result[start]+graph[start][i]
            dfs(i, result, graph, end, traps, visited)


def solution(n, start, end, roads, traps):
    graph = [[0 for __ in range(n+1)] for _ in range(n+1)]

    for r in roads:
        graph[r[0]][r[1]] = r[2]

    answer = [0]*(n+1)
    visited = [0]*(n+1)

    dfs(start, answer, graph, end, traps, visited)
    # print(answer)
    return answer[end]


nn = 4
startstart = 1
endend = 4
roadsrodasd = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
trapsasdas = [2, 3]

print(solution(nn, startstart, endend, roadsrodasd, trapsasdas))
