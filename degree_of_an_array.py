# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        freq_dict = {}
        min_dict = {}
        max_dict = {}
        for j in range(len(nums)):
            if nums[j] in freq_dict:
                freq_dict[nums[j]] += 1
                max_dict[nums[j]] = j - min_dict[nums[j]] + 1
            else:
                freq_dict[nums[j]] = 1
                min_dict[nums[j]] = j
        max_freq = max(list(freq_dict.values()))
        if max_freq == 1:
            return 1
        vals = []
        for key in freq_dict.keys():
            if freq_dict[key] == max_freq:
                vals.append(max_dict[key])
        return min(vals)
