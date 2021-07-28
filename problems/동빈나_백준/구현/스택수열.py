from collections import deque
n = int(input())

data_arr = deque()
numbers = deque()
temp = deque()
result = []

for _ in range(n):
    data_arr.append(int(input()))

for i in range(2,n+1):
    numbers.append(i)

temp.append(1)
result.append("+")

while data_arr:
    pop_value = data_arr.popleft()
    while temp and temp[-1] < pop_value:
        temp.append(numbers.popleft())
        result.append("+")
    if temp and temp[-1]==pop_value:
        temp.pop()
        result.append("-")
    else:
        print("NO")
        exit(0)

for i in result:
    print(i)