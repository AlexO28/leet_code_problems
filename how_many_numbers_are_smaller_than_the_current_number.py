# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums2 = nums.copy()
        nums2.sort()
        num_dict = {}
        for j in range(len(nums2)):
            if nums2[j] not in num_dict:
                num_dict[nums2[j]] = j
        res = []
        for num in nums:
            if num in num_dict:
                res.append(num_dict[num])
            else:
                res.append(0)
        return res
