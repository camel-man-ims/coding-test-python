# 21.04.21
# n 개의 값을 k 개의 영역으로 나누려고 할 때, k 개로 나누어진 영역 안의 요소들 간의 차가 최소가 되게 하게 묶음을 짜라

import sys

n =  int(input())
k = int(input())

# k 개의 영역으로 나눌 때 k 가 더 크다면 0임
if k>=n:
    print(0)
    sys.exit()

array = list(map(int,input().split(' ')))
array.sort()

# 정렬 해놓고, 각 구간들의 차이를 계산
distances = []
for i in range(1,n):
    distances.append(array[i]-array[i-1])
distances.sort(reverse=True)

# 2개면 1개, 3개면 2개 연결 끊으면 k 개의 영역이 완성
# 큰 수대로 차례로 연결을 끊는다
for i in range(k-1):
    distances[i]=0
print(sum(distances))