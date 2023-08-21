# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1:
            return False
        pattern = s[0]
        inpos = 0
        while True:
            if inpos + len(pattern) > len(s):
                return False
            if pattern == s[inpos:(inpos+len(pattern))]:
                inpos += len(pattern)
            else:
                pattern = s[0:(len(pattern)+1)]
                if len(pattern) == len(s):
                    return False
                inpos = len(pattern)
            if inpos >= len(s):
                return True
        return True
