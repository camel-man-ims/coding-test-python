# 21.06.16

# s = input()
s= input()

zero_value = 0
one_value = 0

for i in range(len(s)):
    if s[i]=='1' and (i==len(s)-1 or s[i]!=s[i+1]):
        zero_value+=1

for i in range(len(s)):
    if s[i]=='0' and (i==len(s)-1 or s[i]!=s[i+1]):
        one_value+=1

print(min(one_value,zero_value))


