# 22.07.17

import collections
import sys

sys.stdin = open("input.txt")

n = int(input())
hs = collections.defaultdict(int)

for _ in range(n):
    iv = int(input())
    hs[iv] += 1

mv: int = 0
res: int = 0

for v in hs:
    if mv < hs[v]:
        mv = hs[v]
        res = v
    elif mv == hs[v] and res > v:
        res = v

print(res)
