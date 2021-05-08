def checkPartition(start, end, graph):
    minX, minY = min(start[0], end[0]), min(start[1], end[1])
    maxX, maxY = max(start[0], end[0]), max(start[1], end[1])

    for i in range(minX, maxX+1):
        for j in range(minY, maxY+1):
            if (i, j) == start or (i, j) == end:
                continue

            if graph[i][j] != 'X':
                return False
    return True


def solution(places):
    answer = [1]*5

    person = [[] for _ in range(len(places))]

    for i in range(len(places)):
        for j in range(len(places)):
            for k in range(len(places)):
                if places[i][j][k] == 'P':
                    person[i].append((j, k))

    for i in range(len(places)):
        for j in range(len(person[i])):
            for k in range(j+1, len(person[i])):
                md = abs(person[i][j][0] - person[i][k][0]) + \
                    abs(person[i][j][1] - person[i][k][1])

                if md == 1:
                    answer[i] = 0
                    break

                elif md == 2:
                    if not checkPartition(person[i][j], person[i][k], places[i]):
                        answer[i] = 0
                        break

            if answer[i] == 0:
                break

    return answer


pl = [["OPOOO", "POOOO", "OOOOO", "OOOOO", "POOOO"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
                                                                                                     "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(pl))
