import sys

result = list()

while True:
    l, p, v = map(int, sys.stdin.readline().split())

    if l == 0 or p == 0 or v == 0:
        break

    camp = l*(v//p)
    if v % p < l:
        camp += v % p
    else:
        camp += l

    result.append(camp)

for i in range(len(result)):
    print("Case %d: %d" % (i+1, result[i]))
