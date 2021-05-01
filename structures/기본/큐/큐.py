from collections import deque

data= deque([1,2,3,4])

data.append(5)

print(data)

data.popleft()

print(data[0])
