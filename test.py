########알몸으로 다니지 않는 경우를 빼 주면 됨 동전 뒤집기처럼 생각##############
######### EX : (hat1,hat2, 안입음)#############
###########각 종류별로 n+1을 모두 곱하고 모두 '안입음'이 나올 경우 하나를 빼주면 됨############

c = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
d = {}
for i in c:
    if i[1] in d.keys():
        d[i[1]] +=1
    else:
        d[i[1]] = 1
answer = 1
for i in d:
    answer*=d[i]+1

print(answer-1)