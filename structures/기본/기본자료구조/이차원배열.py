# 21.05.06

arr = [[0]*4 for _ in range(2)]

print(arr)

# 4개의 열을 가진 행을 3개 만든다
arr = [[0 for _ in range(4)] for _ in range(3)]

print(arr)

# python 은 이런식으로 선언하면 얕은복사를 이용하게 되므로, 깊은 복사(for)을 돌려서 생성해야 한다
wrong_arr = [[0] * 4] * 4
print(wrong_arr)
wrong_arr[0][0] =1
print(wrong_arr)