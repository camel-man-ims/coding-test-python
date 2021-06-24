def solution(s_input):

    result = ""
    count = 1

    for i in range(len(s_input)):
        if i == len(s_input)-1 or s_input[i] != s_input[i+1]:
            result += s_input[i] + str(count)
            count = 1
        elif s_input[i] == s_input[i+1]:
            count+=1
    print(result)


solution("aabcccccaaa")
