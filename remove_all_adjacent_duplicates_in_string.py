# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.
# We repeatedly make duplicate removals on s until we no longer can.
# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.
class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s) == 1:
            return s
        res = []
        for j in range(len(s)):
            if len(res) == 0:
                res.append(s[j])
            else:
                elem = res.pop()
                if elem != s[j]:
                    res.append(elem)
                    res.append(s[j])
        return "".join(res)
