n = int(input())

arr = list(map(int,input().split()))

max_value = max(arr)

fixed_arr = []

for i in arr:
    temp = i/max_value * 100
    fixed_arr.append(round(temp,2))

print(round(sum(fixed_arr)/len(arr),2))