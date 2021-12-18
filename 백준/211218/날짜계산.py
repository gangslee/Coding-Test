import sys

E, S, M = map(int, sys.stdin.readline().split())
maxNum = 15*28*19

for i in range(max((E, S, M)), maxNum+1):
    if (i-E) % 15 == 0 and (i-S) % 28 == 0 and (i-M) % 19 == 0:
        print(i)
        exit()
