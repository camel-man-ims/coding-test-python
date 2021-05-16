total_money = 4720

coins = [500,100,50,1]

count = 0

for coin in coins:
    divide = total_money//coin
    total_money -= coin * divide
    count += divide

print(count)
