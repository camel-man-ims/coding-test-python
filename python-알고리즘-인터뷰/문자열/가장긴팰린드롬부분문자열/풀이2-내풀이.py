# 22.07.13
# 파이썬으로 풀어보기

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if len(s) < 2 or s == s[::-1]:
            return s

        def palin(start: int, end: int) -> str:
            if end > n:
                return ""
            while start >= 0 and end < n and s[start] == s[end]:
                start -= 1
                end += 1
            start += 1
            end -= 1
            return s[start:end+1]

        res = ''
        for i in range(len(s)):
            res = max(res,palin(i, i+1), palin(i, i+2),key=len)

        return res

sol = Solution()
palindrome= sol.longestPalindrome("babad")
print(palindrome)
