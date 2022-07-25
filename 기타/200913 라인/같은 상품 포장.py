def solution(boxes):
    answer = -1
    box = sum(boxes, [])
    s_box = set(box)
    answer = (len(box)-(len(box)-len(s_box))*2)/2
    return int(answer)


boxes = [[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]

print(solution(boxes))
