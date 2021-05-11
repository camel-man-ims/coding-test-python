from itertools import permutations

n,m = map(int,input().split(' '))

arr = []

for i in range(1,n+1):
    arr.append(i)

result = list(permutations(arr,m))

for nums in result:
    for num in nums:
        print(num,end=' ')
    print()