arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

for nums in arr:
    print(nums)

result = [[0]*(len(arr)) for _ in range(len(arr))]

print("=======90도 회전 후========")

for i in range(len(arr)):
    for j in range(len(arr)):
        result[j][len(arr)-1-i]=arr[i][j]

for nums in result:
    print(nums)