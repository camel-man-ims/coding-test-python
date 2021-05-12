# 5
# 9 7 5 3 1
# 0 1 2 3 4

n= int(input())

for i in range(n):
    for _ in range(i):
        print(" ",end='')
    for _ in range(2*(n-1-i),-1,-1):
        print("*",end='')
    for _ in range(i):
        print(" ", end='')
    if i is not n-1:
        print()
