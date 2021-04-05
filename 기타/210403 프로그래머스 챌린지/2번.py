def setGraph(g, a, b, c, d):
    leftTop = g[a][b]

    for i in range(a+1, c+1):
        g[i-1][b] = g[i][b]

    for i in range(b+1, d+1):
        g[c][i-1] = g[c][i]

    for i in range(c-1, a-1, -1):
        g[i+1][d] = g[i][d]

    for i in range(d-1, b, -1):
        g[a][i+1] = g[a][i+1]

    g[a][b+1] = leftTop

    return g


def getMin(g, a, b, c, d):

    result = list()

    for i in range(b, d):
        result.append(g[a][i])

    for i in range(a, c):
        result.append(g[i][d])

    for i in range(b+1, d+1):
        result.append(g[c][i])

    for i in range(a+1, c+1):
        result.append(g[i][b])

    return min(result)


def solution(rows, columns, queries):
    graph = [[(i*columns)+j for j in range(1, columns+1)]
             for i in range(0, rows)]

    answer = []

    for i in range(len(queries)):
        answer.append(
            getMin(graph, queries[i][0]-1, queries[i][1]-1, queries[i][2]-1, queries[i][3]-1))

        if i == len(queries)-1:
            break

        graph = setGraph(
            graph, queries[i][0]-1, queries[i][1]-1, queries[i][2]-1, queries[i][3]-1)

    return answer


rs, cs = 6, 6
qs = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]
print(solution(rs, cs, qs))
