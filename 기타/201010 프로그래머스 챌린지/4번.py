def solution(S, C):
    answer = 0
    current = ''
    maxIdx = -1

    for i in range(0, len(S)):
        if S[i] == current:
            if C[i] > maxIdx:
                answer += maxIdx
                maxIdx = C[i]
            else:
                answer += C[i]

        else:
            current = S[i]
            maxIdx = C[i]

    return answer
