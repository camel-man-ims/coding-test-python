import sys

sys.stdin = open("input.txt")

iv = input()
n = len(iv)
hash_set = set()

for i in range(1, n + 1):
    for j in range(n-i+1):
        s = iv[j:j + i]

        if s not in hash_set:
            hash_set.add(s)

print(len(hash_set))