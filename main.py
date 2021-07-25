from collections import deque

arr = deque()

arr.append(1)
arr.append(2)
arr.append(3)
arr.append(4)

while arr:
    arr.pop()
    print(arr)