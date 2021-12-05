import sys

n = sys.stdin.readline().rstrip()

if not ('0' in n):
    print(-1)
    exit()

n = int("".join(sorted(list(n), reverse=True)))

if n % 3 == 0:
    print(n)
else:
    print(-1)
