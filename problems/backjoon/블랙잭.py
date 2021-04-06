# 백준 2798번

from itertools import combinations

n, k = map(int, input().split(' '))

data = list(map(int, input().split(' ')))

arr = combinations(data,3)
result=[]

for arr2 in arr:
    temp=0
    for j in arr2:
        temp = temp +j

    result.append(temp)

result.sort()

result_number=0

for i in range(len(result)):
    if result[i] < k < result[i + 1]:
        result_number = result[i]
        break
    else:
        result_number=k

print(result_number)