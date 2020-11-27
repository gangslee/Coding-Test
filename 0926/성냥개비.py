def solution(k):
    from itertools import product
    matches = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    answer = 0
    zero = 0

    for i in range(1, int(k/2)+1):
        for j in product(matches, repeat=i):
            if sum(j) == k:
                if i > 1 and j[0] == 6 and zero == 2:
                    zero = 0
                else:
                    if i > 1 and j[0] == 6 and zero != 2:
                        zero += 1
                    answer += 1

    return answer


k = 5
print(solution(k))
