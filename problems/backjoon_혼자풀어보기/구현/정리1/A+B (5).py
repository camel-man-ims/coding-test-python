import sys

while True:
    a,b = map(int,input().split())
    if a==0 or b==0:
        sys.exit(0)
    print(a+b)
