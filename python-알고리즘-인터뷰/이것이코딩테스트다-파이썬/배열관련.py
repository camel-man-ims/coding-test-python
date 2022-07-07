# 22.07.07

N = 3
M = 4

arr = [[0] * M for _ in range(N)]
print(arr)

print("---------")

# 2차원 리스트 초기화 시 반드시 list comprehension 이용

arr = [[0] * M] * N
arr[1][1] = 1
print(arr)

print("---------")

arr = [1, 3, 5, 6]

arr.append(10)
print(arr)

arr.insert(0, 11)
print(arr)

arr.sort()
print(arr)

arr.sort(reverse=True)
print(arr)

arr.remove(3)
print(arr)

print(arr.count(3))

print("-------------------")

# 특정한 원소의 값 제거
arr = [1, 2, 3, 4, 5, 6]
arr_remove = [1, 3, 6]

arr = [i for i in arr if i not in arr_remove]
print(arr)

print("------------")