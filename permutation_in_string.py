# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq_dict_1 = {}
        for elem in s1:
            if elem in freq_dict_1:
                freq_dict_1[elem] += 1
            else:
                freq_dict_1[elem] = 1
        freq_dict_2 = {}
        for elem in s2[:len(s1)]:
            if elem in freq_dict_2:
                freq_dict_2[elem] += 1
            else:
                freq_dict_2[elem] = 1
        start = 0
        end = len(s1)-1
        while True:
            if freq_dict_1 == freq_dict_2:
                return True
            end += 1
            if end == len(s2):
                break
            if freq_dict_2[s2[start]] == 1:
                del freq_dict_2[s2[start]]
            else:
                freq_dict_2[s2[start]] -= 1
            start += 1
            if s2[end] in freq_dict_2:
                freq_dict_2[s2[end]] += 1
            else: 
                freq_dict_2[s2[end]] = 1
        return False
