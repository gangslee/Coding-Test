bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]


def solution(bridge_length, weight, truck_weights):
    q = [0]*bridge_length
    sec = 0
    temp = 0
    while q:
        sec += 1
        temp -= q.pop(0)
        if truck_weights:
            if temp+truck_weights[0] <= weight:
                temp += truck_weights[0]
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return sec


print(solution(bridge_length, weight, truck_weights))

# list sum 속도 ㅈㄴ느림
