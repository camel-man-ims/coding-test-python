# 22.07.07

s = "ABCD"
print(s[1:3])

print("---------")

# 튜플 : 리스트랑 비슷하지만 final
tup = (1, 2, 3, 4)
print(tup)

print("-----")

hashMap = dict()
hashMap["a"] = 1
hashMap["b"] = 2
print(hashMap)

for key in hashMap:
    print(hashMap[key])

sArr = ["a", "c"]

for s in sArr:
    if s in hashMap:
        print(hashMap[s])
    else:
        hashMap[s] = 3

print(hashMap)

print(hashMap.keys())
print(hashMap.values())

print("-------")

# set([1,2,3])
hashSet = {1, 2, 3, 4, 2}
hashSetB = {1,6,7,8}

print(hashSet | hashSetB)
print(hashSet & hashSetB)
print(hashSet - hashSetB)

hashSet.add(3)
hashSet.update([10,20,30])
hashSet.remove(3)

print(hashSet)

print("---------")

print(1<<3)