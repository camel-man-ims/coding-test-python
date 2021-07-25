# 21.07.23
# n보다 크고, 2n보다 작거나 같은 소수의 개수

def get_prime(m):
    n = 2*m
    arr = [False,False] + [True] * n
    result = []

    for i in range(2,n+1):
        if arr[i]:
            if i>m:
                result.append(i)
            for j in range(2*i,n+1,i):
                arr[j] = False
    return result

while True:
    n = int(input())
    if n==0:
        break
    print(len(get_prime(n)))


