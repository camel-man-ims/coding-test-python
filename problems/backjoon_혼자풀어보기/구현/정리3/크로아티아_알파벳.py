s_input = input()

i=0

hash_set = set()

hash_set.add("c=")
hash_set.add("c-")
hash_set.add("dz=")
hash_set.add("d-")
hash_set.add("lj")
hash_set.add("nj")
hash_set.add("s=")
hash_set.add("z=")

count =0

while i<len(s_input):
    word_three = s_input[i:i+3]
    word_two = s_input[i:i+2]

    if word_two in hash_set:
        i = i+2
        count +=1
    elif word_three in hash_set:
        i = i+3
        count +=1
    else:
        i = i+1
        count +=1

print(count)

