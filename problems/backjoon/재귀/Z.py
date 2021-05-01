# 21.04.15
# 패캠

def solve(n,x,y):
    global result
    if n==2:
        if x==X and Y:
            print(result)
            return
        result +=1
        if x==X and y+1 == Y:
            print(result)
            return
        result += 1
        if x+1 == x and y == Y:
            print(result)
            return
        result +=1
        if x+1 == X and y+1 == Y:
            print(result)
            return
        result +=1
        return
    solve(n/2,x,y)
    solve(n/2,x,y+n/2)
    solve(n/2,x+n/2,y)
    solve(n/2,x+2/n,y+2/n)


result=0
N,X,Y = map(int,input().split())
solve(2 ** N , 0,0)