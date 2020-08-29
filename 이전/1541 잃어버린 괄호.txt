########캐스팅 하는데 시간이 걸려서 틀린듯########
########캐스팅 int 맨앞 자리가 0이면 무시하고 해줌########

import sys

n = sys.stdin.readline().rstrip().split('-')
num = []

for i in n:
    temp = i.split('+')
    cnt = 0
    for j in temp:
        cnt += int(j)
    num.append(cnt)

result = num[0]

for i in range(1,len(num)):
    result-=num[i]

print(result)