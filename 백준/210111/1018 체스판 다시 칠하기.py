import sys

n, m = map(int, sys.stdin.readline().split())

chess = list()

answer = n*m

for _ in range(n):
    chess.append(sys.stdin.readline())


def solution(square):
    result = [0, 0]

    for i in range(8):
        for j in range(8):
            if ((i+j) % 2 == 0 and square[i][j] == 'B') or ((i+j) % 2 == 1 and square[i][j] == 'W'):
                continue
            result[0] += 1

    for i in range(8):
        for j in range(8):
            if ((i+j) % 2 == 0 and square[i][j] == 'W') or ((i+j) % 2 == 1 and square[i][j] == 'B'):
                continue
            result[1] += 1

    return min(result)


for i in range(n-7):
    for j in range(m-7):
        # 2차원 리스트에서 새로운 부분 2차원 리스트를 빼내는 방법
        c = [chess[i+x][j:j+8] for x in range(8)]
        answer = min(solution(c), answer)

print(answer)
