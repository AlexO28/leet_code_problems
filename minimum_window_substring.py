# Given two strings s and t of lengths m and n respectively, return the minimum window substring
# of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = len(t)
        require = [0] * 128
        chSet = [False] * 128
        for i in range(count):
            require[ord(t[i])] += 1
            chSet[ord(t[i])] = True
        i = -1
        j = 0
        minLen = 999999999
        minIdx = 0
        while i < len(s) and j < len(s):
            if count > 0:
                i += 1
                if i == len(s):
                    index = 0
                else:
                    index = ord(s[i])
                require[index] -= 1
                if chSet[index] and require[index] >=0:
                    count -= 1
            else:
                if minLen > i - j + 1:
                    minLen = i - j + 1
                    minIdx = j
                require[ord(s[j])] += 1
                if chSet[ord(s[j])] and require[ord(s[j])] > 0:
                    count += 1
                j += 1
        if minLen == 999999999:
            return ""
        return s[minIdx:minIdx+minLen]
