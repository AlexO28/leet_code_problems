# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
import math


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 6:
            return self.findProduct(nums)
        else:
            temp = nums[:3]
            temp.extend(nums[(len(nums)-3):])
            return self.findProduct(temp)

    def findProduct(self, arr):
        max_prod = -math.inf
        for i in range(len(arr)-2):
            for j in range(i+1, len(arr)-1):
                for k in range(j+1, len(arr)):
                    max_prod = max(max_prod, arr[i]*arr[j]*arr[k])
        return max_prod
