def solution(s):
    answer = []

    for i in range(len(s)):
        current = s[i]

        if current not in answer:
            answer.append(current)

        substr = current

        for j in range(i+1, len(s)):
            if s[j] in substr:
                break

            substr += s[j]

            if substr not in answer:
                answer.append(substr)

    return len(answer)


ss = "zxzxz"
print(solution(ss))
