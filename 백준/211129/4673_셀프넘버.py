n = [1]*10001
n[0] = 0

for i in range(1, 10001):
    result, temp = i, i

    while temp > 0:
        result += (temp % 10)
        temp //= 10

    if(result <= 10000):
        n[result] = 0

for i in range(1, 10001):
    if n[i] == 0:
        continue
    print(i)
