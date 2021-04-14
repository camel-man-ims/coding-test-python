# 21.04.15
# 패캠 AL 강좌 3번째 강의

# + 보다 join 활용
s=""
a="abc"
join = s.join(a)
print(join)

# chr, ord ascii
print(chr(48))
print(ord('0'))

# list comprehension
list_arr = [i for i in range(5)]
print(list_arr)

# input
# input 은 항상 문자열 기준
# 그래서 변환을 해주어야 하는데, map(int,input().split()) 같은 형식으로 받으면 되는 것
# 이때, 입력값을 튜플로 받음

arr = [3, 4, 2, 1,5,3,3,3,3,3]

def check_is_set(lst):
    return len(lst)==len(set(lst))

print(check_is_set(arr))