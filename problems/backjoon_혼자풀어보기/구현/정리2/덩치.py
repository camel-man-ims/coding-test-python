n = int(input())

arr = []

for _ in range(n):
    weight, height = map(int,input().split())
    arr.append([weight,height])

result = []

for i in range(len(arr)):
    count = 1
    for j in range(len(arr)):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            count +=1
    result.append(count)

for i in result:
    print(i,end=' ')