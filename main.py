arr= dict()

arr['a']=1
arr['b']=2
arr['c']=3
arr['d']=4

s = 'd'

for key in arr.keys():
    if key == s:
        arr[s]=5

print(arr)