a,b= map(int,input().split(" "))

a_arr = []
b_arr = []

for i in str(a):
    a_arr.append(i)

for i in str(b):
    b_arr.append(i)

a_arr.reverse()
b_arr.reverse()

a_string =""
b_string = ""
for i in a_arr:
    a_string += i
for i in b_arr:
    b_string += i

a_int = int(a_string)
b_int = int(b_string)

print(max(a_int,b_int))
