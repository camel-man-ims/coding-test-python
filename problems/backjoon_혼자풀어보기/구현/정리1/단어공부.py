# 21.06.08
# 가장 많이 사용된 단어 출력. 가장 많이 사용된 단어와 횟수가 동일하게 사용된 단어 있을 시 ? 출력

import sys

s = input()

s_upper = s.upper()

hash_map = dict()

for s_value in s_upper:
    if s_value in hash_map:
        hash_map[s_value] += 1
    else:
        hash_map[s_value] = 1

keys = hash_map.values()
result =[]

for i in keys:
    result.append(i)

result.sort(reverse=True)

if len(result)==1:
    print(s.upper())
    sys.exit(0)
elif len(result)>=2:
    if result[0]==result[1]:
        print('?')
        sys.exit(0)
    else:
        for hash_s in hash_map:
            if hash_map[hash_s] == result[0]:
                print(hash_s.upper())
                sys.exit(0)