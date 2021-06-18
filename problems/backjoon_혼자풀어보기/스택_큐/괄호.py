# 21.06.18

n = int(input())

for _ in range(n):
    stack = []
    s_value = input()
    flag = True

    for s in s_value:
        if s=='(':
            stack.append(s)
        elif s==')':
            if stack:
                stack.pop()
            else:
                flag=False

    if flag and not stack:
        print("YES")
    else:
        print("NO")



