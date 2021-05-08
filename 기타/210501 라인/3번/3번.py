def solution(ads):
    answer = 0
    ad_time = 0

    ads = sorted(ads, key=lambda x: -x[0])

    while ads:
        last = ads[-1][0]

        if last > ad_time:
            ad_time = last
            ads.pop()

        else:
            next_add = [-1, -1]
            for i in range(len(ads)-1, -1, -1):
                if ads[i][0] > ad_time:
                    break

                if ads[i][1] > next_add[1]:
                    next_add = ads[i]

            answer += (ad_time-next_add[0])*next_add[1]
            ads.remove(next_add)

        ad_time += 5

    return answer


a = [[1, 3], [3, 2], [5, 4]]

print(solution(a))
