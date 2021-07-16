n = int(input())

arr =[[0]*14 for _ in range(15)]

for i in range(14):
    arr[0][i] = i+1

for i in range(1,15):
    for j in range(0,14):

        sum_result = 0

        for k in range(0,j+1):
            sum_result += arr[i-1][k]

        arr[i][j] = sum_result


for _ in range(n):
    K = int(input())
    N = int(input())

    print(arr[K][N-1])
