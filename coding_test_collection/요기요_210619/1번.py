# email parsing 하는 문제
# John Doe, Peter Parker, Mary Jane Watson-Parker, James Doe 이렇게 주어진다면
# 마지막 문자만 이름으로 설정을 하고, 앞의 글자들은 앞 글자만 따서 저장
# 이 때, 마지막 문자인 이름에는 - 이 들어갈 수 있고, 앞에서부터 8자만 따야함
# jdoe, pparker, mjwatsonpa, jdoe2
# 위의 예에서 jdoe가 2개 나오는데, 구분을 위해 중복이 있다면 마지막에 숫자를 붙여야한다.

# replace 가 안먹혀서 뭔가 했는데, replace 는 새로운 값을 return 한다. 해당 인스턴스의 문자열을 수정해주지 않는다.

def solution(s_values,company_name):
    split = s_values.split(", ")
    result = []
    company_name = company_name.lower()
    hash_map = dict()

    for s in split:
        individual_split = s.split(" ")
        if len(individual_split)==2:
            first_letter = individual_split[0][0].lower()
            name = individual_split[1].lower()

            name = "".join(c for c in name if c.isalpha())

            if len(name)>=8:
                name = name[:8]

            email_title = first_letter+name
            email = ""
            if email_title in hash_map:
                hash_map[email_title] += 1
                count = hash_map[email_title]
                email = "<" + email_title + str(count)+ "@" + company_name + ".com" + ">"
            else:
                hash_map[email_title] =1
                email = "<" + email_title + "@" + company_name + ".com" + ">"
            result.append(email)

        elif len(individual_split)==3:
            first_letter = individual_split[0][0].lower()
            second_letter = individual_split[1][0].lower()
            name = individual_split[2].lower()

            name = "".join(c for c in name if c.isalpha())
            if len(name)>=8:
                name = name[:8]
            email_title = first_letter+second_letter+name
            email = ""
            if email_title in hash_map:
                count = hash_map[email_title]+1
                email = "<" + email_title + str(count)+ "@" + company_name + ".com" + ">"
            else:
                hash_map[email_title] =1
                email = "<" + email_title + "@" + company_name + ".com" + ">"

            result.append(email)

    s_result = ""
    for i in range(len(split)):
        s_result += split[i] + " " + result[i]
        if i is not len(split)-1:
            s_result += ", "

    return s_result

print(solution("John Doe, Peter Parker, Mary Jane Watson-Parker, James Doe, John Elvis Doe, Jane Doe, Penny Parker","Example"))