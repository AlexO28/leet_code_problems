# Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.                                                                                                                                                                                                                                     
import numpy as np


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        min_val = int(np.ceil(len(b)/len(a)))
        line = a*min_val
        res = min_val
        for j in range(min_val+1):
            if b in line:
                return res
            else:
                res += 1
                line += a
        return -1
