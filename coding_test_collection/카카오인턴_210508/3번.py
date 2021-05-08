def solution(n, k, cmd):
    pointer = k
    arr = []
    stack = []
    current = []

    for i in range(n):
        current.append(i)

    for s in cmd:
        replace = s.replace(" ","")
        arr.append(replace)

    for s in arr:
        if s[0] == 'D':
            number = int(s[1:])
            pointer += number
        if s[0] == 'U':
            number = int(s[1:])
            pointer -= number
        if s[0] == 'C':
            pop = current.pop(pointer)
            stack.append(pop)
            if pointer > len(current)-1:
                pointer = len(current)-1
        if s[0] == 'Z':
            num = stack.pop()
            index = 0
            for i in range(len(current)-1):
                if current[i] < num < current[i+1]:
                    index=i+1
                    if index <= pointer:
                        pointer+=1
                    current.insert(index,num)
                    break
                elif num > current[len(current)-1]:
                    current.insert(len(current)-1,num)
    result = []
    flag = True
    for i in range(n):
        for num_value in current:
            if i == num_value:
                flag = True
                break
            else:
                flag= False
        if flag:
            result.append('O')
        else:
            result.append('X')
    str_result = ""
    for s_value in result:
        str_result += s_value
    print(str_result)
    return str_result

solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])