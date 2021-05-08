numbers = ["zero", "one", "two", "three", "four",
           "five", "six", "seven", "eight", "nine"]
signs = ["plus", "minus"]


def stringToNum(strParam):
    result, current = "", ""

    for sp in strParam:
        current += sp

        if current in numbers:
            result += (str(numbers.index(current)))
            current = ""
        elif current in signs:
            if current == "plus":
                result += ' + '
            else:
                result += ' - '
            current = ""

    return result


def numToString(strParam):
    result = ""

    for sp in strParam:
        if sp == '-':
            result += "negative"
        else:
            result += numbers[int(sp)]

    return result


def StringChallenge(strParam):
    string = stringToNum(strParam).split()
    sumResult = int(string[0])
    isPlus = True

    for i in range(1, len(string)):
        if string[i] == '+':
            isPlus = True
        elif string[i] == '-':
            isPlus = False
        else:
            if isPlus:
                sumResult += int(string[i])
            else:
                sumResult -= int(string[i])

    result = numToString(str(sumResult))

    # code goes here
    return result


# keep this function call here
print(StringChallenge("onezeropluseight"))

# 문자열을 식으로 바꾸고 다시 문자로 바꾸기
