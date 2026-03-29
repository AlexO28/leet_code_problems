# You are given two strings s1 and s2, both of length 4, consisting of lowercase English letters.
# You can apply the following operation on any of the two strings any number of times:
# Choose any two indices i and j such that j - i = 2, then swap the two characters at those indices in the string.
# Return true if you can make the strings s1 and s2 equal, and false otherwise.
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        for i in range(3):
            for j in range(3):
                new_s1 = s1.copy()
                new_s2 = s2.copy()
                if i == 1:
                    new_s1[0], new_s1[2] = new_s1[2], new_s1[0]
                elif i == 2:
                    new_s1[1], new_s1[3] = new_s1[3], new_s1[1]
                if j == 1:
                    new_s2[0], new_s2[2] = new_s2[2], new_s2[0]
                elif j == 2:
                    new_s2[1], new_s2[3] = new_s2[3], new_s2[1]
                if new_s1 == new_s2:
                    return True
        return False
