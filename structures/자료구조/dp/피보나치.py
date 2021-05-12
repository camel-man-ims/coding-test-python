arr = [0 for _ in range(300)]

arr[1]=1
arr[2]=1

def fibonacci(n):
    if arr[n] == 0:
        arr[n] = fibonacci(n-1)+ fibonacci(n-2)
        return arr[n]
    else:
        return arr[n]

print(fibonacci(100))