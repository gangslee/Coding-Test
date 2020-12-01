def solution(n):
    temp = n
    n = str(n)

    while temp >= 10:
        temp = getSum(str(temp))

    answer = [len(n)-1, temp]
    return answer


def getSum(n):
    return sum(map(int, n))
