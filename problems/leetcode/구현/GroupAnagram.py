# 21.05.10
# 같은 요소로 이루어진 단어인지 확인하는 문제
# 단어 정렬 후, hash set 에 추가한 다음 반환

class Solution:
    def groupAnagrams(self,li):
        hash_set = dict()

        for word in li:
            # 그냥 단어 sorted 하면 character 나옴
            sorted_word = ''.join(sorted(word))
            # hash set 에 없으면 list 생성해줌
            if sorted_word not in hash_set:
                hash_set[sorted_word] = []
            hash_set[sorted_word].append(word)
        result = []

        for arr in hash_set.values():
            result.append(arr)

        return result

test = Solution()

anagrams = test.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(anagrams)