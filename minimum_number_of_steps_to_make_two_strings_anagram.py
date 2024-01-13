# You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.
# Return the minimum number of steps to make t an anagram of s.
# An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_dict = {}
        for elem in s:
            if elem in s_dict:
                s_dict[elem] += 1
            else:
                s_dict[elem] = 1
        t_dict = {}
        for elem in t:
            if elem in t_dict:
                t_dict[elem] += 1
            else:
                t_dict[elem] = 1
        t_keys = list(t_dict.keys())
        t_keys.sort()
        s_keys = list(s_dict.keys())
        count = 0
        for elem in t_keys:
            if elem not in s_keys:
                count += t_dict[elem]
            else:
                count += abs(t_dict[elem] - s_dict[elem])
        s_keys = [s for s in s_keys if s not in t_keys]
        for elem in s_keys:
            count += s_dict[elem]
        return count // 2
