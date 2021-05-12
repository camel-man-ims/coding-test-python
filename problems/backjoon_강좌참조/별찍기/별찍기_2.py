# 21.04.25

n = int(input())

for i in range(1,n+1):
    for _ in range(n-i,0,-1):
        print(" ",end="")
    for _ in range(i):
        print("*",end="")
    print()