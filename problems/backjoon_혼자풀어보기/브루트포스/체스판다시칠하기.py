n,m = map(int,input().split())

arr = []

for _ in range(n):
    arr.append(input())

arr_white_start = []

for i in range(n):
    str_temp = ""
    if i%2 == 0:
        str_temp+="W"
    else:
        str_temp+="B"

    for k in range(m):
        if str_temp[len(str_temp)-1] == "W":
            str_temp += "B"
        else:
            str_temp += "W"
    arr_white_start.append(str_temp)

arr_black_start = []

for i in range(n):
    str_temp = ""
    if i%2 == 1:
        str_temp+="W"
    else:
        str_temp+="B"

    for k in range(m):
        if str_temp[len(str_temp)-1] == "W":
            str_temp += "B"
        else:
            str_temp += "W"
    arr_black_start.append(str_temp)

white_value = 0
black_value = 0

for i in range(n):
    for j in range(len(arr[i])):
        if arr[i][j] != arr_white_start[i][j]:
            white_value+=1
        if arr[i][j] != arr_black_start[i][j]:
            black_value += 1

print(white_value)
print(black_value)