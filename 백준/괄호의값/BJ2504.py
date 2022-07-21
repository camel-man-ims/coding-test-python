# 22.07.20
# https://velog.io/@booorim98/BOJ-2504

import sys

sys.stdin = open("input.txt")

iv = input()

stack = []
multiply: int = 1
res: int = 0

for i in range(len(iv)):
    if iv[i] == '(':
        stack.append(iv[i])
        multiply *= 2
    elif iv[i] == '[':
        stack.append(iv[i])
        multiply *= 3
    elif iv[i] == ')':
        if not stack or stack[-1] != '(':
            res = 0
            break
        if iv[i-1] == '(':
            res += multiply
        multiply /= 2
        stack.pop()
    elif iv[i] == ']':
        if not stack or stack[-1] != '[':
            res = 0
            break
        if iv[i-1] == '[':
            res += multiply
        multiply /= 3
        stack.pop()

if stack:
    print(0)
else:
    print(int(res))
