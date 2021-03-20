def solution(table, languages, preference):
    table = [list(table[i].split()) for i in range(len(table))]
    table = sorted(table, key=lambda x: x[0])
    result = [0 for _ in range(len(table))]

    for i in range(len(table)):
        for j in range(len(languages)):
            if languages[j] in table[i]:
                result[i] += (preference[j] *
                              (len(table)-table[i].index(languages[j])-1))

    answer = table[result.index(max(result))][0]

    return answer


tt = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
      "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
ll = ["JAVA", "JAVASCRIPT"]
pp = [7, 5]

print(solution(tt, ll, pp))
