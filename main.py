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


def solution():
    count = 0
    for i in range(m):
        for j in range(n):
            if data[i][j] == 1:
                count += 1
                dfs(i, j)
    return count


def dfs(i, j):
    if i > m - 1 or i < 0 or j > n - 1 or j < 0 or data[i][j]!=1:
        return False

    data[i][j] = 7

    for a in dirs:
        dfs(i+a[0],i+a[1])


i = solution()

for i in data:
    print(i)
