# 21.04.21

import heapq

n = int(input())

array = []
q = []

for i in range(n):
    # a = 데드라인 b = 컵라면 수
    a,b= map(int,input().split())
    array.append((a,b))

array.sort()

for i in array:
    a = i[0]
    heapq.heappush(q,i[1])
    # 데드라인을 초과하는 경우, 최소 원소를 제거
    if a < len(q):
        heapq.heappop(q)

print(sum(q))