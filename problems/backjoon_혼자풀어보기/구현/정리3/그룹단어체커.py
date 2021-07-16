# set 에 저장
# set 에 있을 때, 전의 값이랑 같으면 통과
# set 에 있는데, 전의 값이랑 다르면 나가리

n = int(input())

result = 0

for _ in range(n):
    s = input()
    hash_set = set()
    flag = True
    for i in range(len(s)):
        if s[i] not in hash_set:
            hash_set.add(s[i])
            i += 1
        elif s[i] in hash_set:
            if s[i-1] == s[i]:
                i+=1
            elif s[i-1] != s[i]:
                flag=False
                break
    if flag:
        result+=1

print(result)