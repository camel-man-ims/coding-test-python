# 3 <= len <= 15
# - _ . 알파벳 소문자, 숫자
# .는 처음과 끝 불가능. 연속사용 x

def solution(new_id):
    # 1번 소문자 변환
    new_id = new_id.lower()

    # 2번 알파벳 소문자, 숫자, -, _, . 제외한 문자 제거
    changed_id = ""

    for s in new_id:
        if s.isalpha() or s.isdigit() or s == '-' or s == '_' or s == '.':
            changed_id += s

    changed_three = ""
    # 3-2) 2번 . 이상이면 제거
    # changed_id 가 변화하므로 len(changed_id) 역시 변화함
    # for i in range(len(changed_id) - 1):
    #     if changed_id[i] == '.' and changed_id[i + 1] == '.':
    #         changed_three = changed_id[:i] + changed_id[i + 1:]
    #     else:
    #         changed_three = changed_id
    index=0
    while index<len(changed_id):
        if index != len(changed_id)-1 and changed_id[index]=='.' and changed_id[index+1]=='.':
            index+=1
        elif index != len(changed_id)-1 and changed_id[index]=='.' and changed_id[index+1]!='.':
            changed_three += "."
            index+=1
        else:
            changed_three += changed_id[index]
            index+=1

    # 3번 . 2번이상 제거.  . 맨앞이나 맨 뒤면 제거
    # 3-1) 맨앞이나 맨뒤 . 면 제거
    if len(changed_three) >= 2:
        while changed_three[0] == '.' or changed_three[len(changed_three) - 1] == '.':
            if changed_three[0] == '.' and changed_three[len(changed_three) - 1] == '.':
                changed_three = changed_three[1:len(changed_three) - 1]
            elif changed_three[0] == '.':
                changed_three = changed_three[1:]
            elif changed_three[len(changed_three) - 1] == '.':
                changed_three = changed_three[:len(changed_three) - 1]

    if changed_three == ".":
        changed_three = ""

    if changed_three == "":
        changed_three += "a"

    if len(changed_three) >= 16:
        changed_three = changed_three[:15]

    while len(changed_three) < 3:
        changed_three += changed_three[len(changed_three) - 1]

    while changed_three[len(changed_three)-1] == '.':
        changed_three = changed_three[:len(changed_three)-1]

    # print(changed_three)
    return changed_three


solution("...!@BaT#*..y.abcdefghijklm.")
solution("=.=")
solution("aa")
solution("123_.def")
solution("=weew.q.q")
solution("bb...")