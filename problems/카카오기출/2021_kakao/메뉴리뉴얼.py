from itertools import combinations


def convert(s):
    new = ""
    for x in s:
        new += x
    return new

def anagram(s):
    arr = [0 for _ in range(26)]


def solution(orders, course):
    hash_map = dict()
    s_arr = []

    for order in orders:
        for num in course:
            c_arr = list(combinations(order,num))
            for c in c_arr:
                s_arr.append(convert(c))
    for s in s_arr:
        if s in hash_map:
            hash_map[s]+=1
        else:
            hash_map[s]=1

    result = []
    print(hash_map)

    for num in course:
        max_value = 0
        for s in hash_map:
            if len(s)==num:
                max_value = max(max_value,hash_map[s])
        for s in hash_map:
            if hash_map[s]==max_value and len(s)==num and hash_map[s]>=2:
                result.append(s)
    result.sort()
    return result




# solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])
solution(["XYZ", "XWY", "WXA"],[2,3,4])