# 21.05.05
# 테스트케이스 1번에 대해서만 통과 못하는데, 왜 통과 못하는지 모르겠다
# 옷을 고를 수 있는 경우의 수를 구하는 문제

from itertools import combinations

def solution(clothes):
    hash_map = dict()
    for s in clothes:
        if hash_map.get(s[1]):
            hash_map[s[1]] += 1
        else:
            hash_map[s[1]] = 1
    result=0
    int_arr = []

    for i in hash_map.values():
        int_arr.append(i)

    for i in range(1,len(int_arr)+1):
        comb = list(combinations(int_arr,i))
        for j in comb:
            temp_multiple =1
            if len(j)==1:
                result += j[0]
            else:
                for k in j:
                    temp_multiple *= k
                result += temp_multiple
    print(result)
    return result

# A 4 B 2 C 1
# 4+2+1 4*2 4*1 4*2*1 2*1 = 29
solution([["q", "A"], ["w", "B"], ["e", "C"],["q", "A"],["q", "A"],["q", "A"],["q", "B"]])
