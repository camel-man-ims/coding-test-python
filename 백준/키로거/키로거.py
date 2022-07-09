# 22.07.07
# 시간초과

import sys

sys.stdin = open("input.txt")

n = int(input())

for _ in range(n):
    iv = input()

    lst = []
    p = 0
    for s in iv:
        if s == '<':
            if p > 0:
                p-=1
        elif s == '>':
            if p<len(lst):
                p+=1
        elif s == '-':
            if p == len(lst):
                p-=1
            if lst:
                del lst[p]

        else:
            lst.insert(p,s)
            p+=1

    print("".join(lst))