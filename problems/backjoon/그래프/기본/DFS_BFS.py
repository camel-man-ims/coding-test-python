# 21.04.18

from collections import deque

def dfs(v):
    print(v,end = ' ')
    visited[v] = True
    for e in adj[v]:
        if not(visited[e]):
            dfs(e)

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if not (visited[v]):
            visited[v]=True
            print(v,end= ' ')
            for e in adj[v]:
                # 여기서 not visited[e]가 한번 더 안들어가도 되는 것 같다
                if not visited[e]:
                    q.append(e)

# n = 정점의 개수 m = 간선의 개수 v = 탐색 시작 번호
n,m,v = map(int,input().split())
# 0은 비워둬서 n+1까지 선언
# adj = 간선. 2차원 배열로 선언
adj = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)

# 참조값 정렬
# 문제에서 순서가 낮은 값이 먼저 나오도록 하기 위해
for e in adj:
    e.sort()

visited = [False] * (n+1)
dfs(v)
print()

visited = [False] * (n+1)
bfs(v)

