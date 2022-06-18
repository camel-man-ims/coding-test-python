def solution(s):

    n = len(s)

    if n == 1:
        return 1
    if n ==2 :
        return 2

    result = []

    for i in range(1,n//2+1):
        before = s[:i]
        j = i
        cnt = 1
        s_temp = ""
        while j < n :
            if before == s[j:j+i]:
                cnt+=1
            else:
                if cnt==1:
                    s_temp += before
                else:
                    s_temp += str(cnt) + before
                    cnt = 1
                before = s[j:j+i]
            j += i

        j-=i
        if i!=1:
            if cnt != 1:
                s_temp += str(cnt) + before
            else:
                s_temp += s[j:n]
        else:
            s_temp += str(cnt) + before
        print(s_temp)
        result.append(len(s_temp))
    result.sort()
    return result[0]


print(solution("ababcdcdababcdcd"))
