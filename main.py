s = "abcdef"

print(s[-len(s):])
print(s[::-1])

arr = ['abcd','abc','a','asdfsd','af']

arr.sort(key=len,reverse=True)

print(arr)