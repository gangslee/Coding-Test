import sys

n = int(sys.stdin.readline())

result = n

# 99까지는 무조건 한수여서 100부터 검사
for i in range(100, n+1):
    num = str(i)
    temp = int(num[0]) - int(num[1])

    for j in range(1, len(num)-1):
        if int(num[j]) - int(num[j+1]) != temp:
            result -= 1
            break

print(result)
