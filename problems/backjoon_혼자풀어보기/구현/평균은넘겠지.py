n= int(input())

array = []

for _ in range(n):
    input_arr = map(int,input().split())
    arr = []
    for i in range(1,len(input_arr)):
        arr.append(input_arr[i])

    average = sum(arr)/len(arr)
    result = 0
    for i in arr:
        if i>average:
            result+=1
    array.append(round(result/len(arr),3))
print(array)