import sys

# 22.07.17

sys.stdin = open("input.txt")

iv = input()
determine = input()
stack = []

for i in range(len(iv)):
    stack.append(iv[i])

    if len(stack) >= len(determine):
        tmp: list = []
        for _ in range(len(determine)):
            tmp.append(stack.pop())
        s: str = "".join(tmp)[::-1]
        if s != determine:
            while tmp:
                stack.append(tmp.pop())

if stack:
    print("".join(stack))
else:
    print("FRULA")
