def dfs(v):
    print(v)
    visited[v]=True
    for num in arr[v]:
        if not visited[num]:
            dfs(num)

arr = [ [] for _ in range(5)]

arr[1].append(2)
arr[1].append(3)
arr[1].append(4)

arr[2].append(1)
arr[2].append(3)

arr[3].append(2)
arr[3].append(4)

arr[4].append(1)
arr[4].append(3)

visited = [False] * 5

dfs(1)


