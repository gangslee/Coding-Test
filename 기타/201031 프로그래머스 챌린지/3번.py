def solution(v):
    answer = [0, 0, 0]
    global gv
    gv = v

    for i in range(len(gv)):
        for j in range(len(gv)):
            if gv[i][j] < 3:
                answer[gv[i][j]] += 1
                checkVisit(i, j, len(gv))

    return answer


def checkVisit(i, j, length):
    global gv
    gv[i][j] += 3
    if i > 0 and gv[i][j] % 3 == gv[i-1][j] % 3 and gv[i-1][j] < 3:
        checkVisit(i-1, j, length)
    if j > 0 and gv[i][j] % 3 == gv[i][j-1] % 3 and gv[i][j-1] < 3:
        checkVisit(i, j-1, length)
    if i < len(gv)-1 and gv[i][j] % 3 == gv[i+1][j] % 3 and gv[i+1][j] < 3:
        checkVisit(i+1, j, length)
    if j < len(gv)-1 and gv[i][j] % 3 == gv[i][j+1] % 3 and gv[i][j+1] < 3:
        checkVisit(i, j+1, length)


print(solution([[0, 0, 1], [2, 2, 1], [0, 0, 0]]))
