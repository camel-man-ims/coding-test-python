# 문자 정렬 후 잇기
s = "rewrewsaewq"
print(''.join(sorted(s)))

# 길이로 정렬
sArr = ['aaaa','bb','ccccccc','d']
print(sorted(sArr,key=len,reverse=True))

# 첫, 마지막을 key로 정렬
sArr = ['sdqas','aadwqs','cdwewq','ber']

def fn(s):
    return s[0],s[-1]

print(sorted(sArr,key=fn))

# lambda 이용 정렬
print(sorted(sArr,key=lambda x: (x[0],x[-1])))