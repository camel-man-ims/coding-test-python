number = int(input())

arr = [0 for _ in range(300)]

def fibonacci(n):
    if n==0:
        return 0
    if n<=2:
        return 1
    if arr[n]==0:
        arr[n] = fibonacci(n-1)+fibonacci(n-2)
        return arr[n]
    else:
        return arr[n]

print(fibonacci(number))