a = "abcde"
b = "ab"

for i in range(len(a)-len(b)+1):
    print(a[i:i+len(b)])
