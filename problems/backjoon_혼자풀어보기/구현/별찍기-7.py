# n = 5
# 별 1 3 5 7 9 7 5 3 1
# 공백 4 3 2 1 0 1 2 3 4

n= int(input())

for i in range(n):
    for k in range(n-1-i):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()

for i in range(1,n+1):
    for k in range(i):
        print(" ",end="")
    for k in range(2*n-1-2*i):
        print("*",end="")
    print()