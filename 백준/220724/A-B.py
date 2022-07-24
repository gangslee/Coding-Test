from re import L


A, B = map(int, input().split())

if B % 2 == 1 and B % 10 != 1:
    print(-1)
    exit()

result = 1

while True:
    if B % 10 == 1:
        B = (B-1)//10
    elif B % 2 == 0:
        B = B//2
    else:
        result = -1
        break

    result += 1

    if A == B:
        break
    elif A > B:
        result = -1
        break

print(result)
