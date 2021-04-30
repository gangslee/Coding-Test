import sys

n = int(sys.stdin.readline())

plus, minus = [], []
result = 0

for _ in range(n):
    current = int(sys.stdin.readline())

    if current == 1:
        result += 1

    elif current > 0:
        plus.append(current)

    else:
        minus.append(current)

plus.sort(reverse=True)
minus.sort()

for i in range(0, len(plus), 2):
    if i == len(plus)-1:
        result += plus[i]
    else:
        result += (plus[i]*plus[i+1])

for i in range(0, len(minus), 2):
    if i == len(minus)-1:
        result += minus[i]
    else:
        result += (minus[i]*minus[i+1])

print(result)
