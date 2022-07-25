def solution(lottos, win_nums):
    rank = [6, 5, 4, 3, 2]
    cnt = 0

    for l in lottos:
        if l in win_nums:
            cnt += 1

    plus = lottos.count(0)

    answer = [cnt+plus, cnt]

    for i in range(len(answer)):
        if answer[i] not in rank:
            answer[i] = 6
        else:
            answer[i] = rank.index(answer[i])+1

    return answer


lo = [44, 1, 0, 0, 31, 25]
wn = [31, 10, 45, 1, 6, 19]

print(solution(lo, wn))
