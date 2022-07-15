import sys

# 22.07.15

sys.stdin= open("input.txt")

n,m = map(int,input().split())

hash_set = set()

for _ in range(n):
    s = input()
    hash_set.add(s)

cnt: int = 0
for _ in range(m):
    s = input()
    if s in hash_set:
        cnt += 1

print(cnt)