# 22.07.07

a = 0.3
b = 0.6

print(a + b)  # 0.89999999
print(round(a + b, 4))  # 소수점 5째 자리에서 반올림

print("------------")

a = 3
b = 2

print(3 / 2)
print(3 // 2)  # 몫
print(3 ** 2)  # 거듭제곱

print("-----------")

n = 10
arr = [0] * n
print(arr)

print("---------")

arr = [1, 2, 3, 4, 5, 6]
print(arr[-1])
print(arr[1:4])

print("----------")

arr = [i for i in range(20) if i % 2 == 0]
print(arr)
