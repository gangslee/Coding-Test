import sys
from collections import deque

N = int(sys.stdin.readline())
pizza = list(map(int, sys.stdin.readline().split()))
result = [0] * N
q = deque()

for i in range(N):
    q.append([i, 0])

cnt = 0

while q:
    idx, p = q.popleft()
    cnt += 1
    p += 1

    if pizza[idx] == p:
        result[idx] = cnt
    else:
        q.append([idx, p])


result = map(str, result)
print(' '.join(result))
