# 21.05.02
# 답은 맞는것 같은데 정답처리가 안됨

input_string = input()

array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# = list('abcd....z') 이렇게하면 하나하나 리스트 된다
compare = dict()

result = []

for i in range(len(input_string)):
    if input_string[i] not in compare:
        compare[input_string[i]]=i

for iter_value in array:
    if iter_value in compare:
        result.append(compare[iter_value])
    else:
        result.append(-1)

print(result)