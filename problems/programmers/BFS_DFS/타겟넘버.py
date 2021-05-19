# 21.05.19

from collections import deque

def solution(numbers, target):

    queue = deque()
    queue.append((numbers[0],0))
    queue.append((-1*numbers[0],0))

    length = len(numbers)
    result = 0

    while queue:
        temp,idx  = queue.popleft()
        idx +=1
        if idx < length:
            queue.append((temp+numbers[idx],idx))
            queue.append((temp-numbers[idx],idx))
        else:
            if temp == target:
                result +=1

    return result

print(solution([1,1,1,1,1],3))