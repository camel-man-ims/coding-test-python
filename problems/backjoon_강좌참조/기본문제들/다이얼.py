# 21.05.02

hash_map = dict()

hash_map["A"]=2
hash_map["B"]=2
hash_map["C"]=2

hash_map["D"]=3
hash_map["E"]=3
hash_map["F"]=3

hash_map["G"]=4
hash_map["H"]=4
hash_map["I"]=4

hash_map["J"]=5
hash_map["K"]=5
hash_map["L"]=5

hash_map["M"]=6
hash_map["N"]=6
hash_map["O"]=6

hash_map["P"]=7
hash_map["Q"]=7
hash_map["R"]=7
hash_map["S"]=7

hash_map["T"]=8
hash_map["U"]=8
hash_map["V"]=8

hash_map["W"]=9
hash_map["X"]=9
hash_map["Y"]=9
hash_map["Z"]=9

s = input()

result = 0

for s_val in s:
    result += hash_map[s_val] +1

print(result)

