import sys

# 22.07.17

sys.stdin = open("input.txt")

iv = input()
determine = input()

while len(iv) >= len(determine):
    flag: bool = False
    tmp: str = ""
    p: int = 0
    while p < len(iv):
        if iv[p:p + len(determine)] == determine:
            p += len(determine)
        tmp += iv[p]
        p += 1
    iv = tmp

if iv:
    print(iv)
else:
    print("FRULA")