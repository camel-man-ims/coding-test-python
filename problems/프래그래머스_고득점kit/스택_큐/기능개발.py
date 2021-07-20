# 21.07.18

def solution(progresses, speeds):
    index = 0
    length = len(progresses)

    result = []

    while index<length:
        count = 1

        for i in range(length):
            progresses[i] += speeds[i]

        if progresses[index] >=100:
            index +=1
            while index<length and progresses[index]>=100:
                index+=1
                count+=1

            result.append(count)
    return result


solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])