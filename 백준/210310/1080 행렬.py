# 풀이 참고 => https://m.blog.naver.com/PostView.nhn?blogId=pjok1122&logNo=221652193756&proxyReferer=https:%2F%2Fwww.google.com%2F

import sys

n, m = map(int, sys.stdin.readline().split())

A, B = [], []
result = 0

for i in range(n*2):
    if i < n:
        A.append(list(map(int, list(sys.stdin.readline().rstrip()))))
    else:
        B.append(list(map(int, list(sys.stdin.readline().rstrip()))))


def flip(x, y):
    for r in range(x, x+3):
        for c in range(y, y+3):
            A[r][c] = 1-A[r][c]


for i in range(n-2):
    for j in range(m-2):
        if A[i][j] != B[i][j]:
            flip(i, j)
            result += 1

if A == B:
    print(result)
else:
    print(-1)
