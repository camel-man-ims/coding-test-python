n,m = map(int,input().split())

hm  = dict()

for _ in range(n):
    s: list = input().split()
    hm[s[0]] = s[1]

for _ in range(m):
    s: str = input()
    print(hm[s])