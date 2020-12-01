# import sys

# n, k = map(int, input().split())

# spin = list()
# idx = 0

# result = ['?']*n

# for i in range(k):
#     spin.append(list(input().split()))

# spin.reverse()

# for i in range(k):
#     if result[idx] != '?' or spin[i][1] in result or spin[i][1]<'A' or spin[i][1]>'Z':
#         print('!')
#         sys.exit(0)

#     result[idx] = spin[i][1]
#     idx = (idx-int(spin[i][0])) % n

# for i in result:
#     print(i, end="")


n, k = map(int, input().split())
board = ['?']*n
alpha_check = [False]*26
word_stack = []

for i in range(k):
    a, b = input().split()
    a = int(a)
    word_stack.append(a)
    word_stack.append(b)

idx = 0

while word_stack:
    alpha = word_stack.pop()
    if board[idx] == '?':
        if not alpha_check[ord(alpha)-ord('A')]:
            board[idx] = alpha
            alpha_check[ord(alpha)-ord('A')] = True
        else:
            print('!')
            break
    else:
        if board[idx] != alpha:
            print('!')
            break
    idx += word_stack.pop()
    idx %= n

else:
    print(*board, sep='')
