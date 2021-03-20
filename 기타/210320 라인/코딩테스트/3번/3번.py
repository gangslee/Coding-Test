def solution(enter, leave):
    answer = [0]*len(enter)

    for i in range(len(enter)):
        for j in range(i+1, len(enter)):
            pivots = sorted([enter.index(i+1), enter.index(j+1)])
            sliceEnter, sliceLeave = enter[pivots[1]:], leave[:leave.index(enter[pivots[0]])]

            for e in sliceEnter:
                if e in sliceLeave:
                    answer[i] += 1
                    answer[j] += 1
                    break

    return answer


enterenter = [1, 4, 2, 3]
leaveleavbe = [2, 1, 4, 3]
print(solution(enterenter, leaveleavbe))
