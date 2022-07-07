# 22.07.07
# https://leetcode.com/problems/most-common-word/
import collections
import re

# counts.most_common 함수 example
# [('ball', 2), ('bob', 1), ('a', 1)]
# print(counts.most_common(3))

class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        words = [word for word in re.sub('[^\w]',' ',paragraph).lower().split() if word not in banned]
        w = [word for word in re.sub('[^\w]',' ', paragraph).split()]
        print(w)
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]

sol = Solution()
sol.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.","hit")