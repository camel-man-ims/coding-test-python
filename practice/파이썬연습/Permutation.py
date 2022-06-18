N = 5
R = 3

arr = [0 for _ in range(R)]
v = [False for _ in range(N)]

input_arr = [11,22,33,44,55]

def get_combination(start,cnt):
    if cnt == R:
        print(arr)
        return

    for i in range(start,N):
        arr[cnt] = i
        get_combination(i+1,cnt+1)

# get_combination(0,0)

def get_permutation(cnt):
    if cnt == R:
        print(arr)
        return

    for i in range(N):
        if v[i]:
            continue
        v[i] = True
        arr[cnt] = input_arr[i]
        get_permutation(cnt+1)
        v[i] = False

get_permutation(0)