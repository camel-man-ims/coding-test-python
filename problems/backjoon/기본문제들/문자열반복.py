# 21.05.02

n= int(input())

result = []

for _ in range(n):
    a,b = input().split(" ")
    iter_num = int(a)
    temp = ""

    for s in b:
        for number in range(iter_num):
            temp += s
    result.append(temp)

for re in result:
    print(re)