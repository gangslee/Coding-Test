

genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]

# dic = {}

# for i in range(len(plays)):
#     if genres[i] in dic.keys():
#         dic[genres[i]][0] += plays[i]
#         if len(dic[genres[i]]) == 2:
#             if plays[i] > plays[dic[genres[i]][1]]:
#                 dic[genres[i]].append(dic[genres[i]][1])
#                 dic[genres[i]][1] = i
#             else:
#                 dic[genres[i]].append(i)
#         else:
#             if plays[i] > plays[dic[genres[i]][1]]:
#                 dic[genres[i]][2] = dic[genres[i]][1]
#                 dic[genres[i]][1] = i
#             elif plays[dic[genres[i]][1]] >= plays[i] > plays[dic[genres[i]][2]]:
#                 dic[genres[i]][2] = i
#     else:
#         dic[genres[i]] = [plays[i], i]

# dic = sorted(dic.items(), key=lambda x: x[0], reverse=True)

# answer = []
# for key, value in dic:
#     answer.append(value[1])
#     answer.append(value[2])
# print(answer)

answer = []
d = {e: [] for e in set(genres)}
for e in zip(genres, plays, range(len(plays))):
    # {'classic': [[500, 0], [150, 2], [800, 3]], 'pop': [[600, 1], [2500, 4]]} 형태로 변형
    d[e[0]].append([e[1], e[2]])
genreSort = sorted(list(d.keys()), key=lambda x: sum(
    map(lambda y: y[0], d[x])), reverse=True)
# d의 키들에 대해 총합을 바탕으로 정렬

for g in genreSort:
    temp = [e[1]
            for e in sorted(d[g], key=lambda x: (x[0], -x[1]), reverse=True)]
    # 장르별 정렬 후 index 값을 temp에 넣음

    answer += temp[:min(len(temp), 2)]
    # temp의 길이 혹은 최소단위 2로 슬라이싱 후 결과물에 추가
print(answer)
