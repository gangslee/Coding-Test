import sys

S = int(sys.stdin.readline())
N, result = 0, 1

while N < S:
    result += 1
    N += result


print(result-1)
