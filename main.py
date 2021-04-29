n = 1000
marked = [False,False] + [True] * (n-1)
prime_numbers = []

for i in range(2,n+1):
    if marked[i]:
        prime_numbers.append(i)
    for j in range(2*i,n+1,i):
        marked[j]=False

print(prime_numbers)