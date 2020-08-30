def solution(c):
    d = {}
    for i in c:
        if i[1] in d.keys():
            d[i[1]] +=1
        else:
            d[i[1]] = 1
    answer = 1
    for i in d:
        answer*=d[i]+1
    
    return answer-1