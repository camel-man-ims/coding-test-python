# 21.05.07
# 문자열 압축 문제
# a3b5a9c4c5
# =>
# a12b5c9 식으로 출력

s = input()

result = ""
pointer = 0
alpha_turn = dict()
hash_list = dict()

alpha_list = []
num_list = []

for i in range(0,len(s)):
    if s[i].isalpha():
        alpha_list.append(i)
        if not s[i] in alpha_turn:
            alpha_turn[s[i]] = pointer
            pointer +=1

for i in range(len(alpha_list)-1):
    start = alpha_list[i]
    end = alpha_list[i+1]
    num = s[start+1:end]
    num_list.append(int(num))

end_number = int(s[alpha_list[len(alpha_list)-1]+1:len(s)])
num_list.append(end_number)

for i in range(len(alpha_list)):
    if s[alpha_list[i]] in hash_list:
        hash_list[s[alpha_list[i]]] += num_list[i]
    else:
        hash_list[s[alpha_list[i]]] = num_list[i]

pointer=0
result = []
for _ in range(len(hash_list)):
    for h1 in hash_list:
        if alpha_turn[h1] == pointer:
            result.append(h1)
            result.append(hash_list[h1])
            pointer+=1

s_result = ""
for value in result:
    s_result += str(value)

print(s_result)