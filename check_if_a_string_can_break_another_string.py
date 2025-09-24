# Given two strings: s1 and s2 with the same size, check if some permutation of string s1 can break some permutation of string s2 or vice-versa. In other words s2 can break s1 or vice-versa.
# A string x can break string y (both of size n) if x[i] >= y[i] (in alphabetical order) for all i between 0 and n-1.
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        s1.sort()
        s2.sort()
        s1 = "".join(s1)
        s2 = "".join(s2)
        found_1 = 0
        found_2 = 0
        for j in range(len(s1)):
            if s1[j] < s2[j]:
                found_1 += 1
            elif s1[j] > s2[j]:
                found_2 += 1
        return (found_1 == 0) or (found_2 == 0)
