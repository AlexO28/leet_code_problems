# Given two version numbers, version1 and version2, compare them.
# Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        str1 = version1.split(".")
        str2 = version2.split(".")
        str1 = [int(elem) for elem in str1]
        str2 = [int(elem) for elem in str2]
        i = 0
        while True:
            if (i >= len(str1)) and (i >= len(str2)):
                return 0
            if i >= len(str1):
                elem1 = 0
            else:
                elem1 = str1[i]
            if i >= len(str2):
                elem2 = 0
            else:
                elem2 = str2[i]
            if elem1 > elem2:
                return 1
            elif elem1 < elem2:
                return -1
            i += 1
        return 0
