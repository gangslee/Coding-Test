def solution(n, edges):
    answer = []
    counter = {}
    center = []
    side = []

    for i in range(len(edges)):
        for j in range(2):
            if edges[i][j] not in counter:
                counter[edges[i][j]] = 1
            else:
                counter[edges[i][j]] += 1

                if counter[edges[i][j]] == n/3-1:
                    if counter[edges[i][j]] == n/3:
                        center.append(edges[i][j])
                    else:
                        side.append(edges[i][j])
    print(center, side)
    for i in center:
        for j in side:

            if [i, j] in edges:

                answer.append(edges.index([i, j]))
            if [j, i] in edges:
                answer.append(edges.index([j, i]))

    answer.sort()
    return answer


n = 9
edges = [[0, 2], [2, 1], [2, 4], [3, 5], [5, 4], [5, 7], [7, 6], [6, 8]]
print(solution(n, edges))
