# 21.06.04
# ( [ ] ) 문제

while True:
    s_line = input()
    if s_line == '.':
        break
    stack =[]
    for s in s_line:
        if s == '(' or s=='[':
            stack.append(s)
        elif s == ')':
            if not stack or stack.pop()!='(':
                print('no')
                break
        elif s == ']':
            if not stack or stack.pop() != '[':
                print('no')
                break
        elif s == '.':
            if stack:
                print('no')
            else:
                print('yes')