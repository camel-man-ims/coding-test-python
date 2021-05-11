# 21.05.11

def check(s):
    if s == s[::-1]:
        return True
    else:
        return False

def solution(s):

    arr = []

    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            s_value = s[i:j]
            if check(s_value):
                arr.append(s_value)

    arr.sort(key=len,reverse=True)
    answer = len(arr[0])
    return answer


i= solution("abcdcba")
print(i)