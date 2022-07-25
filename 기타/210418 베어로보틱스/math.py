def MathChallenge(strParam):
    words = strParam.split()
    stack = list()

    for w in words:
        if w == '+':
            x, y = stack.pop(), stack.pop()
            stack.append(x+y)
        elif w == '-':
            x, y = stack.pop(), stack.pop()
            stack.append(x-y)
        elif w == '*':
            x, y = stack.pop(), stack.pop()
            stack.append(x*y)
        elif w == '/':
            x, y = stack.pop(), stack.pop()
            stack.append(x//y)
        else:
            stack.append(int(w))

    return stack[0]


sp = "4 5 + 2 1 + *"
print(MathChallenge(sp))

# 참고 : https://comdoc.tistory.com/entry/12-%ED%9B%84%EC%9C%84-%ED%91%9C%EA%B8%B0%EB%B2%95%EA%B3%BC-%EC%8A%A4%ED%83%9D-%ED%8C%8C%EC%9D%B4%EC%8D%AC
