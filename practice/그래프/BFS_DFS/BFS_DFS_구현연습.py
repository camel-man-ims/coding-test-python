# 21.04.21

from collections import deque


def dfs(num):
    print(num,end=' ')
    visited[num]=True
    for val in adj[num]:
        if not visited[val]:
            dfs(val)


def bfs(num):
    q = deque([num])
    while q:
        pop_value = q.popleft()
        if not visited[pop_value]:
            print(pop_value, end = ' ')
            visited[pop_value]= True
            for i in adj[pop_value]:
                q.append(i)


n,m,k = map(int,input().split())

# adjacent
adj = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)

for e in adj:
    e.sort()

visited = [False] * (n+1)
dfs(k)

print()

visited = [False] * (n+1)
bfs(k)