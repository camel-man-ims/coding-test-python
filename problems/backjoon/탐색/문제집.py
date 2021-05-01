# 21.04.17
# 위상정렬 - 고급 탐색 알고리즘
# 위상정렬 - 순서가 정해져있는 작업을 차례로 수행해야 할 때, 순서를 결정해줌

# BFS 와 비슷한 메커니즘
# 위상이 0 인 노드를 찾고, 다음 노드를 넣음. 다음 노드와의 간선을 삭제해서 0으로 만들어줌.
# 사이클이 있으면 시작점을 찾을 수 없기 때문에 사이클이 없어야 한다

# 힙 = 우선순위 큐

import heapq

n,m = map(int,input().split())
array = [[] for i in range(n+1)]
in_degree = [0]*(n+1)

heap = []
result = []

for _ in range(m):
    x,y = map(int,input().split())
    array[x].append(y)
    in_degree[y] +=1

for i in range(1,n+1):
    if in_degree[i]==0:
        heapq.heappush(heap,i)

while heap:
    data = heapq.heappop(heap)
    result.append(data)
    for y in array[data]:
        in_degree -= 1
        if in_degree[y]==0:
            heapq.heappush(heap,y)
for i in result:
    print(i, end = ' ')