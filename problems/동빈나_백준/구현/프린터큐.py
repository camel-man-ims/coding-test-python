from collections import deque

n = int(input())

for _ in range(n):
    num_range, find_index = map(int,input().split())
    arr = list(map(int,input().split()))

    queue = deque()
    index = 0
    result = []

    for i in range(len(arr)):
        queue.append([arr[i],index])
        index+=1

    while queue:
        max_value = max(queue)
        if queue[0][0] >= max_value[0]:
            pop_value = queue.popleft()
            result.append(pop_value[1])
        else:
            pop_value = queue.popleft()
            queue.append(pop_value)

    for i in range(len(result)):
        if result[i] == find_index:
            print(i+1)

