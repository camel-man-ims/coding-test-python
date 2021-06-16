# 21.06.14

arr = []

for _ in range(10):
    arr.append(int(input()))

set_ = set()

for i in arr:
    set_.add(i%42)

print(len(set_))