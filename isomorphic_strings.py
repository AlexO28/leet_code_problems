# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        s_ind = 0
        t_ind = 0
        for j in range(len(s)):
            if s[j] in dict_s.keys():
                new_elem_s = dict_s[s[j]]
            else:
                s_ind += 1
                dict_s[s[j]] = s_ind
                new_elem_s = s_ind
            if t[j] in dict_t.keys():
                new_elem_t = dict_t[t[j]]
            else:
                t_ind += 1
                dict_t[t[j]] = t_ind
                new_elem_t = t_ind
            if new_elem_s != new_elem_t:
                return False
        return True
