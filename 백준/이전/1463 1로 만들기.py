import sys

n, cnt = int(sys.stdin.readline()), 0
result = [n]

def cal(l):
    lst = []
    for i in l:
        lst.append(i-1)
        if i%3==0:
            lst.append(i/3)
        if i%2==0:
            lst.append(i/2)
    lst = set(lst)
    lst = list(lst) #set은 중복을 불허해서 필요 없으면 set햇다 list화시키는 방법이있음
    print(lst)
    return lst

while True:
    if n==1:
        break
    temp, result = result, []
    result = cal(temp)
    cnt+=1
    if 1 in result:
        break

print(cnt)