# 21.05.12

def palindrome(s):
    if len(s)<=1:
        return True

    if s[0] == s[1]:
        return palindrome(s[1:-1])
    else:
        return False

