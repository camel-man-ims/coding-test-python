# 21.05.23

n,m = map(int,input().split(' '))

max_value = 0

for _ in range(n):
    data = list(map(int,input().split()))
    min_value = min(data)
    max_value = max(max_value,min_value)

print(max_value)

