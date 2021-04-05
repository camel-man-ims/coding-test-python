# 1번
# 리스트의 모든 값이 고유하면 true, 아니면 false 를 반환
from collections import Counter
from typing import List


def all_union(li):
    return len(li) == len(set(li))


x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 2, 3, 4, 5]

print(all_union(x))
print(all_union(y))


# 2번
# 문자열의 첫 문자를 대문자로 만들라

def capitalize(s):
    return s.title()


s = "ersu"
print(capitalize(s))


# 4번
# falsey value 제거 ( 0, noun, false ) 등등

def remove_falsey(li):
    return list(filter(None, li))


li = [False, 0, 1, 2, 3, '']
print(remove_falsey(li))


# 8번
# a 리스트 - b 리스트?
def remove_b(a, b):
    set_b = set(b)
    return [item for item in a if item not in set_b]


a = [1, 2, 3, 4, 5]
b = [3, 3, 3, 3, 4, 5]

print(remove_b(a, b))


# 9번
# 숫자를 자리수로 만들기

def make_number(n):
    return list(map(int, str(n)))


print(make_number(123456))


# 14번
# 고유하지 않은 값 필터링하기

def filter_non_unique(lst):
    return [item for item, count in Counter(lst).items() if count == 1]


print(filter_non_unique([1, 2, 2, 2, 3, 4, 5, 5, 5, 5]))


# 15번
# 중복되는 값 가져오기
def filter_unique(lst):
    return [item for item, count in Counter(lst).items() if count > 1]


print(filter_unique([1,1,1,1,1,2,3,3,3,3,4,5]))
