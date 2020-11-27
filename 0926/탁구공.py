def solution(n, p, c):
    answer, divide, day = 0, 0, 0

    for i in range(n):
        day += 1

        if p[i] >= c[i]:
            answer += (c[i]*100/2**divide)

            if divide > 0:
                divide = 0

            if not i == len(p)-1:
                p[i+1] += p[i]-c[i]

        else:
            divide += 1

            if divide == 3 or i == len(p)-1:
                break

            p[i+1] += p[i]

    return format(answer/day, '.2f')


n = 7
p = [6, 2, 1, 0, 2, 4, 3]
c = [3, 6, 6, 2, 3, 7, 6]

print(solution(n, p, c))
