# 22.07.07

import sys
from itertools import permutations

sys.stdin = open('input.txt', 'rt')

n = int(input())
lst = list(map(int,input().split()))

res = list(permutations(lst,n))

max_value = 0
for res_list in res:
    temp_sum = 0
    for i in range(1,n):
        temp_sum += abs(res_list[i] -res_list[i-1])
    max_value = max(max_value,temp_sum)

print(max_value)

