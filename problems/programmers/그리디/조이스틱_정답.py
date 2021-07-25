def check_asc(i,name):
    flag = True

    if i+1<len(name):
        for num in range(i+1,len(name)):
            if name[num] != 'A':
                flag = False
    return flag


def check_desc(i, name):
    flag = True

    if i-1>=0:
        for num in range(i-1,0,-1):
            if name[num] != 'A':
                flag = False
    return flag

def solution(name):
    result =0

    for c in name:
        number = ord(c)
        number_cal = min(abs(65-number),abs(91-number))
        result += number_cal

    go_asc = 0
    go_desc = 1

    for i in range(0,len(name)):
        if not check_asc(i,name):
            go_asc +=1
    for i in range(len(name)-1,0,-1):
        if not check_desc(i,name):
            go_desc+=1

    result += min(go_asc,go_desc)

    if result <= 0:
        return 0
    else:
        return result