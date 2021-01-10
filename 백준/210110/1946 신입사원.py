import sys

t = int(sys.stdin.readline())

rank, case = [], []

for i in range(t):
    case.append(int(sys.stdin.readline()))
    temp = []

    for j in range(case[i]):
        temp.append(list(map(int, sys.stdin.readline().split())))
    temp.sort()  # 0번 인덱스 기준으로 정렬에서 저장
    rank.append(temp)

result = case

# 현재 최소값을 0번 리스트의 1번 인덱스로 설정
# 정렬이 되있기에 2번째 반복문에 1번 인덱스 검사시 새로운 현재 최소값보다 비교 값이 클 경우 제외 카운트 +1
for i in range(t):
    minValue = rank[i][0][1]
    for j in range(1, case[i]):
        if rank[i][j][1] > minValue:
            result[i] -= 1
        else:
            minValue = rank[i][j][1]
    print(result[i])
