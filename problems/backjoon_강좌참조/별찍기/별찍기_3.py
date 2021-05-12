# 21.04.25

n = int(input())

for i in range(1,n+1):
    for _ in range(n-i,-1,-1):
        print("*",end="")
    print()