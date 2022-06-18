n = int(input())

cnt =0
result = []

def hanoi(n,start,end):
    global cnt
    if n==1:
        result.append([start,end])
        cnt+=1
        return

    hanoi(n-1,start,6-start-end)
    result.append([start,end])
    cnt+=1
    hanoi(n-1,6-start-end,end)

hanoi(n,1,3)

print(cnt)

if n<=20:
    for num in result:
        print(str(num[0]) + " " + str(num[1]))
