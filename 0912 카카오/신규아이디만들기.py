def solution(new_id):
    re = ['-', '_', '.']
    answer = new_id.lower()
    for i in answer:
        if not('a' <= i <= 'z' or i in re or i.isdigit()):
            answer = answer.replace(i, '')
        elif i == '.':
            answer = answer.replace('..', '.')
    answer = answer.lstrip('.').rstrip('.')
    print(answer)
    if len(answer) > 15:
        return answer[:15].lstrip('.').rstrip('.')
    elif len(answer) < 3:
        if answer == '':
            answer = 'a'
        while len(answer) < 3:
            answer = answer+answer[len(answer)-1]
        return answer
    else:
        return answer


ni = '123_.def'

print(solution(ni))
