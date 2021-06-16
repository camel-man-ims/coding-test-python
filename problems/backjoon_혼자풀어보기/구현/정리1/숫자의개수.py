# 21.06.10
# 곱의 결과에 대한 숫자의 개수를 순서대로 몇개인지 출력하는 문제

a= int(input())
b= int(input())
c= int(input())

value = a*b*c

hash_map = dict()

for i in str(value):
    if int(i) in hash_map:
        hash_map[int(i)] +=1
    else:
        hash_map[int(i)]=1

li = []

for i in hash_map:
    li.append((i,hash_map[i]))

li.sort(key=lambda x:x[0])

for i in range(10):
    flag = True
    val = 0
    for tup in li:
        if i == tup[0]:
            flag=False
            val = tup[1]
    if flag:
        print(0)
    else:
        print(val)