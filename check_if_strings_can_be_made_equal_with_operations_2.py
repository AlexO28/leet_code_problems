# You are given two strings s1 and s2, both of length n, consisting of lowercase English letters.
# You can apply the following operation on any of the two strings any number of times:
# Choose any two indices i and j such that i < j and the difference j - i is even, then swap the two characters at those indices in the string.
# Return true if you can make the strings s1 and s2 equal, and false otherwise.
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        new_s11 = []
        new_s12 = []
        for j in range(len(s1)):
            if j % 2 == 0:
                new_s11.append(s1[j])
            else:
                new_s12.append(s1[j])
        new_s21 = []
        new_s22 = []
        for j in range(len(s2)):
            if j % 2 == 0:
                new_s21.append(s2[j])
            else:
                new_s22.append(s2[j])
        new_s11.sort()
        new_s12.sort()
        new_s21.sort()
        new_s22.sort()
        return (new_s11 == new_s21) and (new_s12 == new_s22)
