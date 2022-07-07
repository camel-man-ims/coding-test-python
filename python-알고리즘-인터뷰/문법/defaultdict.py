# 22.07.07
# https://www.daleseo.com/python-collections-defaultdict/

# 1번 방법
import collections

def countLetters(word):
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter

# 2번 방법
def setDefault(word):
    counter = {}
    for letter in word:
        counter.setdefault(letter,0)
        counter[letter] += 1
    return counter

def defaultDict(word):
    counter = collections.defaultdict(int)

    for letter in word:
        counter[letter] += 1
    return counter

c = defaultDict("abcwess")
print(list(c.values()))