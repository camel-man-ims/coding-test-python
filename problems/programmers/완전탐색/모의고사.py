# 21.04.30

def solution(answers):
    n1 = [1,2,3,4,5]
    n2 = [2,1,2,3,2,4,2,5]
    n3 = [3,3,1,1,2,2,4,4,5,5]
    answer = []

    pointer=0
    count1=0
    count2=0
    count3=0

    for num in answers:
        if pointer == 5:
            pointer=0
        if num == n1[pointer]:
            count1 +=1
        pointer +=1

    pointer=0
    for num in answers:
        if pointer == 8:
            pointer=0
        if num == n2[pointer]:
            count2 +=1
        pointer +=1

    pointer=0
    for num in answers:
        if pointer == 10:
            pointer=0
        if num == n3[pointer]:
            count3 +=1
        pointer +=1

    result = []
    result.append((1,count1))
    result.append((2,count2))
    result.append((3,count3))

    result.sort(key=lambda x:x[1],reverse=True)
    po = result.pop(0)
    first_value = po[1]
    first_index = po[0]
    answer.append(first_index)
    for _ in range(2):
        pop = result.pop(0)
        if pop[1] == first_value:
            answer.append(pop[0])

    answer.sort()

    return answer


l = solution([1, 2,3,4,5])
print(l)