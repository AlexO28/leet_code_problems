# You are given a string s that consists of lowercase English letters.
# A string is called special if it is made up of only a single character. For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.
# Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring occurs at least thrice.
# A substring is a contiguous non-empty sequence of characters within a string.
class Solution:
    def maximumLength(self, s: str) -> int:
        info_dict = {}
        for i in range(len(s)-2):
            for j in range(i+1, len(s)):
                line = s[i:j]
                if len(set(list(line))) != 1:
                    continue
                freq = 1
                if (line not in info_dict) and (len(s)-j >= 2):
                    for k in range(i+1, len(s)-len(line)+1):
                        if self.are_equal(line, s, k):
                            freq += 1
                            if freq == 3:
                                break
                    info_dict[line] = freq
        lines = [key for key in info_dict if info_dict[key] >= 3]
        if len(lines) == 0:
            return -1
        else:
            return max([len(line) for line in lines])

    def are_equal(self, line, s, k):
        for x in range(k, k+len(line)):
            if line[x-k] != s[x]:
                return False
        return True
