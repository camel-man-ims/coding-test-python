# 21.04.15

N = int(input())

arr = []

for _ in range(N):
    num = int(input())
    arr.append(num)

max_value = 0
count_asc = 0
count_desc = 0

for i in range(len(arr)):
    if arr[i] > max_value:
        count_asc += 1
        max_value = arr[i]

max_value = 0

for i in range(len(arr)-1,-1,-1):
    if arr[i] > max_value:
        count_desc += 1
        max_value = arr[i]

print(count_asc)
print(count_desc)
