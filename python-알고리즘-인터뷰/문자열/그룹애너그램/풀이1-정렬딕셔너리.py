import collections

# 22.07.07

class Solution:
    def groupAnagrams(self, strs):
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())