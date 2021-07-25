# 21.07.23
# 실패
n = int(input())

index =0
arr = []

for _ in range(n):
    input_value = input().split(" ")
    arr.append([input_value[0],index,input_value[1]])
    index+=1

arr.sort()

for s_arr in arr:
    print(str(s_arr[0]) + " " + str(s_arr[2]))