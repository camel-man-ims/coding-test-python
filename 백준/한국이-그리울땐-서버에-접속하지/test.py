import sys

# 혹시 길이가 3인가 했음

sys.stdin = open("input.txt")

n = int(input())
valid = input()

split_arr: list = valid.split("*")

v1: str = split_arr[0]
v2: str = split_arr[1]

for _ in range(n):
    s = input()
    if s[0] != v1 or s[-1] != v2:
        print("NE")
    else:
        print("DA")