# 21.05.02

n= int(input())

result = []

for _ in range(n):
    count=0
    temp =0
    input_value = input()
    for s in input_value:
        if s == 'O':
            count +=1
            temp += count
        else:
            count = 0
    result.append(temp)

for i in result:
    print(i)
