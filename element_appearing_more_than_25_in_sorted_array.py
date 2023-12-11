# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq_dict = {}
        for elem in arr:
            if elem not in freq_dict:
                freq_dict[elem] = 1
            else:
                freq_dict[elem] += 1
        max_freq = 0
        elem = 0
        for key in freq_dict.keys():
            val = freq_dict[key]
            if val > max_freq:
                max_freq = val
                elem = key
        return elem
 
