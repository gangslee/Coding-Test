def solution(A, B):
    maxAnswer = int((A+B)/4)
    maxAB = max(A, B)
    minAB = A+B-maxAB

    while maxAnswer > 0:
        if (maxAB >= maxAnswer*4) or (maxAB >= maxAnswer*3 and minAB >= maxAnswer) or (maxAB >= maxAnswer*2 and minAB >= maxAnswer*2):
            return maxAnswer
        maxAnswer -= 1

    return 0
