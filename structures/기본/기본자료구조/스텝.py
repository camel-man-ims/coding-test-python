# 21.05.11

s = "abcdef"

print(s[-len(s):])
print(s[::-1])
print("===")
print(s[3::-1])
print(s[3:0:-1])

arr = ['abcd','abc','a','asdfsd','af']

arr.sort(key=len,reverse=True)

print(arr)