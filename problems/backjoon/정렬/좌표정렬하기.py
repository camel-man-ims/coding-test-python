# 21.05.06

n = int(input())
arr = []
for _ in range(n):
    a,b = map(int,input().split(' '))
    arr.append((a,b))

arr.sort()

for num in arr:
    print(str(num[0]) + " " + str(num[1]))