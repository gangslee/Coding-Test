import sys

n = int(sys.stdin.readline())

k = list()

result = 0

for _ in range(n):
    k.append(int(sys.stdin.readline()))

k.sort(reverse=True)

for i in range(len(k)):
    k[i] *= (i+1)

print(max(k))
