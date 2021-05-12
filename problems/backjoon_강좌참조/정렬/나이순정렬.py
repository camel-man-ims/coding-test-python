# 10814 나이순 정렬
# 21.04.13

n = int(input())

array = []

for _ in range(n):
    input_data = input().split(' ')
    array.append((int(input_data[0]),input_data[1]))

# python 은 stable 속성을 지님 ( 원래 있던 놈이 위로 가게 됨 )
array = sorted(array,key=lambda x:x[0])

for i in array:
    print(i[0],i[1])