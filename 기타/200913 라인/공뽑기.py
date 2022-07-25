def solution(ball, order):
    from collections import deque
    ball = deque(ball)
    order = deque(order)
    answer = deque([])
    temp = deque([])

    while len(ball) > 0:
        if order[0] == ball[0] or order[0] == ball[len(ball)-1]:
            if order[0] == ball[0]:
                ball.popleft()

            elif order[0] == ball[len(ball)-1]:
                ball.pop()

            answer.append(order.popleft())

            if len(temp) > 0:
                temp.reverse()
                order.extendleft(temp)
                temp.clear()
        else:
            temp.append(order.popleft())

    return list(answer)


ball = [1, 2, 3, 4, 5, 6]
order = [6, 2, 5, 1, 4, 3]


print(solution(ball, order))
