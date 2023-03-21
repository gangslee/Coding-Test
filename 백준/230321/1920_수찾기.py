import sys

n = int(sys.stdin.readline())
a = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

for num in nums:
    print(1) if num in a else print(0)
