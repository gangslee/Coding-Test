N = int(input())

cycle = 0
current = N

while True:
    if current < 10:
        current *= 11
    else:
        current = (current % 10)*10 + ((current//10) + (current % 10)) % 10

    cycle += 1

    if current == N:
        break

print(cycle)
