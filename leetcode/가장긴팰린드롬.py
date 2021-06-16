# https://leetcode.com/problems/longest-palindromic-substring/

def longestPalindrome(s):
    if len(s)<2 or s == s[::-1]:
        return s
    max_ = ""
    for i in range(len(s)):

        max_ = max(max_,expand(i,i+1,s),expand(i,i+2,s),key=len)
    return max_

def expand(left,right,s):
    while left>=0 and right<len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]


palindrome= longestPalindrome("123456")
print(palindrome)
