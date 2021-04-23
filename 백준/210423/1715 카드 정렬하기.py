import sys
import heapq    # 우선순위 큐 라이브러리

n = int(sys.stdin.readline())
card = []

for _ in range(n):
    card.append(int(sys.stdin.readline()))

heapq.heapify(card)
result = 0

while len(card) > 1:
    a, b = heapq.heappop(card), heapq.heappop(card)
    result += (a+b)
    heapq.heappush(card, a+b)


print(result)

# n=10, card가 다 10일 때
# (10 + 10) + (20 + 10) + (30 + 10) ... + (90 + 10) = 100 * 4 + 50 + 90 = 540 이 아니라
# (10 + 10) + (10 + 10) + (10 + 10) + (10 + 10) + (10 + 10) 임
