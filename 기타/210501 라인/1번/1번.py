def solution(inputString):
    answer = 0
    open_word, close_word = ["(", "{", "[", "<"], [")", "}", "]", ">"]
    stack = []

    for i in range(len(inputString)):
        if inputString[i] in open_word:
            stack.append(inputString[i])

        elif inputString[i] in close_word:
            if len(stack) == 0:
                return -1*i
            else:
                current = stack.pop()

                if current == open_word[close_word.index(inputString[i])]:
                    answer += 1
                else:
                    return -1*i

    if len(stack) != 0:
        return -1*(len(inputString)-1)

    return answer


iss = "ABC)ABC"

print(solution(iss))
