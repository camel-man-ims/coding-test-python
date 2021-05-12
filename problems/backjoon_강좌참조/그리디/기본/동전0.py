# 21.05.06

n,k = map(int,input().split(' '))

coins = []

for _ in range(n):
    coin = int(input())
    coins.append(coin)

coins.sort(reverse=True)
count = 0
for coin in coins:
    while coin<=k:
        k -= coin
        count +=1
print(count)