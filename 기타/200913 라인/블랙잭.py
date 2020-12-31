def solution(cards):
    answer = 0

    from collections import deque
    cards = deque(cards)
    result = deque([])
    idx = 0
    while len(cards) > 0:
        if idx < 4:
            if cards[0] >= 10:
                result.append(10)
            elif cards[0] == 1:
                if idx < 2:
                    result.append(11)
                else:
                    if result[idx-2] == 11:
                        result.append(1)
                    else:
                        result.append(result[idx-2])
                        result[idx-2] = 11
            else:
                result.append(cards[0])

        else:
            if result[0]+result[2] == 21:
                if result[1]+result[3] != 21:
                    answer += 3
                idx = 0
                result.clear()
            elif result[0]+result[2] > 21:
                answer -= 2
                idx = 0
                result.clear()
            else:
                if (result[1] == 1 or result[1] >= 7) and (result[0]+result[2] < 17):
                    if cards[0] >= 10:
                        result[2] += 10
                    elif cards[0] == 1:
                        if result[0]+result[2] <= 10:
                            result[2] += 11
                        else:
                            result[2] += 1
                    else:
                        print(1)
                        result[2] += cards[0]
                elif (2 <= result[1] <= 3) and (result[0]+result[2] < 12):
                    if cards[0] >= 10:
                        result[2] += 10
                    elif cards[0] == 1:
                        if result[0]+result[2] <= 10:
                            result[2] += 11
                        else:
                            result[2] += 1
                    else:
                        result[2] += cards[0]
                else:
                    if result[1]+result[3] < 17:
                        if cards[0] >= 10:
                            result[3] += 10
                        elif cards[0] == 1:
                            if result[1]+result[3] <= 10:
                                result[3] += 11
                            else:
                                result[3] += 1
                        else:
                            result[3] += cards[0]

                    if result[1]+result[3] > 21:
                        answer += 2
                        idx = 0
                        result.clear()
                    elif result[1]+result[3] == 21:
                        answer -= 2
                        idx = 0
                        result.clear()
                    else:
                        if result[0]+result[2] > result[1]+result[3]:
                            answer += 2
                        elif result[0]+result[2] < result[1]+result[3]:
                            answer -= 2
                        idx = 0
                        result.clear()
        cards.popleft()
        idx += 1
        print(result)
    return answer


cards = [1, 4, 10, 6, 9, 1, 8, 13]
print(solution(cards))
