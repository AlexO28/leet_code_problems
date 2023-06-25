# We can scramble a string s to get a string t using the following algorithm:
# If the length of the string is 1, stop.
# If the length of the string is > 1, do the following:
# Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
# Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
# Apply step 1 recursively on each of the two substrings x and y.
# Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.


import numpy as np


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        sSize = len(s1)
        if sSize == 1:
            return s1 == s2
        isS = np.full([sSize + 1, sSize, sSize], False)         
        for i in range(sSize):
            for j in range(sSize):
                isS[1][i][j] = (s1[i] == s2[j])
        for length in range(2, sSize + 1):
            for i in range(0, sSize - length + 1):
                for j in range(0, sSize - length + 1):
                    for k in range(1, length):
                        isS[length][i][j] = isS[length][i][j] or (isS[k][i][j] and isS[length-k][i+k][j+k])
                        isS[length][i][j] = isS[length][i][j] or (isS[k][i+length-k][j] and isS[length-k][i][j+k])
        return isS[sSize][0][0]
