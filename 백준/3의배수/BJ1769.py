# 22.07.15

import sys

sys.stdin=open("input.txt")

iv = input()

tmp: int = 0
cnt: int = 0

flag = False
res = False

ivn = int(iv)

if ivn < 10:
    print(0)
    if ivn%3==0:
        print("YES")
    else:
        print("NO")
    sys.exit(0)

while True:
    cnt += 1
    tmp = 0
    for s in iv:
        tmp += int(s)

    if tmp < 10:
        flag = True
        if tmp % 3 == 0:
            res = True
        else:
            res = False
    if flag:
        break

    iv = str(tmp)

print(cnt)
if res:
    print("YES")
else:
    print("NO")