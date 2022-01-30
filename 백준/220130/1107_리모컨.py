n = int(input())
ans = abs(100 - n)
m = int(input())
if m:
    broken = set(input().split())
else:
    broken = set()

for num in range(1000001):
    for N in str(num):
        if N in broken:
            break
    else:
        ans = min(ans, len(str(num)) + abs(num - n))

print(ans)
