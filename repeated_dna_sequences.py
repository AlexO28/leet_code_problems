# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        arr = set()
        res = []
        for j in range(len(s)-9):
            substr = s[j:(j+10)]
            if substr not in arr:
                arr.add(substr)
            else:
                if substr not in res:
                    res.append(substr)
        return res
