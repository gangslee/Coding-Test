progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]


def solution(progresses, speeds):

    remain = []
    for i in range(len(progresses)):
        day = int((100-progresses[i]) / speeds[i])
        if (100-progresses[i]) % speeds[i] != 0:
            day += 1
        remain.append(day)

    idx = 0
    answer = [1]
    for i in range(1, len(remain)):
        if remain[idx] < remain[i]:
            answer.append(1)
            idx = i
        else:
            answer[len(answer)-1] += 1

    return answer


print(solution(progresses, speeds))
