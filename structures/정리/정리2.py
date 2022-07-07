# 22.07.07
# 익명함수
import math

print((lambda a,b: a+b)(3,7))

print("---------------")

# 입출력
# n = int(input())
# data = list(map(int,input().split()))
# n2,m,k = map(int,input().split())

# import sys
# sys.stdin.readline().rstrip()

answer = 7
print("result = " + str(answer))

# 핵심라이브러리
# itertools 순열 조합
# heapq 우선순위큐
# bisect 이진탐색
# collections 덱, 카운터

arr = [1,2,3,4]
print(sum(arr))
print(min(arr))
print(max(arr))
print(eval("3*5+1"))
print(sorted(arr,reverse=True))
print(arr)

from itertools import combinations
from itertools import permutations
from itertools import product
from itertools import combinations_with_replacement

data=[10,20,30,40,50]
print(list(permutations(data,3)))
print(list(combinations(data,3)))
# 중복 순열
print(list(product(data,repeat=2)))
# 중복 조합
print(list(combinations_with_replacement(data,2)))

print("----------")

# heapq
# 최대힙을 만들 때는 넣을 때 -, 뺄 때 -붙여주기
import heapq
arr = [1,4,30,4,5]
h = []
for i in arr:
    heapq.heappush(h,i)

while h:
    print(heapq.heappop(h))


# 이진탐색
from bisect import bisect_left, bisect_right
arr = [1,2,3,3,3,3,4,5]
print(bisect_left(arr,3))
print(bisect_right(arr,3))


# 큐
# deque를 사용해서 큐 구현

from collections import deque
data = deque([1,2,3])
data.append(4)
data.appendleft(5)
print(data)
print(list(data))

# counter
# 등장 횟수 세기
from collections import Counter
counter = Counter(["a","a","b","b","b","c"])
print(counter["a"])

# math
print(math.factorial(30))
print(math.sqrt(36))
# 최대 공약수
print(math.gcd(21,14))