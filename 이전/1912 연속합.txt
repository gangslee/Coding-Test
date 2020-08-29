import sys

n = int(sys.stdin.readline())
result = list(map(int, sys.stdin.readline().split()))



for i in range(1, n):
    result[i] = max(result[i-1]+result[i], result[i])

print(max(result))