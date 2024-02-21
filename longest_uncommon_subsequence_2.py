# Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.
# An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.
# A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.
# For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        freq_dict = {}
        for line in strs:
            if line in freq_dict.keys():
                freq_dict[line] = 2
            else:
                freq_dict[line] = 1
        bad_lines = []
        for line in freq_dict.keys():
            if freq_dict[line] == 2:
                bad_lines.append(line)
        max_len = -1
        for line in freq_dict.keys():
            if freq_dict[line] == 1:
                found = False
                for elem in bad_lines:
                    if len(elem) >= len(line):
                        i = 0
                        j = 0
                        while (i < len(elem)) and (j < len(line)):
                            if elem[i] == line[j]:
                                j += 1
                                i += 1
                                if j == len(line):
                                    found = True
                            else:
                                i += 1
                    if found:
                        break
                if not found:
                    max_len = max(max_len, len(line))
        return max_len
