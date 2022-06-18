import sys
sys.stdin=open("input.txt", "rt")
sys.setrecursionlimit(100000)

n=int(input())
board=[list(map(int, input().split())) for _ in range(n)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
largest=max(map(max, board))
res=[]
ch=[[0]*n for _ in range(n)]
cnt=0
count = 0

def DFS(x, y):
    global count
    count+=1
    ch[x][y]=1
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>depth:
            DFS(xx, yy)

for i in range(1, largest):
    depth=i
    for j in range(n):
        for k in range(n):
            if board[j][k]>i and ch[j][k]==0:
                DFS(j,k)
                cnt += 1
    res.append(cnt)
    cnt=0
    ch = [[0] * n for _ in range(n)]

print(count)
print(max(res))

from collections import deque

dq=deque()

for d in range(1,largest):
    for i in range(n):
        for j in range(n):
            if board[i][j]>d and ch[i][j]==0:
                dq.append((i, j))
                ch[i][j]=1
                while dq:
                    now=dq.popleft()
                    for k in range(4):
                        x=now[0]+dx[k]
                        y=now[1]+dy[k]
                        if 0<=x<n and 0<=y<n and ch[x][y]==0 and board[x][y]>d:
                            dq.append((x, y))
                            ch[x][y]=1
                cnt+=1
    res.append(cnt)
    ch = [[0] * n for _ in range(n)]
    cnt=0


print(max(res))