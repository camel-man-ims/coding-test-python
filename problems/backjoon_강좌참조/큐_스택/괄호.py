# 21.05.06
# 맞았는데 ...

n = int(input())
result = []
for _ in range(n):
    s_value = input()
    stack = []
    flag=True
    for s in s_value:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if stack:
                stack.pop()
            else:
                flag=False
                break
    if flag and not stack:
        result.append("YES")
    else:
        result.append("NO")

print(result)
