# 21.04.27

n = int(input())

for i in range(n):
    for _ in range(n-1-i,0,-1):
        print(" ",end='')
    for _ in range(2*i+1):
        print("*",end='')
    print()

for i in range(n):
    for _ in range(i+1):
        print(" ",end="")
    for _ in range(2*(n-i-1)-1):
        print("*",end="")
    for _ in range(i+1):
        print(" ",end="")
    if i is not n-1:
        print()