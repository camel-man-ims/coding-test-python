# 21.04.15
# for keys in arr.keys():
#     if s not in keys:
#         arr[s] = 1
#     else:
#         arr[s] = arr[s] + 1
# 이렇게 for keys 로 받으면 안된다 ... 왜지?

N = int(input())

arr = dict()

for _ in range(N):
    s = input()
    if s not in arr:
        arr[s]=1
    else:
        arr[s]=arr[s]+1

target = max(arr.values())
array =[]

for book,number in arr.items():
    if number==target:
        array.append(book)
print(sorted(array)[0])