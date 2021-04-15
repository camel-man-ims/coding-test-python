# 21.04.15
# 문제 잘못 읽어서 index +=1 해야하는데, index +=3 해버림

s = input()
find = input()
count = 0
index = 0

while len(s)-index >= len(find):
    find_ = s[index:index + len(find)]
    if find_ == find:
        count += 1
        index += len(find)
    else:
        index +=1

print(count)