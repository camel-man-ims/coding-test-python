import sys

n = int(input())

if n==0:
    print(1)
    sys.exit(0)

target = 0
count = 0

ten,one=0,0

while target != n:
    if count==0:
        ten = n//10
        one = n%10
    else:
        ten = target//10
        one = target%10

    temp = ten+one

    new_one = temp%10
    target = one*10 + new_one
    count +=1

print(count)
