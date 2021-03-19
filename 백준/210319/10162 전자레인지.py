import sys

T = int(sys.stdin.readline())

if T % 10 != 0:
    print(-1)
    exit()

sec = [300, 60, 10]
result = list()

for s in sec:
    result.append(T//s)
    T = T % s

for r in result:
    print(r, end=" ")
