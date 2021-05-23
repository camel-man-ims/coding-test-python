def solution(n, lost, reserve):
    student = []
    for _ in range(1, n + 1):
        student.append(1)

    for i in lost:
        student[i - 1] = 0

    for i in reserve:
        student[i - 1] += 1

    print(student)

    for i in range(len(student)):
        if i + 1 < len(student) and i - 1 >= 0 and student[i] == 0:
            if student[i - 1] == 2:
                student[i - 1] -= 1
                student[i] += 1
            elif student[i + 1] == 2:
                student[i + 1] -= 1
                student[i] += 1
        elif i == 0:
            if student[0] == 0 and student[i + 1] == 2:
                student[1] -= 1
                student[0] += 1
        elif i == len(student) - 1:
            if student[len(student) - 1] == 0 and student[len(student) - 2] == 2:
                student[len(student) - 1] += 1
                student[len(student) - 2] -= 1
    result = 0
    for i in student:
        if i > 0:
            result += 1
    return result