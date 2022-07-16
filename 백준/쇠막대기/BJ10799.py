import sys

# 22.07.16

sys.stdin = open("input.txt")

iv = input()

stack = []
cnt: int = 0
res: int = 0

for i in range(len(iv)):
    c = iv[i]

    if c == '(':
        stack.append([c,i])
        cnt += 1
    elif c == ')':
        if stack:
            # [-1][1] = last index
            # if cut pipe
            cnt -= 1
            if stack[-1][1] == i-1:
                res += cnt
            else:
                res += 1
            stack.pop()

print(res)



