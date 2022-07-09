import sys

sys.stdin = open("input.txt","rt")

N,K = map(int,input().split())

arr = []

for i in range(N):
    arr.append(int(input()))

start = 0
end = 10000000

sum_value = 0

while start<end:
    mid = (start + end) // 2

    temp = 0
    for a in arr:
        temp += a//mid

    if temp >= K:
        start = mid+1
    else:
        end = mid

print(start-1)