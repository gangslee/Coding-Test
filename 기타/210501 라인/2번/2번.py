# def solution(array):
#     answer = []

#     maxValue = max(array)

#     for i in range(len(array)):
#         if array[i] == maxValue:
#             answer.append(-1)
#         else:
#             for j in range(1, len(array)):
#                 if i-j >= 0 and array[i-j] > array[i]:
#                     answer.append(i-j)
#                     break

#                 elif i+j <= (len(array)-1) and array[i+j] > array[i]:
#                     answer.append(i+j)
#                     break

#     return answer

def solution(array):
    answer = []

    for i in range(1, len(array)):
        if array[i] > array[0]:
            answer.append(i)
            break

    for i in range(1, len(array)):
        if array[i] >= array[i-1]:
            if i != len(array)-1 and array[i+1] > array[i]:
                answer.append(i+1)
            else:
                answer.append(answer[i-1])
        else:
            answer.append(i-1)

    answer[array.index(max(array))] = -1

    return answer


# a = [3, 5, 4, 1, 2]
# a = [7, 4, 4, 2, 9, 6]
a = [1, 2, 3, 4, 5]
print(solution(a))
