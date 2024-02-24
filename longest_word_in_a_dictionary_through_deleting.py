# Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by deleting some of the given string characters. If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dict_info = {}
        for line in dictionary:
            if len(line) <= len(s):
                if len(line) in dict_info:
                    dict_info[len(line)].append(line)
                else:
                    dict_info[len(line)] = [line]
        lengths = list(dict_info.keys())
        lengths.sort(reverse = True)
        for line_len in lengths:
            values = dict_info[line_len]
            values.sort()
            for value in values:
                i = 0
                j = 0
                found = False
                while (i < len(value)) and (j < len(s)):
                    if (s[j] == value[i]):
                        j += 1
                        i += 1
                    else:
                        j += 1
                    if i == len(value):
                        found = True
                if found:
                    return value
        return ""
