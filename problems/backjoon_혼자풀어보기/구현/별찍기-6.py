# n = 5
# 별 9 7 5 3 1
# 공백 0 1 2 3 4

n = int(input())

for i in range(n):
    for k in range(i):
        print(" ",end="")
    for k in range(2*n-1-2*i):
        print("*",end="")
    print()