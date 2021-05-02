# 21.05.02
# 맞은거같은데 런타임에러
# 에러처리가 제대로 안되는듯
import sys

s = input()

s_lower =s.lower()

hash_map = dict()

for s_value in s_lower:
    if s_value in hash_map:
        hash_map[s_value] += 1
    else:
        hash_map[s_value] = 1

temp_arr = []
for i in hash_map:
    temp_arr.append((i,hash_map[i]))

temp_arr.sort(key=lambda x:x[1],reverse=True)

pop_1 = temp_arr.pop(0)

if len(temp_arr) >=2:
    pop_2 = temp_arr.pop(0)

    if pop_1[1] == pop_2[1]:
        print("?")
        sys.exit(0)
    else:
        print(pop_1[0].upper())
        sys.exit(0)
print(pop_1[0].upper())
