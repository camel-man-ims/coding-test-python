from itertools import combinations

def solution(numbers):
    num_array = []
    for num in str(numbers):
        num_array.append(int(num))

    print(num_array)
    answer = 0
    return answer

def find_prime_number(num):
    pass


n = 1000000
marked = [False,False] + [True] * (n-1)
prime_numbers = []
for i in range(2,n+1):
    if marked[i]:
        prime_numbers.append(i)
    for j in range(2*i,n+1,i):
        marked[j]=False

solution1 = solution(17)

