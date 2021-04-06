s = "K1KA57CB7"

result = []
value=0

for i in s:
    if i.isalpha():
        result.append(i)
    else:
        value = value + int(i)

result.sort()

result_string =""

for i in result:
    result_string = result_string + i

result_string = result_string + str(value)

print(result_string)

