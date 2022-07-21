# 22.07.18
# fail
# 문자열 끼리 더하면 원하는 대로 더해진다고 생각했음
# java로 풀음

import sys

sys.stdin = open("input.txt")

ivn = int(input())

form = "***\n* *\n***\n"

def recurse(n: int):
    global form
    if n == 3:
        return form

    res = ""
    space = ""

    for i in range(n // 3):
        for j in range(n // 3):
            space += " "
        if i is not n//3-1:
            space += "\n"

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                res += space
                continue
            res += recurse(n // 3)
    return res


print(recurse(ivn))