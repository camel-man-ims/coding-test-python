# 21.04.30
# 에라토스테네스의 체
# https://inten.tistory.com/entry/Python-3x-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%86%8C%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0
# 2부터 n 까지 배수들을 모두 지워준다

n =1000
a = [False,False] + [True]*(n-1)
primes = []

for i in range(2,n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i,n+1,i):
            a[j] = False
print(primes)