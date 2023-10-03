# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_dict = {}
        num_pairs = 0
        for num in nums:
            if num not in num_dict.keys():
                num_dict[num] = 1
            else:
                num_pairs += num_dict[num]
                num_dict[num] += 1
        return num_pairs
