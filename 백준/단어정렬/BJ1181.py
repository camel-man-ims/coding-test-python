import sys

sys.stdin=open("input.txt")

n = int(input())

lst = []

for _ in range(n):
    lst.append(input())

w_list = list(set(lst))

w_list.sort(key=lambda x:(len(x),x[0:]))

print('\n'.join(w_list))
