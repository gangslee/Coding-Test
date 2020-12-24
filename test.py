pan = list()
for _ in range(10):
    pan.append(list(map(int, input().split())))

x, y = 1, 1

while True:
    pan[x][y] += 9

    if pan[x][y] == 11:
        pan[x][y] -= 2
        break

    if pan[x+1][y] == 1 and pan[x][y+1] == 1:
        break

    if pan[x][y+1] == 1:
        x += 1
    else:
        y += 1

for i in pan:
    print(*i, end=" ")
    print()
