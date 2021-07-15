import sys

n = int(input())

count = 0

while n>=0:
    if n%5==0:
        count += n//5
        print(count)
        sys.exit(0)
    n-=3
    count+=1

print(-1)
