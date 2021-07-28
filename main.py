from collections import deque

arr = deque()

arr.append([1,100])
arr.append([2,200])
arr.append([3,300])
arr.append([4,400])

print(max(arr))