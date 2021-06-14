# 21.06.14
# 한수 구하기 ( 각 자리가 등차수열을 이루는 수 )

n= int(input())

if n<100:
    print(n)
else:
    target = 100
    result = 99
    while target<=n:
        first = int(str(target)[0])
        middle = int(str(target)[1])
        last = int(str(target)[2])

        if first - middle == middle-last or middle - first == last - middle:
            result+=1
        target+=1
    print(result)