import sys
import collections

n = int(sys.stdin.readline())
times = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
times = sorted(times, key=lambda x: [x[1], x[0]])
cnt, start = 0, 0

for time in times:
    if time[0]>=start:
        start = time[1]
        cnt+=1

print(cnt)