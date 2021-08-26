n= int(input())

a=0
b=1

while n>0:
   temp = a
   a = b
   b += temp
   # a,b = b,a+b
   n-=1

print(a)