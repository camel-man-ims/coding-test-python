# 21.04.19
from collections import deque

def dfs(num):
    print(num, end= ' ')
    visited[num]=True
    for i in adj[num]:
        if not visited[i]:
            dfs(i)

def bfs(num):
    queue = deque([num])
    while queue:
        pop_value = queue.popleft()
        if not visited[pop_value]:
            visited[pop_value]=True
            print(pop_value,end= ' ')
            for i in adj[pop_value]:
                queue.append(i)


# n = 정점개수 m = 간선개수 v = 탐색시작번호
n,m,v = map(int,input().split())

adj = [[] for _ in range(n+1)]

for _ in range(m):
    x,y= map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)

for arr in adj:
    arr.sort()

# false 를 list 형으로 선언해줘야 한다
visited = [False] * (n+1)
dfs(v)

print()

visited = [False] * (n+1)
bfs(v)