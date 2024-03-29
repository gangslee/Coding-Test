import sys

N, M = map(int, sys.stdin.readline().split())
graph = list()

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

block = [[[0, 1], [0, 2], [0, 3]], [[1, 0], [2, 0], [3, 0]],
         [[0, 1], [1, 0], [1, 1]], [[1, 0], [2, 0], [2, 1]],
         [[1, 0], [2, 0], [2, -1]], [[0, 1], [0, 2], [1, 0]],
         [[0, 1], [0, 2], [1, 2]], [[0, 1], [1, 1], [2, 1]],
         [[0, 1], [1, 0], [2, 0]], [[0, 1], [0, 2], [-1, 2]],
         [[1, 0], [1, 1], [1, 2]], [[1, 0], [1, 1], [2, 1]],
         [[1, 0], [1, -1], [2, -1]], [[0, 1], [-1, 1], [-1, 2]],
         [[0, 1], [1, 1], [1, 2]], [[0, 1], [0, 2], [1, 1]],
         [[1, 0], [1, 1], [2, 0]], [[1, 0], [1, -1], [2, 0]],
         [[0, 1], [0, 2], [-1, 1]]]

result = 0

for i in range(N):
    for j in range(M):
        for b in block:
            try:
                current = graph[i][j]+graph[i+b[0][0]][j+b[0][1]] + \
                    graph[i+b[1][0]][j+b[1][1]]+graph[i+b[2][0]][j+b[2][1]]
            except:
                current = 0

            result = max(current, result)

print(result)
