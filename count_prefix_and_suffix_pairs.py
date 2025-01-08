# You are given a 0-indexed string array words.
# Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:
# isPrefixAndSuffix(str1, str2) returns true if str1 is both a 
# prefix
#  and a 
# suffix
# of str2, and false otherwise.
# Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i], words[j]) is true.
from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        if len(words) == 1:
            return 0
        res = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if len(words[i]) == len(words[j]):
                    if words[i] == words[j]:
                        res += 1
                elif len(words[i]) < len(words[j]):
                    found = False
                    for k in range(len(words[i])):
                        if words[i][k] != words[j][k]:
                            found = True
                            break
                    if not found:
                        for k in range(len(words[i])):
                            if words[i][-k-1] != words[j][-k-1]:
                                found = True
                                break
                    if not found:
                        res += 1
        return res
