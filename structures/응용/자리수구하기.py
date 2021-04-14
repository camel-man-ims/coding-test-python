a = 92756

temp =[]

while a:
    temp.append(a % 10)
    a=a//10

result=[]

for i in range(len(temp)-1,-1,-1):
    result.append(temp[i])

print(result)