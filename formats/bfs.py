from collections import deque

data = [
    [1, 1, 1, 0],
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 1]
]

m = len(data)
n = len(data[0])

dirs = [
    [-1, 0], [1, 0], [0, -1], [0, 1]
]


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    while queue:
        poll = queue.popleft()
        x1 = poll[0]
        y1 = poll[1]
        data[x1][y1] = 7

        for arr in dirs:
            x2 = x1+arr[0]
            y2 = y1+arr[1]
            if 0<x2<m and 0<y2<n and data[x2][y2]==1:
                queue.append([x2,y2])
        print(queue)

def solution():
    count = 0
    for i in range(m):
        for j in range(n):
            if data[i][j] == 1:
                count = count + 1
                bfs(i, j)
    return count


count1= solution()
print(count1)

for i in data:
    print(i)