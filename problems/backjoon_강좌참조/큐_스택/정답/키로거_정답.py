# 백준 5397 키로거 21-04-09

test_case = int(input())

for _ in range(test_case):
    left_stack = []
    right_stack = []

    data=input()
    # String 으로 전체 받아짐

    for i in data:
        if i == '-':
            if left_stack:
                left_stack.pop()
        elif i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)

    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))