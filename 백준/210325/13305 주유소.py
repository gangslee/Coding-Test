import sys

N = int(sys.stdin.readline())
road = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

result = road[0]*price[0]
current = price[0]

for i in range(1, len(road)):
    current = min(current, price[i])
    result += (road[i]*current)

print(result)
