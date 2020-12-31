p = int(input())

m = list()


# 소수 확인 함수


def chkPrime(a):
    if a < 2:
        return False

    for i in range(2, a):
        if(a % i == 0):
            return False

    return True

# 행복한 소수 확인 함수


def chkHappy(n):
    while n != '89':
        sum = 0

        for i in n:
            sum += int(i)**2

        if sum == 1:
            return True
        else:
            n = str(sum)
    else:
        return False


for i in range(p):
    m.append(input())

    num = m[i].split()[1]

    if chkPrime(int(num)):
        result = chkHappy(num)

        if result:
            m[i] += ' YES'
        else:
            m[i] += ' NO'
    else:
        m[i] += ' NO'

for i in m:
    print(i)
