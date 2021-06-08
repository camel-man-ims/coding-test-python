def solution(n,data,limit):
    result = []

    li_total = []
    for s in data:
        li = s.split(" ")
        li_total.append(li)
    hash_map = dict()
    for i in range(1,n+1):
        hash_map[i]=1000000

    for s in li_total:
        if hash_map[int(s[1])] > int(s[2]) + int(s[3]):
            result.append(s[0])
            hash_map[int(s[1])]= int(s[2]) + int(s[3])
        elif hash_map[int(s[1])] == int(s[2]) + int(s[3]):
            get = result[int(s[1])-1]
            num_1 = s[0]
            num_1 = int(num_1[1:])
            num_2 = int(get[1:])

            if num_1 > num_2:
                result[int(s[1])-1]=s[0]
            elif num_1 == num_2:
                alpha_1 = s[0]
                alpha_1 = alpha_1[0]
                alpha_2 = get[0]

                if alpha_1 < alpha_2:
                    result[int(s[1])-1]=s[0]

    time_ = 0
    space_ = 0

    for s in li_total:
        for re in result:
            if s[0] == re:
                time_ += int(s[2])
                space_ += int(s[3])
    time_flag = True
    space_flag = True

    limit_split = limit.split(' ')

    if int(limit_split[0]) == 0:
        time_flag = True
    elif int(limit_split[0]) !=0 and space_ > int(limit_split[0]):
        time_flag = False

    if int(limit_split[1]) == 0:
        space_flag = True
    elif int(limit_split[1]) != 0 and space_ > int(limit_split[1]):
        space_flag = False

    if time_flag and space_flag:
        return result
    else:
        return []


l = solution(2, ["a1 1 5 9", "a2 1 9 5", "b1 2 3 3"], "0 10")
print(l)