n = int(input())

arr = [500, 100, 50, 10, 5, 1]

n= 1000-n
count =0

for coin in arr:
    if n>0:
        division_value = n // coin
        count += division_value
        n -= coin * division_value

print(count)