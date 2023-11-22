# Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                k = i + j
                if k in nums_dict.keys():
                    nums_dict[k].append(nums[i][j])
                else:
                    nums_dict[k] = [nums[i][j]]
        keys = list(nums_dict.keys())
        keys.sort()
        res = []
        for key in keys:
            res.extend(nums_dict[key][::-1])
        return res
