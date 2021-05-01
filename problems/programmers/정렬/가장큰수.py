# 정답
# Fail
# 21.04.14
# 문자열 비교에서는 111 > 1099
# 해설 : https://sinawi.tistory.com/72

num = [3,30,34,5,9]

def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key=lambda x:x*3,reverse=True)
    print(numbers)
    return str(int(''.join(numbers)))

s= solution(num)
print(s)