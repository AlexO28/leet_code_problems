# You are given a string s that consists of only digits.
# Check if we can split s into two or more non-empty substrings such that the numerical values of the substrings are in descending order and the difference between numerical values of every two adjacent substrings is equal to 1.
# For example, the string s = "0090089" can be split into ["0090", "089"] with numerical values [90,89]. The values are in descending order and adjacent values differ by 1, so this way is valid.
# Another example, the string s = "001" can be split into ["0", "01"], ["00", "1"], or ["0", "0", "1"]. However all the ways are invalid because they have numerical values [0,1], [0,1], and [0,0,1] respectively, all of which are not in descending order.
# Return true if it is possible to split s​​​​​​ as described above, or false otherwise.
# A substring is a contiguous sequence of characters in a string.
class Solution:
    def splitString(self, s: str) -> bool:
        self.s = s
        return self.search(0, -1)

    def search(self, i, x):
        if i >= len(self.s):
            return True
        y = 0
        if x < 0:
            r = len(self.s) - 1
        else:
            r = len(self.s)
        for j in range(i, r):
            y = y * 10 + int(self.s[j])
            if ((x < 0) or (x - y == 1)) and self.search(j + 1, y):
                return True
        return False
