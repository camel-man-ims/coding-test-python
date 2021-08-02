# https://www.youtube.com/watch?v=FYCGV6F1NuY
# https://data-jj.tistory.com/34

number= int(input())

def hanoi(n,start,end):
    if n==1:
        print(start,end)
        return
    hanoi(n-1,start,6-start-end)
    print(start,end)
    hanoi(n-1,6-end-start,end)

hanoi(number,1,3)