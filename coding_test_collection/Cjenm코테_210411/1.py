# url 이 들어왔을 때 keys[] 도 같이 주어진다
# ex) https://google.com?abcd=1234&bcdd=4321
# 이때 , keys[]의 값이 abcd 면 abcd 만 있는 부분의 URL 만 반환하기
# ex) http://google.com?abcd=1234

url = "https://google.com?abcd=1234&bcdd=4321&abcd=3421"
keys = ["abcd"]

word = "com"
com_index=0

for i in range(len(url)):
    j = i+3
    com_value = url[i:j]
    if com_value == word:
        com_index=j

com_ = url[0:com_index] + str('?')
result = ""

for i in range(com_index,len(url)):
    for w in keys:
        j = i + len(w)
        word_value = url[i:j]
        if word_value == w:
            for k in range(i,len(url)):
                if url[k] =='&' or k==len(url)-1:
                    result += url[i:k+1]
                    break

com_ += result

print(com_)
