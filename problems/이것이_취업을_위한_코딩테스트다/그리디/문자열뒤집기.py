# 21.05.24
# string 인데, '0'을 안붙여줘서 답이 안나왔었다
# 문제나 파이썬 자체를 의심하지 말고, 코드를 의심하자
# 분명히 뭔가 잘못했으니까 제대로 결과가 안나오는 것

s_value = input()

zero_value = 0
one_value = 0

pointer = 0
# case zero
while pointer < len(s_value):
    if s_value[pointer] == '0':
        if pointer==len(s_value)-1 or s_value[pointer] != s_value[pointer+1]:
            zero_value += 1
    else:
        if pointer==len(s_value)-1 or s_value[pointer] != s_value[pointer+1]:
            one_value += 1
    pointer += 1

print(zero_value)
print(one_value)