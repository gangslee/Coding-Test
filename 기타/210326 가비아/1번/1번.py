import time
import math


def solution(n):
    answer = 0
    cnt = 1

    while n >= 5**cnt:
        answer += (n//5**cnt)
        cnt += 1

    return answer


num = 25
print(solution(num))
