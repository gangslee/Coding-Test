def solution(n, delivery):
    answer = ['?']*n
    delivery = sorted(delivery, key=lambda x: -x[2])

    for i in delivery:
        if i[2] == 1:
            answer[i[0]-1] = 'O'
            answer[i[1]-1] = 'O'
        else:
            if answer[i[0]-1] == 'O':
                answer[i[1]-1] = 'X'
            elif answer[i[1]-1] == 'O':
                answer[i[0]-1] = 'X'

    return "".join(answer)


delivery = [[5, 6, 0], [1, 3, 1], [1, 5, 0], [7, 6, 0], [3, 7, 1], [2, 5, 0]]
n = 7
print(solution(n, delivery))
