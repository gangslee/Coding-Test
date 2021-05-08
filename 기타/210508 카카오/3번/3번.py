def solution(n, k, cmd):
    answer = ['O']*n
    stack = []

    for c in cmd:
        if c == 'Z':
            idx = stack.pop()
            answer[idx] = 'O'

        elif c == 'C':
            answer[k] = 'X'

            stack.append(k)

            if k == n-1:
                for i in range(k-1, -1, -1):
                    if answer[i] == 'O':
                        k = i
                        break
            else:
                k += answer[k+1:].index('O')+1

        else:
            command = c.split()

            if command[0] == 'U':
                up_cnt = 0

                for i in range(int(command[1]), n):
                    up_cnt = answer[k-i:k].count('X')
                    if answer[k-(i+up_cnt)] == 'O':
                        k -= (i+up_cnt)
                        break

            else:
                for i in range(int(command[1]), n):
                    down_cnt = answer[k+1:k+i+1].count('X')
                    if answer[k+(i+down_cnt)] == 'O':
                        k += (i+down_cnt)
                        break

    return ''.join(answer)


nn = 8
kk = 2
cmdcmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]

print(solution(nn, kk, cmdcmd))
