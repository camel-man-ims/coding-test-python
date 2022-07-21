import sys

sys.stdin = open("input.txt")

def recurse(n: int):
    if n == 1:
        return '-'

    tmp = ""
    for _ in range(n//3):
        tmp += ' '

    res = ""
    lr: str = recurse(n//3)
    res += lr
    res += tmp
    res += lr

    return res


for line in sys.stdin:
    # iv[0] 활용
    iv = list(map(int, line.split()))
    print(recurse(pow(3,iv[0])))