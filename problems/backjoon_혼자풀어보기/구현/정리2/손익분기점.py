# 21.06.16
# A,B,C 가 주어졌을 때, A + nB < nC 인 n 을 구하는 문제

a,b,c = map(int,input().split())

n=1

if b>=c:
    print(-1)
else:
    temp = c-b
    divide = a//temp
    print(divide+1)