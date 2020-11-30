n = int(input())

name = [input() for _ in range(n)]  # n만큼 입력받아 리스트를 생성

totalVote = []*1000

while True:
    temp = input()
    if len(temp) == 0:
        break
    vote = list(map(int, temp.split()))
    totalVote.append(vote)

exit(0)

totalVote.pop()

rank = {}


for i in range(len(totalVote)):
    if totalVote[i][0] not in rank:
        rank[totalVote[i][0]] = []
    rank[totalVote[i][0]].append(i)


while True:
    rank = sorted(rank.items(), key=lambda item: len(item[1]))

    if len(rank[-1][1]) > int(len(totalVote)/2):
        print(name[rank[0][0]-1])
        break

    else:
        minVote = list()

        for i in rank:
            if len(i[1]) > len(rank[0][1]):
                break
            minVote.append(i[0])

        rank = dict(rank)

        for i in minVote:
            if totalVote[i][1] in minVote:
                if totalVote[i][2] not in minVote:
                    rank[totalVote[i][2]].append(i)
            else:
                rank[totalVote[i][1]].append(i)

            del rank[i]
