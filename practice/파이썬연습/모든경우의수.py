N = 5
arr = [0 for _ in range(N)]

def get_all(cnt):
    if cnt==N:
        print(arr)
        return

    for i in range(N):
        arr[cnt] = i
        get_all(cnt+1)

get_all(0)
