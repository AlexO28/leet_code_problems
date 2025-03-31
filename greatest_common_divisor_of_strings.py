# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        for j in range(min(len(str1), len(str2))):
            if str1[j] == str2[j]:
                m1, r1 = divmod(len(str1), j+1)
                m2, r2 = divmod(len(str2), j+1)
                if (r1 == 0) and (r2 == 0):
                    if (str1 == str1[:(j+1)] * m1) and (str2 == str2[:(j+1)] * m2):
                        res = str1[:(j+1)]
            else:
                return res
        return res
