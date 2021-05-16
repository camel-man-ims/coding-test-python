from collections import deque

def bfs(value):
    print(value,end=' ')
    visited[value] = True
    for num in arr[value]:
        if visited[num] is False:
            bfs(num)

def dfs(value):
    # deque(3) x deque([3]) o
    q = deque([value])
    while q:
        pop = q.popleft()
        if visited[pop] is False:
            print(pop,end=' ')
            visited[pop] = True
            for num in arr[pop]:
                q.append(num)


n,m,v = map(int,input().split(' '))

arr = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split(' '))
    arr[a].append(b)
    arr[b].append(a)

for e in arr:
    e.sort()

visited = [False] * (n+1)
bfs(v)
print()
visited = [False] * (n+1)
dfs(v)