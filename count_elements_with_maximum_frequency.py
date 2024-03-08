# You are given an array nums consisting of positive integers.
# Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
# The frequency of an element is the number of occurrences of that element in the array.
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        freq_dict = {}
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        vals = list(freq_dict.values())
        vals.sort(reverse=True)
        for j in range(1, len(vals)):
            if vals[j] != vals[0]:
                return j * vals[0]
        return len(vals) * vals[0]
