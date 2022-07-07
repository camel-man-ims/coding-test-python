lst = [10, 20, 30,40,50,60]

print(lst[1:3])
print(lst[0:5:2])

print(lst.pop())
print(lst)
# 앞에서부터 n 번째 index 제거
print(lst.pop(1))
print(lst)

# 파이썬에서는 모든 것이 객체!
# 1차원 배열에서도 값을 객체로 연결하기 때문에 각각의 자료형이 달라도 되는 것
# 그러나 메모리에 연속적으로 저장할 수 없기 때문에 속도는 떨어짐

# map
hashMap = dict()
hashMap2 = {}

hashMap['a'] = 'b'

for i,v in hashMap.items():
    print("i = " + str(i) + " v = " + v)

s = set({})

sArr = "Abcde"
# 기본
print(sArr[::1])
# 뒤집기
print(sArr[::-1])
# 2칸씩
print(sArr[::2])