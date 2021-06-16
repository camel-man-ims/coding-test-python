n = int(input())

count =1
result = []
stack = []
for _ in range(n):
    number = int(input())

    while count <= number:
        stack.append(count)
        count +=1
        result.append("+")

    if stack[-1] == number:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit(0)

print('\n'.join(result))