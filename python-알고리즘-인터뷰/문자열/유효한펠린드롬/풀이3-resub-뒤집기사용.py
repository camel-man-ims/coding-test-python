# re.sub()
# 뒤집기 사용

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = s.lower()
        strs = re.sub("[^a-zA-Z0-9]","",strs)

        return strs == strs[::-1]