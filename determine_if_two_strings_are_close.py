# Two strings are considered close if you can attain one from the other using the following operations:
# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.
# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        freq_dict_1 = {}
        for elem in word1:
            if elem in freq_dict_1:
                freq_dict_1[elem] += 1
            else:
                freq_dict_1[elem] = 1
        freq_dict_2 = {}
        for elem in word2:
            if elem in freq_dict_2:
                freq_dict_2[elem] += 1
            else:
                freq_dict_2[elem] = 1
        keys1 = list(freq_dict_1.keys())
        keys2 = list(freq_dict_2.keys())
        keys1.sort()
        keys2.sort()
        if keys1 != keys2:
            return False
        vals1 = list(freq_dict_1.values())
        vals2 = list(freq_dict_2.values())
        vals1.sort()
        vals2.sort()
        return vals1 == vals2
