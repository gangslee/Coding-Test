# import sys
# import copy
# from collections import deque

# n, m = map(int, sys.stdin.readline().split())

# lab = list()
# virus = list()
# direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
# result = 0

# for i in range(n):
#     line = list(map(int, sys.stdin.readline().split()))

#     for j in range(len(line)):
#         if line[j] == 2:
#             virus.append((i, j))

#     lab.append(line)


# def bfs(r, c):
#     q = deque([(r, c)])

#     while q:
#         current = q.popleft()

#         for d in direction:
#             nr, nc = current[0]+d[0], current[1]+d[1]

#             if -1 < nr < n and -1 < nc < m and newLab[nr][nc] == 0 and not visit[nr][nc]:
#                 visit[nr][nc] = True
#                 newLab[nr][nc] = 2
#                 q.append((nr, nc))


# wall = [-1, -1, -1]

# for i in range(n*m):
#     if lab[i//m][i % m] != 0:
#         continue
#     wall[0] = i
#     for j in range(i+1, n*m):
#         if lab[j//m][j % m] != 0:
#             continue
#         wall[0] = j
#         for k in range(j+1, n*m):

#             if lab[k//m][k % m] == 0:
#                 wall[2] = k

#                 if -1 not in wall:
#                     newLab = copy.deepcopy(lab)

#                     for w in wall:
#                         newLab[w//m][w % m] = 1

#                     visit = [[False for __ in range(m)] for _ in range(n)]

#                     for v in virus:
#                         bfs(v[0], v[1])

#                     nv = 0

#                     for nl in newLab:
#                         nv += nl.count(0)

#                     result = max(result, nv)


# print(result)


import sys
import copy
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0


def bfs():
    global ans
    w = copy.deepcopy(a)
    for i in range(n):
        for j in range(m):
            if w[i][j] == 2:
                q.append([i, j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if w[nx][ny] == 0:
                    w[nx][ny] = 2
                    q.append([nx, ny])

    cnt = 0
    for i in w:
        cnt += i.count(0)
    ans = max(ans, cnt)


def wall(x):
    if x == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                a[i][j] = 1
                wall(x+1)
                a[i][j] = 0


n, m = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
q = deque()
wall(0)
print(ans)

# 미해결 pypy3로 제출 다른분 코드 참고
