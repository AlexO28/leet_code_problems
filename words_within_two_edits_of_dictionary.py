# You are given two string arrays, queries and dictionary. All words in each array comprise of lowercase English letters and have the same length.
# In one edit you can take a word from queries, and change any letter in it to any other letter. Find all words from queries that, after a maximum of two edits, equal some word from dictionary.
# Return a list of all words from queries, that match with some word from dictionary after a maximum of two edits. Return the words in the same order they appear in queries.
from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for s in queries:
            for t in dictionary:
                number_of_discrepancies = 0
                found = False
                for i in range(len(s)):
                    if s[i] != t[i]:
                        number_of_discrepancies += 1
                        if number_of_discrepancies > 2:
                            found = True
                            break
                if not found:
                    ans.append(s)
                    break
        return ans
