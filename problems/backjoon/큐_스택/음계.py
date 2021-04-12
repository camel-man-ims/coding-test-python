# 백준 2920번

a = list(map(int,input().split(' ')))

i = len(a)

ascending = True
descending = True

for i in range(1,8):
    # 6 > 5
    if a[i] > a[i-1]:
        descending = False
    elif a[i]<a[i-1]:
        ascending = False


if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')
