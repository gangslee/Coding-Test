import heapq

n, k = map(int, input().split())
jewel, bag, temp = [], [], []
result = 0

for _ in range(n):
    jewel.append(list(map(int, input().split())))

for _ in range(k):
    bag.append(int(input()))

# jewel.sort()
bag.sort()

for b in bag:
    while jewel and b >= jewel[0][0]:
        heapq.heappush(temp, -jewel[0][1])
        heapq.heappop(jewel)

    if temp:
        result += heapq.heappop(temp)
    elif not jewel:
        break

print(-result)
