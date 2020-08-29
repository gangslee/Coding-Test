# 0이뜨는수 : fibo(n-1) 1이뜨는수 fibo(n) 여기서는 3부터

import sys

n = int(sys.stdin.readline())
s = [int(sys.stdin.readline()) for i in range(n)]

def fibo(f1, f2, cnt):
    fn = f1+f2
    if cnt==0:
        return [f2,fn]
    else:
        return fibo(f2,fn,cnt-1)

for i in s:
    if i == 0:
        print(1,0)
    elif i==1:
        print(0,1)
    elif i==2:
        print(1,1)
    else:
        print(fibo(0,1,i-2)[0], fibo(0,1,i-2)[1])

