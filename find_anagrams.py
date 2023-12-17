# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = list(p)
        s = list(s)
        p.sort()
        res = []
        for j in range(len(s)-len(p)+1):
            temp = s[j:(j+len(p))]
            temp.sort()
            if temp == p:
                res.append(j)
        return res
