n = 62

i=1
count = 2
while 3*i*(i+1)+1<=n:
    count +=1
    i +=1

print(count)
# 1~6 1 6
# 7~18 2 6+12
# 19~36 3 6+12+18
