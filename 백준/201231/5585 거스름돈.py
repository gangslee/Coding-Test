import sys

n = int(sys.stdin.readline())

rest = 1000-n

coin = [500, 100, 50, 10, 5, 1]

result = 0

for i in coin:
    if rest >= i:
        result += rest//i
        rest = rest % i


print(result)
