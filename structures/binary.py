arr = [1, 2, 3, 4, 5, 6, 7]
find = 5

def binary(start, end):
    if start > end:
        pass

    middle = int((start + end) / 2)

    if arr[middle] == find:
        return middle
    elif arr[middle] > find:
        return binary(start,middle-1)
    else:
        return binary(middle+1,end)

print(binary(0,len(arr)-1))