# 리스트 컴프리헨션
print([i for i in [1,2,3,4,5] if i%2 == 0])

# sep
print('a','b',sep=', ')

# True == 1
print(True==1)

# 불변 가변
a = 'abcd'
a = 'bc'
print(id('abcd'))
print(id(a))
print(id('bc'))
# error string = 불변
# a[1] = 'c'

# is id()값 비교 , == 값 비교
a = [1,2,3]
print(a == [1,2,3])
print(a is [1,2,3])