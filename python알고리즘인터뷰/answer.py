import sys
sys.stdin=open("input.txt", "rt")

n=int(input())
board=[list(map(int, input().split())) for _ in range(n)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
largest=max(map(max, board))

for i in range(1, largest):
    depth = i
    ch = [[0] * n for _ in range(n)]




