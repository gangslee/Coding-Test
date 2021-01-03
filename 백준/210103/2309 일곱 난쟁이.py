import sys

n = list()

for _ in range(9):
    n.append(int(sys.stdin.readline()))

n.sort()

nineSum = sum(n)

# 앞서서 검사한 인덱스에 대해서는 검사하지 않는다.
for i in range(8):
    for j in range(i+1, 9):

        if nineSum-(n[i]+n[j]) == 100:
            result = [n[i], n[j]]
            n.remove(result[0])
            n.remove(result[1])

            for k in n:
                print(k)

            sys.exit()
