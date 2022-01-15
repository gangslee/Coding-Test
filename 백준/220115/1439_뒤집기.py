s = input()
result = 1

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        result += 1

print(result//2)
