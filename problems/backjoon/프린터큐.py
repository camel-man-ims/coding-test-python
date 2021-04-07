test_case = int(input())

for _ in range(test_case):
    n, m = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' ')))
    queue_with_index = []
    for i in range(len(queue)):
        value = queue[i]
        index = i
        queue_with_index.append([value, index])

    count = 0

    while True:
        if queue_with_index[0][0] == max(queue_with_index, key=lambda x: x[0])[0]:
            count += 1
            if queue_with_index[0][1] == m:
                print(count)
                break
            else:
                queue_with_index.pop(0)
        else:
            queue_with_index.append(queue.pop(0))
