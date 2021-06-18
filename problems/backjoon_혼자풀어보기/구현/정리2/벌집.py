# 1 6 12 18 ...
# 6n
# ex) 30 4번째
# total=0
import sys

six_add = 6
count = 2
n= int(input())

if n==1:
    print(1)
    sys.exit(0)

n-=1

while n>six_add:
    count+=1
    n -= six_add
    six_add+=6

print(count)


