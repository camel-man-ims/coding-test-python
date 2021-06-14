# 21.06.14
# 단어가 처음 등장하는 위치 찾기

s = input()

arr = list('abcdefghijklmnopqrstuvwxyz')

hash_map = dict()

for s_ in arr:
    hash_map[s_]=-1

for i in range(len(s)):
    if hash_map[s[i]] != -1:
        pass
    else:
        hash_map[s[i]] = i

for s_ in arr:
    print(hash_map[s_],end=' ')