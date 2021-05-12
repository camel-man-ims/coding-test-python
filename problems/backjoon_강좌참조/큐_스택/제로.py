# 21.05.06

n= int(input())

stack = []

for _ in range(n):
    num = int(input())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()

result =0

for i in stack:
    result += i

print(result)