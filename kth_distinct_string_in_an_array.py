# A distinct string is a string that is present only once in an array.
# Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".
# Note that the strings are considered in the order in which they appear in the array.
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq_dict = {}
        for elem in arr:
            if elem in freq_dict:
                freq_dict[elem] = 1
            else:
                freq_dict[elem] = 0
        string_dict = {}
        for key in freq_dict.keys():
            if freq_dict[key] == 0:
                string_dict[key] = 0
        if len(string_dict.keys()) < k:
            return ""
        string_counter = 0
        for elem in arr:
            if elem in string_dict:
                string_counter += 1
                if string_counter == k:
                    return elem
