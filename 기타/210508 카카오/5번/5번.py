def dfs(start, result, links):
    for l in links:
        if start in l:


def solution(k, num, links):

    if k == 1:
        return sum(num)

    answer = 0

    for i in range(k-1):
        maxIdx = num.index(max(num))
        dfs(maxIdx, 0, links)

    return answer


kk = 3
nummm = [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1]
linksss = [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5],
           [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]

print(solution(kk, nummm, linksss))
