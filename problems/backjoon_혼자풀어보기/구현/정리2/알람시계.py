# 21.06.18

H,M = map(int,input().split())

if M>=45:
    print(H,M-45)
else:
    if H>=1:
        print(H-1,M+15)
    else:
        print(23,M+15)