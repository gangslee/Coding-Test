# 참고 풀이 https://suri78.tistory.com/183

import sys

n = int(sys.stdin.readline())
letter = [0]*26
current, result = 9, 0

for _ in range(n):
    word = sys.stdin.readline().rstrip()

    for i in range(len(word)):
        letter[ord(word[i])-65] += 10**(len(word)-1-i)

letter.sort(reverse=True)

for i in letter:
    if i == 0:
        break
    result += i*current
    current -= 1

print(result)
