# 21.04.25
# 공백 4 3 2 1 0
# 별 1 3 5 7 9
# 5줄

n = int(input())

for i in range(1,n+1):

    for _ in range(n-i,0,-1):
        print(" ",end="")

    for _ in range(2*i-1):
        print("*",end='')
    print()