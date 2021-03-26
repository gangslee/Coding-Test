def solution(N, coffee_times):
    answer = []
    machine = [0]*N
    sec = 0
    i = 0

    while machine:
        sec = min(machine)
        machine.remove(sec)

        if sec != 0:
            currentIdx = coffee_times.index(sec)
            answer.append(currentIdx+1)
            coffee_times[currentIdx] = -1

        if i < len(coffee_times):
            coffee_times[i] += sec
            machine.append(coffee_times[i])
            i += 1

    return answer


nn = 1
ct = [100, 1, 50, 1, 1]
print(solution(nn, ct))
