# 21.05.08
# "one4seveneight" => 1478
# "2three45sixseven" => 234567

alpha_list = dict()
alpha_list["zero"] = 0
alpha_list["one"] = 1
alpha_list["two"] = 2
alpha_list["three"] = 3
alpha_list["four"] = 4
alpha_list["five"] = 5
alpha_list["six"] = 6
alpha_list["seven"] = 7
alpha_list["eight"] = 8
alpha_list["nine"] = 9


def solution(s):
    result = ""
    i=0
    while i<len(s):
        word = ""

        if s[i].isalpha():
            word += s[i]
            pointer = i + 1
            while pointer < len(s):
                if word in alpha_list:
                    break
                word += s[pointer]
                pointer+=1

            result += str(alpha_list[word])
            i = pointer

        else:
            result += str(s[i])
            i = i+1

    return int(result)


solution("23four5six7")
