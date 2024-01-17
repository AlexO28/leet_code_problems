# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_dict = {}
        for elem in arr:
            if elem in freq_dict:
                freq_dict[elem] += 1
            else:
                freq_dict[elem] = 1
        values = list(freq_dict.values())
        return len(values) == len(list(set(values)))
