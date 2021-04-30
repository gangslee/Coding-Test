from itertools import permutations
import sys

n = int(sys.stdin.readline())
result = 0

numbers = list(map(int, sys.stdin.readline().split()))

cases = permutations(numbers)

for c in cases:
    current = 0
    for i in range(1, len(c)):
        current += abs(c[i]-c[i-1])

    result = max(result, current)

print(result)
