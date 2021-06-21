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

    # 3번 . 2번이상 제거.  . 맨앞이나 맨 뒤면 제거
    # 3-1) 맨앞이나 맨뒤 . 면 제거
    if len(changed_id) >= 2:
        while changed_id[0] == '.' or changed_id[len(changed_id) - 1] == '.':
            if changed_id[0] == '.' and changed_id[len(changed_id) - 1] == '.':
                changed_id = changed_id[1:len(changed_id) - 1]
            elif changed_id[0] == '.':
                changed_id = changed_id[1:]
            elif changed_id[len(changed_id) - 1] == '.':
                changed_id = changed_id[:len(changed_id) - 1]

    # 3-2) 2번 . 이상이면 제거
    for i in range(len(changed_id) - 1):
        if changed_id[i] == '.' and changed_id[i + 1] == '.':
            changed_id = changed_id[:i] + changed_id[i + 1:]

    if changed_id == ".":
        changed_id = ""

    if changed_id == "":
        changed_id += "a"

    if len(changed_id) >= 16:
        changed_id = changed_id[:15]

    while len(changed_id) < 3:
        changed_id += changed_id[len(changed_id) - 1]

    while changed_id[len(changed_id)-1] == '.':
        changed_id = changed_id[:len(changed_id)-1]

    print(changed_id)
    return changed_id


solution("...!@BaT#*..y.abcdefghijklm.")
solution("=.=")
solution("aa")
solution("a")
solution("=weew.q.q")
solution("bb...")