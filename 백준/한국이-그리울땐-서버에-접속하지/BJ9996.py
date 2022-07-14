import sys
# 22.07.15

# https://www.acmicpc.net/board/view/20672
# 반례
# 1
# abcd*cdef
# abcdef
# 글자 중복해서 세면 안된다.

sys.stdin = open("input.txt")

n = int(input())
valid = input()

split_arr: list = valid.split("*")

v1: str = split_arr[0]
v2: str = split_arr[1]

for _ in range(n):
    s = input()

    if len(s) < len(v1) or len(s) < len(v2) or len(s) < len(v1) + len(v2):
        print("NE")
        continue

    s1 = s[0:len(v1)]
    s2 = s[len(s)-len(v2):len(s)]
    # s2 = s[-1:-(len(v2)+1):-1][::-1]

    if s1 != v1 or s2 != v2:
        print("NE")
        continue
    print("DA")
