import sys

n = int(input())

if n==1:
    print("1/1")
    sys.exit(0)

son = 1
mom = 2
count = 2

# flag
# True = down
# False = up
flag = True

while count!=n:
    if flag:
        while mom!=1 and count!=n:
            son+=1
            mom-=1
            count+=1
        if count==n:
            break
        else:
            son+=1
            count+=1
            flag=False
    else:
        while son!=1 and count!=n:
            son-=1
            mom+=1
            count+=1
        if count==n:
            break
        else:
            mom+=1
            count+=1
            flag=True
print(str(son) + "/" + str(mom))


