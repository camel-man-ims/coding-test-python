# 21.05.16
# https://velog.io/@dldhk97/%EC%9E%AC%EA%B7%80%ED%95%A8%EC%88%98%EC%99%80-%EA%BC%AC%EB%A6%AC-%EC%9E%AC%EA%B7%80

def factorial_tail(n,acc):
    if n==1:
        return acc
    return factorial_tail(n-1,acc*n)


tail = factorial_tail(7,1)
print(tail)