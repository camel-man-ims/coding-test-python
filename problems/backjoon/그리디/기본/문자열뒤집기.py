# 21.04.20
# 다시해보기

n = int(input())

zero_count = 0
one_count = 0

n = str(n)
i=0

while i<len(n):
    if n[i] == '0':
        for j in range(i,len(n)):
            if j==len(n)-1 or n[j] != n[j+1]:
                zero_count +=1
                i=j+1
                break
    else:
        i=i+1

i=0
while i<len(n):
    if n[i] == '1':
        for j in range(i,len(n)):
            if j==len(n)-1 or n[j] != n[j+1]:
                one_count +=1
                i=j+1
                break
    else:
        i=i+1

result = min(zero_count,one_count)
print(result)