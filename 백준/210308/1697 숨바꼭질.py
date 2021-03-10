import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

graph = [100001]*(100001)


def search(start, end):
    graph[start] = 0

    q = deque([(start, 0)])

    while q:
        current = q.popleft()

        if 0 <= current[0]-1 <= 100000 and current[1]+1 < graph[current[0]-1]:
            graph[current[0]-1] = current[1]+1
            q.append((current[0]-1, current[1]+1))

        if 0 <= current[0]+1 <= 100000 and current[1]+1 < graph[current[0]+1]:
            graph[current[0]+1] = current[1]+1
            q.append((current[0]+1, current[1]+1))

        if 0 <= current[0]*2 <= 100000 and current[1]+1 < graph[current[0]*2]:
            graph[current[0]*2] = current[1]+1
            q.append((current[0]*2, current[1]+1))


search(n, k)
print(graph[k])
