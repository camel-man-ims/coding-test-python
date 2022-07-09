# 22.07.09
# L이 100만이었다.

import sys

sys.stdin = open("input.txt")

n = int(input())

for _ in range(n):
    iv = input()

    ls = []
    rs = []

    for s in iv:
        # left stack ->
        if s == '<':
            if ls:
                rs.append(ls.pop())
        elif s == '>':
            if rs:
                ls.append(rs.pop())
        elif s == '-':
            if ls:
                ls.pop()
        else:
            ls.append(s)

    ls.extend(reversed(rs))

    print(''.join(ls))