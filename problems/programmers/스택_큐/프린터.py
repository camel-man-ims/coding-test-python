from collections import deque

def solution(priorities, location):
    queue = deque()
    index=0
    for num in priorities:
        queue.append((index,num))
        index +=1
    count =0

    print(queue)

    while True:
        if queue[0][1] == max(queue, key=lambda x: x[1])[1]:
            count +=1
            if location == queue[0][0]:
                return count
            else:
                queue.popleft()
        else:
            queue.append(queue.popleft())


pro = [1,1,9,1,1,1]
location = 0

i= solution(pro, location)
print(i)

