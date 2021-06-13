import sys
input = sys.stdin.readline

INF = int(1e9) # 10억

n,m = map(int,input().split())

start = int(input())

graph = [[] for i in range(n+1)]

print(graph)