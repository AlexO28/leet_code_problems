# Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
# You may assume the input array always has a valid answer.
import numpy as np


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_new = nums.copy()
        nums_new.sort()
        mid_point = int(np.ceil(len(nums_new) / 2))
        i1 = 0
        i2 = mid_point
        for j in range(len(nums)):
            if j % 2 == 0:
                nums[j] = nums_new[i1]
                i1 += 1
            else:
                nums[j] = nums_new[i2]
                i2 += 1
        greater = True
        terminated = False
        for j in range(len(nums)-1):
            if greater:
                if nums[j+1] <= nums[j]:
                    terminated = True
                    break
                else:
                    greater = False
            else:
                if nums[j+1] >= nums[j]:
                    terminated = True
                    break
                else:
                    greater = True
        if terminated:
            i1 = mid_point-1
            i2 = len(nums_new)-1
            for j in range(len(nums)):
                if j % 2 == 0:
                   nums[j] = nums_new[i1]
                   i1 -= 1
                else:
                   nums[j] = nums_new[i2]
                   i2 -= 1
