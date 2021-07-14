n=int(input())

for _ in range(n):
    H,W,N = map(int,input().split())

    current = 101
    count = 1

    while N!=count:
        if (current+100) // 100 <= H:
            current+=100
            count+=1
        else:
            current = current - (H-1)*100 + 1
            count+=1

    print(current)