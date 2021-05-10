def getResult(maps, x, y, r, p):
    result = 0

    for i in range(r):
        for j in range(r-i, r+i+2):
            power = p

            if j == (r-i) or j == (r+i+1):
                power /= 2

            if power >= maps[i+x][j+y]:
                print(maps[i+x][j+y], power)
                result += 1

    # for i in range(r-i, r+i+2):
    #     for j in range(r):
    #         power = p

    #         if j == (r-i) or j == (r+i+1):
    #             power /= 2

    #         if power >= maps[i-x+r][j-y+r]:
    #             result += 1

    return result


def solution(maps, p, r):
    answer = 0

    for i in range(len(maps) - r):
        for j in range(len(maps) - r):
            answer = max(answer, getResult(maps, i, j, r//2, p))

    return answer


mm = [[1, 28, 41, 22, 25, 79, 4], [39, 20, 10, 17, 19, 18, 8], [21, 4, 13, 12, 9, 29, 19], [
    58, 1, 20, 5, 8, 16, 9], [5, 6, 15, 2, 39, 8, 29], [39, 7, 17, 5, 4, 49, 5], [74, 46, 8, 11, 25, 2, 11]]

pp = 19

rr = 6

print(solution(mm, pp, rr))
