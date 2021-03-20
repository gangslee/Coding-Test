upper = [chr(i) for i in range(65, 91)]
lower = [chr(i) for i in range(97, 123)]
num = [str(i) for i in range(0, 10)]
sc = ["~", "!", "@", "#", "$", "%", "^", "&", "*"]
allChr = upper+lower+num+sc
table = [upper, lower, num, sc]


def one(inp_str):
    if 8 <= len(inp_str) <= 15:
        return True
    else:
        return False


def two(inp_str):
    for s in inp_str:
        if s not in allChr:
            return False

    return True


def three(inp_str):
    result = [0]*4
    for s in inp_str:
        for i in range(len(table)):
            if result[i] == 1:
                continue
            if s in table[i]:
                result[i] = 1

        if sum(result) == 3:
            return True

    return False


def four(inp_str):
    for i in range(len(inp_str)-3):
        if inp_str[i] == inp_str[i+1] == inp_str[i+2] == inp_str[i+3]:
            return False
    return True


def five(inp_str):
    ch = []

    for s in inp_str:
        if s not in ch:
            if inp_str.count(s) >= 5:
                return False
            else:
                ch.append(s)

    return True


def solution(inp_str):
    answer = []

    if not one(inp_str):
        answer.append(1)

    if not two(inp_str):
        answer.append(2)

    if not three(inp_str):
        answer.append(3)

    if not four(inp_str):
        answer.append(4)

    if not five(inp_str):
        answer.append(5)

    if len(answer) == 0:
        answer.append(0)

    return answer


s = "ZzZz9Z824"
print(solution(s))
