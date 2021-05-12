# 백준 5397번

def solution(db):
    pointer = 0

    result = []

    for i in range(len(db)):
        d = db.pop(0)

        if d.isalpha() or d.isdigit():
            result.insert(pointer, d)
            pointer += 1
        else:
            if d == '<' and pointer > 0:
                pointer -= 1
            elif d == '>' and pointer < len(db):
                pointer += 1
            elif d == '-':
                pointer -= 1
                del result[pointer]

    re = ""

    for i in result:
        re += i
    return re

sol = []

n = int(input())
for _ in range(n):
    data = list(map(str, input()))
    res = solution(data)
    sol.append(res)

for i in range(len(sol)):
    print(''.join(sol[i]))




