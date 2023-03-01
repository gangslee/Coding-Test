while True:
    str = input()

    if str == "#":
        break

    print(str[0], (str[2:].count(str[0]) + str[2:].count(str[0].upper())))
