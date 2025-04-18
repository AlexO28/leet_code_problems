# You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.
# Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        indices = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                indices.append(i)
                if len(indices) > 2:
                    return False
        if len(indices) == 0:
            return True
        elif len(indices) == 1:
            return False
        else:
            return (s1[indices[0]] == s2[indices[1]]) and (s2[indices[0]] == s1[indices[1]])
