# 21.07.21

def is_prime(number):
    for i in range(2,number):
        if number % i ==0:
            return False
    return True

N = 100

arr = []

arr.append(2)

for i in range(3,N):
    if is_prime(i):
        arr.append(i)

print(arr)