def solution(s):
    answer = 0

    word_string = ["zero", "one", "two", "three",
                   "four", "five", "six", "seven", "eight", "nine"]
    current = ""

    for i in s:
        if 48 <= ord(i) <= 57:
            answer *= 10
            answer += int(i)
        else:
            current += i

            if current in word_string:
                answer *= 10
                answer += word_string.index(current)
                current = ""

    return answer


ss = "onezerozerozero"

print(solution(ss))
