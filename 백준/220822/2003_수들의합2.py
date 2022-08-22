n, m = map(int, input().split())
a = list(map(int, input().split()))

result = 0

for i in range(len(a)):
    current = a[i]

    if current == m:
        result += 1
        continue

    for j in range(i+1, len(a)):
        if current + a[j] < m:
            current += a[j]
        else:
            if current + a[j] == m:
                result += 1
            break

print(result)
