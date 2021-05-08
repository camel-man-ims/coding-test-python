# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n= int(input())
li = []
for _ in range(n):
    m = int(input())
    li.append(m)
result = 0

if n%2==0:
    for i in range(1,n):
        result += li[i]
else:
    for i in range(0,n):
        result += li[i]

print(result)