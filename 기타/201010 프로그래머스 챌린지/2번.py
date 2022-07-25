
def solution(n, k):
    answer = 1
    while 0 < n < k:
        k -= n
        n -= 1
        answer += 1
    if n == 0:
        answer = -1
    return answer


print(solution(10, 5))
