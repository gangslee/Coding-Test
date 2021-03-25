# 주어진 program과 command에 있는 program의 일치 여부를 확인하는 함수
def chkProgram(program, programPart):
    if program == programPart:
        return True
    else:
        return False

# 주어진 flag_rule에 대해 command가 규칙을 잘 이행하고 있는지 확인하는 함수


def chkRules(rules, rulePart):

    # flag_name의 종류, flag_argument_type의 종류를 각각 담는 리스트들
    flagList, argumentTypeList = list(), list()

    # flag_rules의 모든 규칙들에 대해 각 규칙의 flag_name과 flag_argument_type을 분리하는 작업
    for r in rules:
        flag, argumentType = r.split()
        flagList.append(flag)
        argumentTypeList.append(argumentType)

    # 각 flag_name 별로 command가 규칙을 잘 이행하는 지 여부를 확인
    for i in range(len(flagList)):
        # 현재 검사중인 flag_name이 command에 존재하지 않을 경우를 파악
        if flagList[i] not in rulePart:
            return False

        # command내 현재 검사중인 flag_name의 flag_argument_type의 위치(인덱스)를 확인
        argIdx = rulePart.index(flagList[i])+1

        # flag_argument_type이 NULL일 경우 command의 맨 마지막에 위치하거나 해당 flag_name의 다음 인덱스에 다른 flag_name이 위치하는지를 파악하여 flag argument를 받지 않는 규칙 이행 여부 확인
        if argumentTypeList[i] == "NULL":
            if argIdx < len(rulePart) and rulePart[argIdx] not in flagList:
                return False

        # flag_argument_type이 STRING이나 NUMBER, STRIGS, NUMBERS일 경우 command의 맨 마지막에 위치하지 않거나 해당 flag_name의 다음 인덱스에 다른 flag_name이 위치하지 않는지를 파악하여 flag argument 받는지 규칙 이행 여부 확인
        elif argumentTypeList[i] == "STRING" or argumentTypeList[i] == "NUMBER" or argumentTypeList[i] == "STRING" or argumentTypeList[i] == "NUMBERS":
            if argIdx == len(rulePart) or rulePart[argIdx] in flagList:
                return False

            # 현재 flag_argument들을 담을 변수
            currentArgument = rulePart[argIdx]

            # flag_argument_type이 STRING의 경우 flag_argument가 알파벳 대소문자로만 이루어져야 하는 규칙 이행 여부 파악
            if argumentTypeList[i] == "STRING":
                for c in currentArgument:
                    if not ('a' <= c <= 'z' or "A" <= c <= "Z"):
                        return False

            # flag_argument_type이 NUMBER 경우 flag_argument가 0부터 9까지의 숫자로만 이루어져야 하는 규칙 이행 여부 파악
            if argumentTypeList[i] == "NUMBER":
                for c in currentArgument:
                    if not ('0' <= c <= '9'):
                        return False

    return True  # 위 조건들을 모두 통과할 시 (규칙을 이행할 시) True를 반환


def solution(program, flag_rules, commands):
    answer = [True]*len(commands)

    for i in range(len(commands)):
        commandLine = list(commands[i].split())

        # 주어진 program과 command에 있는 program의 일치 여부를 확인
        if not chkProgram(program, commandLine.pop(0)):
            answer[i] = False
            continue

        # command가 주어진 flag_rule을 잘 이행하고 있는지 여부 확인
        if not chkRules(flag_rules, commandLine):
            answer[i] = False
            continue

    return answer


pp = "trip"
frfr = ["-days NUMBERS", "-dest STRING"]
comm = ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]
print(solution(pp, frfr, comm))
