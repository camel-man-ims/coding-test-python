a,b,v = map(int,input().split())

num1 = v-a
num2 = a-b

temp = num1//num2

if temp==0:
    temp+=1

print(temp+1)