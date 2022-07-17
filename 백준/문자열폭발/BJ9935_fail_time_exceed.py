import sys

# 22.07.17
# 시간초과

sys.stdin = open("input.txt")

iv = input()
determine = input()


def check(s: str):
    global determine
    for i in range(len(s) - len(determine) + 1):
        if s[i:i + len(determine)] == determine:
            return True
    return False


while check(iv) and len(iv) >= len(determine):
    tmp: str = ""
    p: int = 0
    while p < len(iv):
        if iv[p:p + len(determine)] == determine:
            p += len(determine)
            continue
        tmp += iv[p]
        p += 1
    iv = tmp

if iv:
    print(iv)
else:
    print("FRULA")
