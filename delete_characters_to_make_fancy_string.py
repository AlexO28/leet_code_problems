# A fancy string is a string where no three consecutive characters are equal.
# Given a string s, delete the minimum possible number of characters from s to make it fancy.
# Return the final string after the deletion. It can be shown that the answer will always be unique.
class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        s = list(s)
        res = []
        res.append(s[0])
        res.append(s[1])
        for j in range(2, len(s)):
            if not((s[j-1] == s[j-2]) and (s[j] == s[j-1])):
                res.append(s[j])
        return "".join(res)
