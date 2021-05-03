# 21.05.03
# 순열로 모든 수의 조합을 구해서, 소수인지 확인하는 문제

from itertools import permutations

import math

def is_prime(x):
    if x<=1:
        return False
    end = int(math.sqrt(x))
    # end <=2 일때 오류나서 틀렸었음
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

def solution(numbers):
    result = 0
    num_list = []

    for i in range(1,len(numbers)+1):
        p_list = list(permutations(numbers,i))
        for arr in p_list:
            s = "".join(arr)
            num_list.append(int(s))

    print(num_list)
    num_list_remove_duplicate = list(set(num_list))
    print(num_list_remove_duplicate)

    for num in num_list_remove_duplicate:
        if is_prime(int(num)):
            result +=1
    return result

print(solution('011'))









