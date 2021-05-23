# 21.05.20

n = int(input())
arr = []

for _ in range(n):
    a,b = map(int,input().split(' '))
    arr.append((a,b))

start = 0
count = 0

arr.sort()
print(arr)

for i in range(n):
    if arr[i][0] == start:
        print(start)
        for j in range(i,n):
            if arr[i][1] > arr[j][1]:
                break
            else:
                start = arr[i][1]
                count +=1


print(count)


