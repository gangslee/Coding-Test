import sys

n, m = map(int, input().split())

frog_hobby = list()

for _ in range(n):
    frog_hobby.append(list(map(int, input().split())))

frog_flower = list()

for _ in range(n):
    frog_flower.append(list(map(int, input().split())))

home = list()

for _ in range(m):
    home.append(list(map(int, input().split())))

result = list()


def matchFrog(idx):
    if idx == n+1:
        print('YES')
        for num in result:
            print(num+1, end=" ")
        sys.exit(0)

    for i in range(n):    # n번째 집을 선호 하는지
        if idx in frog_flower[i] and i not in result:
            result.append(i)

            for j in range(m):  # 취미를 체크
                if home[j][0] != home[j][1]:
                    if idx == home[j][0] and idx > home[j][1] and frog_hobby[i][home[j][2]-1] != frog_hobby[result[home[j][1]-1]][home[j][2]-1]:
                        result.pop()
                        return

                    elif idx == home[j][1] and idx > home[j][0] and frog_hobby[i][home[j][2]-1] != frog_hobby[result[home[j][0]-1]][home[j][2]-1]:
                        result.pop()
                        return

            matchFrog(idx+1)


matchFrog(1)
print('NO')
