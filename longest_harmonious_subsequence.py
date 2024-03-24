# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
# A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        num_dict = {}
        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        keys = list(num_dict.keys())
        keys.sort()
        res = 0
        for key in keys:
            cur_res = num_dict[key]
            if key+1 in num_dict:
                cur_res_1 = cur_res + num_dict[key+1]
            else:
                cur_res_1 = -1
            if key-1 in num_dict:
                cur_res_2 = cur_res + num_dict[key-1]
            else:
                cur_res_2 = -1
            res = max(res, max(cur_res_1, cur_res_2))
        return res
