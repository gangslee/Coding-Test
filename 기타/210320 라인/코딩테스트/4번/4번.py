def props(d, data):
    current = d
    result = current[1]
    while True:
        idx = int(current[2])
        parent = data[idx].split()
        result = parent[1]+"/"+result
        if parent[2] == "0":
            break
        current = parent
    return result


def solution(data, word):
    answer = []
    table = [[] for _ in range(len(data))]

    for d in data:
        node = list(d.split())
        table[int(node[2])].append(node)

    leafParent = -1
    doll = list()

    for i in range(len(table)-1, -1, -1):
        if len(table[i]) > 0:
            if leafParent == -1:
                doll += table[i]
                leafParent = int(table[i][0][2])
            else:
                if i != leafParent:
                    doll += table[i]
                    break

    doll = sorted(doll, key=lambda x: (
        x[1] == word, x[1].find(word), -int(x[0])))

    for d in doll:
        answer.append(props(d, data))

    return answer


datata = ["1 BROWN 0", "2 CONY 0", "3 DOLL 1", "4 DOLL 2",
          "5 LARGE-BROWN 3", "6 SMALL-BROWN 3", "7 BLACK-CONY 4", "8 BROWN-CONY 4"]
wordword = "BROWN"
print(solution(datata, wordword))
