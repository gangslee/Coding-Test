def solution(info, query):
    import re
    answer = []
    for i in range(len(query)):
        q = query[i].replace('and', '', 3).replace('-', '', 4).split()
        cnt = 0
        print(q)
        for j in range(len(info)):
            plus = 1
            if int(q[len(q)-1]) > int(re.findall("\d+", info[j])[0]):
                continue
            else:
                for k in range(len(q)-1):
                    if q[k] not in info[j]:
                        plus = 0
                        break
            cnt += plus
        answer.append(cnt)
    return answer


infos = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
         "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
querys = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]

print(solution(infos, querys))
