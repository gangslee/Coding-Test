def solution(orders, course):
    answer = []
    from itertools import combinations

    for i in course:
        d = {}
        idx = 1
        for j in orders:
            temp = list(j)
            temp.sort()
            for k in list(combinations(temp, i)):

                if k not in d.keys():
                    d[k] = 1
                else:
                    d[k] = d[k]+1

        l = sorted(d.items(), reverse=True, key=lambda item: (item[1]))

        if len(l) > 0 and l[0][1] > 1:
            temp = l[0][1]
            answer.append(''.join(l[0][0]))

            if len(l) > 1:
                while True:
                    if l[idx][1] < temp:
                        break
                    answer.append(''.join(l[idx][0]))
                    idx += 1
    answer.sort()
    return answer
