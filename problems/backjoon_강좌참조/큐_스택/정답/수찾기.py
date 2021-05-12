n = int(input())

arr = set(map(int,input().split()))

m = int(input())

arr2= list(map(int,input().split()))

for i in arr2:
    if i not in arr:
        print('0')
    else:
        print('1')